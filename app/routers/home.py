from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
import ast
import json
import traceback

import pandas as pd

from social_post_model.core.chains.social_post_chains import (
    update_social_post_chain,
    validate_query_chain,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)

df = pd.read_excel("SocialPost.xlsx")
columns = df.columns.to_list()
data = df[columns].to_dict(orient="records")


def clean_quotes(text):
    """Clean curly quotes and other problematic characters"""
    if isinstance(text, str):
        # Replace curly quotes with straight quotes
        text = text.replace(""", "'").replace(""", "'")
        text = text.replace('"', '"').replace('"', '"')
        text = text.replace("…", "...")  # Replace ellipsis
    return text


def get_website_summary(summary):
    # If it's already a dict, return as is
    if isinstance(summary, dict):
        return summary
    try:
        # Clean the summary string before parsing
        summary = clean_quotes(summary)

        # Try to parse as dict (only works if the string is a valid literal)
        parsed = ast.literal_eval(summary)
        if isinstance(parsed, dict):
            return parsed
        else:
            # If it's not a dict after parsing, wrap in dict
            return {"Overview of the business": summary}
    except Exception as e:
        logger.warning(f"Failed to parse website summary: {e}")
        # If parsing fails, wrap in dict
        return {"Overview of the business": str(summary)}


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/submit", response_class=HTMLResponse)
async def submit(
    request: Request, set_number: int = Form(...), post_number: int = Form(...)
):
    try:
        display_data = data[set_number - 1]
        post = post_number - 1

        # Clean data before parsing
        brand_guide_str = clean_quotes(display_data["BrandGuide"])
        brand_guide = ast.literal_eval(brand_guide_str)

        website_summary = get_website_summary(display_data["Website summary"])

        welcome_call_str = clean_quotes(display_data["Welcomecall Details"])
        welcome_call_details = json.loads(welcome_call_str)

        social_post_str = clean_quotes(display_data["Social Post (9V)"])
        social_post = ast.literal_eval(social_post_str)

        specific_post = social_post["posts"][post]

        return templates.TemplateResponse(
            "result.html",
            {
                "request": request,
                "set_number": set_number,
                "post_number": post_number,
                "specific_post": specific_post,
                "website_summary": website_summary,
                "brand_guide": brand_guide,
                "welcome_call_details": welcome_call_details,
            },
        )
    except Exception as e:
        logger.error(f"Error in submit: {str(e)}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        # Return error page or redirect
        return templates.TemplateResponse(
            "error.html", {"request": request, "error": str(e)}
        )


@router.post("/update_post")
async def update_post(
    set_number: int = Form(...),
    post_number: int = Form(...),
    selected_text: str = Form(...),
    user_message: str = Form(...),
    field_type: str = Form(...),  # 'post_text' or 'category'
):
    """
    Update specific post text or category based on user input

    Args:
        set_number: The set number (1-based)
        post_number: The post number (1-based)
        selected_text: The text user selected
        user_message: The user's request for changes
        field_type: Which field to update ('post_text' or 'category')
    """

    try:
        # Get the specific data row
        display_data = data[set_number - 1]

        # Validate the user query first
        check_query = await validate_query_chain(user_message)
        print(f"Validation score: {check_query['score']}")
        print(f"Validation reason: {check_query['reason']}")

        # If validation fails (score is 0), return the reason without updating
        if check_query["score"] == 0:
            return {
                "success": False,
                "validation_failed": True,
                "reason": check_query["reason"],
                "error": "Query validation failed",
            }

        # Continue with the update process if validation passes
        # Clean and parse social post data
        social_post_str = clean_quotes(display_data["Social Post (9V)"])
        social_post = ast.literal_eval(social_post_str)
        specific_post = social_post["posts"][post_number - 1]

        print(f"User message: {user_message}")

        # Get additional context data
        brand_guide_str = clean_quotes(display_data["BrandGuide"])
        brand_guide = ast.literal_eval(brand_guide_str)

        website_summary = get_website_summary(display_data["Website summary"])

        welcome_call_str = clean_quotes(display_data["Welcomecall Details"])
        welcome_call_details = json.loads(welcome_call_str)

        # Call the AI update function
        updated_value = await update_social_post_chain(
            user_message,
            selected_text,
            field_type,
            specific_post,
            brand_guide,
            welcome_call_details,
            website_summary,
        )

        # Update the specific field in the social post
        if field_type == "post_text":
            social_post["posts"][post_number - 1]["Post"] = updated_value
            return_value = updated_value
        elif field_type == "category":
            social_post["posts"][post_number - 1]["Category"] = updated_value
            return_value = updated_value
        else:
            # If field_type is neither, assume it's the updated value for post text
            social_post["posts"][post_number - 1]["Post"] = updated_value
            return_value = updated_value

        # Update the data in memory (save the entire social_post object, not just the updated_value)
        data[set_number - 1]["Social Post (9V)"] = str(social_post)

        print(f"Successfully updated {field_type} with value: {return_value}")

        # Return the updated field value
        return {
            "success": True,
            "updated_value": return_value,
            "field_type": field_type,
        }

    except Exception as e:
        logger.error(f"Error updating post: {str(e)}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}
