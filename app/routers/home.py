from fastapi import APIRouter, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import logging
import ast
import json

import pandas as pd

router = APIRouter()
templates = Jinja2Templates(directory="templates")
logger = logging.getLogger(__name__)

df = pd.read_excel("SocialPost.xlsx")
columns = df.columns.to_list()
data = df[columns].to_dict(orient="records")


def get_website_summary(summary):
    # If it's already a dict, return as is
    if isinstance(summary, dict):
        return summary
    try:
        # Try to parse as dict (only works if the string is a valid literal)
        parsed = ast.literal_eval(summary)
        if isinstance(parsed, dict):
            return parsed
        else:
            # If it's not a dict after parsing, wrap in dict
            return {"Overview of the business": summary}
    except Exception:
        # If parsing fails, wrap in dict
        return {"Overview of the business": summary}


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@router.post("/submit", response_class=HTMLResponse)
async def submit(
    request: Request, set_number: int = Form(...), post_number: int = Form(...)
):
    display_data = data[set_number - 1]
    post = post_number - 1
    brand_guide = ast.literal_eval(display_data["BrandGuide"])
    website_summary = get_website_summary(display_data["Website summary"])
    welcome_call_details = json.loads(display_data["Welcomecall Details"])
    social_post = ast.literal_eval(display_data["Social Post (9V)"])
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
