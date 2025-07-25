from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from dotenv import load_dotenv
from social_post_model.core.prompts.social_post_prompts import (
    social_post_update_prompt,
    query_checker_prompt,
)
from typing import Any
import json

load_dotenv()


class SocialPostUpdateContent(BaseModel):
    updated_text: str = Field(
        ..., description="Here is the updated text of the social post"
    )


class QueryValidator(BaseModel):
    score: int = Field(
        ..., description="Score 0 if query is invalid and 1 if it is valid"
    )
    reason: str = Field(
        default="",
        description=' Empty string ""  if score is 1 and query is valid and enter a proper reason why if the query is invalid and score is 0',
    )


llm = ChatOpenAI(model="gpt-4.1", temperature=0, max_retries=3, use_responses_api=True)


async def update_social_post_chain(
    query,
    text_to_change,
    section,
    current_output,
    brand_guide,
    welcome_call_details,
    website_summary,
) -> Any:
    llms = llm.with_structured_output(SocialPostUpdateContent)
    update_chain = social_post_update_prompt | llms
    input_data = {
        "query": query,
        "text_to_change": text_to_change,
        "section": section,
        "current_output": current_output,
        "brand_guide": brand_guide,
        "welcome_call_details": welcome_call_details,
        "website_summary": website_summary,
    }
    response = await update_chain.ainvoke(input_data)
    return response.updated_text


async def validate_query_chain(query):
    llmo = llm.with_structured_output(QueryValidator)
    query_chain = query_checker_prompt | llmo
    input_data = {"search_query_or_request": query}
    response = await query_chain.ainvoke(input_data)
    output = json.loads(response.model_dump_json())
    return output
