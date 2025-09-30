from social_post_model.utils.constants import STANDARD_ACTION_PROMPTS
from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
import ast
import json
import asyncio
import traceback

import pandas as pd

from social_post_model.core.chains.social_post_chains import (
    update_social_post_chain,
    validate_query_chain,
    guardrails_check_chain,
)

router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)

df = pd.read_excel("SocialPost.xlsx")
columns: list[str] = df.columns.to_list()
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
    field_type: str = Form(...),  # 'post_text', 'category', 'objective', or 'caption'
    is_standard_action: str = Form(default="false"),  # "true" or "false"
    action_type: str = Form(default=""),  # The standard action key if applicable
):
    """
    Update specific post fields based on user input or standard actions

    Args:
        set_number: The set number (1-based)
        post_number: The post number (1-based)
        selected_text: The text user selected
        user_message: The user's request for changes (or mapped standard action prompt)
        field_type: Which field to update ('post_text', 'category', 'objective', or 'caption')
        is_standard_action: Whether this is a standard action or custom query
        action_type: The key of the standard action if applicable
    """

    try:
        # Get the specific data row
        display_data = data[set_number - 1]

        # Handle standard actions by mapping to predefined prompts
        final_message = user_message
        if (
            is_standard_action.lower() == "true"
            and action_type in STANDARD_ACTION_PROMPTS
        ):
            final_message = STANDARD_ACTION_PROMPTS[action_type]
            logger.info(f"Using standard action '{action_type}': {final_message}")

        # Validate the query first
        check_query, guardrails_check = await asyncio.gather(
            validate_query_chain(final_message),
            guardrails_check_chain(final_message, field_type),
        )

        logger.info(f"Validation score: {check_query['score']}")
        logger.info(f"Validation reason: {check_query['reason']}")
        logger.info(f"Field type: {field_type}")
        logger.info(f"Guardrails check score: {guardrails_check['score']}")
        logger.info(f"Guardrails check reason: {guardrails_check['reason']}")
        logger.info(f"Is standard action: {is_standard_action}")
        logger.info(f"Action type: {action_type}")

        # If validation fails (score is 0), return the reason without updating
        if check_query["score"] == 0:
            return {
                "success": False,
                "validation_failed": True,
                "reason": check_query["reason"],
                "error": "Query validation failed",
            }

        elif guardrails_check["score"] == 0:
            return {
                "success": False,
                "guardrails_failed": True,
                "reason": guardrails_check["reason"],
                "error": "Guardrails check failed",
            }

        # Continue with the update process if validation passes
        # Clean and parse social post data
        social_post_str = clean_quotes(display_data["Social Post (9V)"])
        social_post = ast.literal_eval(social_post_str)
        specific_post = social_post["posts"][post_number - 1]

        logger.info(f"Final message being processed: {final_message}")

        # Get additional context data
        brand_guide_str = clean_quotes(display_data["BrandGuide"])
        brand_guide = ast.literal_eval(brand_guide_str)

        website_summary = get_website_summary(display_data["Website summary"])

        welcome_call_str = clean_quotes(display_data["Welcomecall Details"])
        welcome_call_details = json.loads(welcome_call_str)
        length_post_length = len(specific_post)

        # Call the AI update function with the final message
        updated_value = await update_social_post_chain(
            query=final_message,  # Use the final_message (either original or mapped standard action)
            text_to_change=selected_text,
            section=field_type,
            current_output=specific_post,
            brand_guide=brand_guide,
            welcome_call_details=welcome_call_details,
            website_summary=website_summary,
            length_post=length_post_length,
        )

        # Update the specific field in the social post
        if field_type == "post_text":
            social_post["posts"][post_number - 1]["Post"] = updated_value
            return_value = updated_value
        elif field_type == "category":
            social_post["posts"][post_number - 1]["Category"] = updated_value
            return_value = updated_value
        elif field_type == "objective":
            social_post["posts"][post_number - 1]["Objective"] = updated_value
            return_value = updated_value
        elif field_type == "caption":
            social_post["posts"][post_number - 1]["Caption"] = updated_value
            return_value = updated_value
        else:
            # If field_type is none of the above, assume it's the updated value for post text
            social_post["posts"][post_number - 1]["Post"] = updated_value
            return_value = updated_value

        # Update the data in memory (save the entire social_post object, not just the updated_value)
        data[set_number - 1]["Social Post (9V)"] = str(social_post)

        action_info = (
            f" (Standard Action: {action_type})"
            if is_standard_action.lower() == "true"
            else ""
        )
        logger.info(
            f"Successfully updated {field_type} with value: {return_value}{action_info}"
        )

        # Return the updated field value
        return {
            "success": True,
            "updated_value": return_value,
            "field_type": field_type,
            "is_standard_action": is_standard_action.lower() == "true",
            "action_type": action_type
            if is_standard_action.lower() == "true"
            else None,
        }

    except Exception as e:
        logger.error(f"Error updating post: {str(e)}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}


@router.post("/confirm_update")
async def confirm_update(
    set_number: int = Form(...),
    post_number: int = Form(...),
    field_type: str = Form(...),
    updated_value: str = Form(...),
):
    """
    Confirm and persist the updated post field to the data store

    Args:
        set_number: The set number (1-based)
        post_number: The post number (1-based)
        field_type: Which field was updated ('post_text', 'category', 'objective', or 'caption')
        updated_value: The final updated value to persist
    """
    try:
        # Get the specific data row
        display_data = data[set_number - 1]

        # Clean and parse social post data
        social_post_str = clean_quotes(display_data["Social Post (9V)"])
        social_post = ast.literal_eval(social_post_str)

        # Update the specific field in the social post
        if field_type == "post_text":
            social_post["posts"][post_number - 1]["Post"] = updated_value
        elif field_type == "category":
            social_post["posts"][post_number - 1]["Category"] = updated_value
        elif field_type == "objective":
            social_post["posts"][post_number - 1]["Objective"] = updated_value
        elif field_type == "caption":
            social_post["posts"][post_number - 1]["Caption"] = updated_value
        else:
            # Default to post text if field_type is not recognized
            social_post["posts"][post_number - 1]["Post"] = updated_value

        # Update the data in memory
        data[set_number - 1]["Social Post (9V)"] = str(social_post)

        logger.info(f"Confirmed and persisted update for {field_type}: {updated_value}")

        return {
            "success": True,
            "message": "Changes confirmed and saved successfully",
            "field_type": field_type,
            "updated_value": updated_value,
        }

    except Exception as e:
        logger.error(f"Error confirming update: {str(e)}")
        logger.error(f"Full traceback: {traceback.format_exc()}")
        return {"success": False, "error": str(e)}
