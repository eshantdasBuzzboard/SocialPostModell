# Social Post Model - AI-Powered Social Media Content Update System

A Python-based AI system for intelligent social media post updates with built-in guardrails and validation for brand consistency.

## Overview

The Social Post Model provides developers with a simple interface to validate and update social media post content using AI. The system includes comprehensive guardrails to ensure content updates meet brand guidelines and social media best practices before processing.

## Features

- **Guardrails Validation**: Automated checks to ensure content updates comply with brand guidelines and social media standards
- **AI-Powered Content Generation**: Generates updated content suggestions based on user queries
- **Standard Action Prompts**: Pre-defined optimized queries for common editing tasks
- **Asynchronous Processing**: High-performance parallel execution for fastest results
- **Simple API**: Only 3 functions needed for complete functionality

## Installation

1. Clone the repository
2. Install dependencies:
```bash
   pip install -r requirements.txt
```

3. Set up environment variables: Create a .env file in the root directory and add your OpenAI API key:
```
   OPENAI_API_KEY="your-openai-api-key-here"
```

## Requirements

- python-dotenv
- langchain
- langchain_openai

## Usage

### Import Required Functions

```python
from social_post_model.core.chains.social_post_chains import (
    update_social_post_chain,
    validate_query_chain,
    guardrails_check_chain,
)
import asyncio
```

### Step 1: Validation

Before updating any content, always run both validation checks:

```python
check_query, guardrails_check = await asyncio.gather(
    validate_query_chain(query),
    guardrails_check_chain(query, section),
)
```

#### Understanding Validation Results

The functions return two validation scores:

**Successful Validation (Both Pass)**
```python
{'score': 1, 'reason': ''}
{'score': 1, 'reason': ''}
```
✅ Proceed to content update

**Failed Validation (One or Both Fail)**
```python
{'score': 1, 'reason': ''}
{'score': 0, 'reason': 'The query violates brand voice guidelines by requesting overly formal language.'}
```
❌ Do NOT proceed - Display reason to user

### Step 2: Content Update (Only if validation passes)

If both validation scores are 1, proceed with content update:

```python
if check_query["score"] == 1 and guardrails_check["score"] == 1:
    updated_value = await update_social_post_chain(
        query=query,
        text_to_change=text_to_change,
        section=section,
        current_output=current_output,
        brand_guide=brand_guide,
        welcome_call_details=welcome_call_details,
        website_summary=website_summary,
        length_post=length_post,
    )
    print(updated_value)
```

## Input Parameters

### Required Parameters

- **query** (str): The user's request for content modification
- **text_to_change** (str): The specific text selected by the user to be modified
- **section** (str): The section being updated (e.g., "Post", "Caption", "Objective", "Category")
- **current_output** (dict): The complete current post data structure
- **brand_guide** (dict): Brand guidelines including voice, personality traits, colors, fonts, hashtags
- **welcome_call_details** (dict): Business information from onboarding including description, services, target audience
- **website_summary** (dict): Website content summary with business overview and unique selling propositions
- **length_post** (int): Current character length of the post content

## Standard Action Prompts

The system includes pre-defined optimized queries for common editing tasks. These can be used instead of custom queries:

### Available Standard Actions

#### **fix-language**
Improves the natural flow and readability of content by:
- Identifying and replacing awkward phrasing with smooth, conversational language
- Restructuring sentences that sound robotic or artificial
- Eliminating repetitive words or phrases that appear too close together
- Maintaining the original meaning and length while enhancing readability

#### **make-shorter**
Reduces content length by 20-30% while preserving all essential information:
- Removes unnecessary filler words and redundant qualifiers
- Consolidates duplicate concepts expressed in different ways
- Eliminates wordy introductions and verbose explanations
- Cuts redundant descriptive elements while keeping key details

#### **simplify**
Makes content more accessible to a broader audience by:
- Replacing technical jargon with everyday language
- Breaking complex sentences into shorter, clearer statements
- Converting passive voice to active voice where appropriate
- Using simpler vocabulary while maintaining professionalism
- Keeping within 10% of the original word count

#### **improve-consistency**
Creates unified messaging across content by:
- Establishing consistent terminology and key phrases
- Standardizing tone and communication style per brand guidelines
- Resolving any contradictory statements or conflicting information
- Ensuring logical flow between related content pieces
- Maintaining exact original character count

#### **more-salesy**
Enhances persuasive elements without being pushy by:
- Adding benefit-focused language that emphasizes outcomes and value
- Including strategic urgency elements that motivate action
- Highlighting unique selling points and competitive advantages
- Incorporating credibility markers and social proof
- Strengthening calls-to-action throughout the content
- Using only verified business information from provided sources
- Maintaining exact original character count

#### **less-salesy**
Transforms promotional content into educational, relationship-building material by:
- Removing aggressive sales language and pushy tactics
- Converting product-focused messaging to value-driven content
- Establishing a helpful, consultative tone
- Leading with educational insights before commercial mentions
- Replacing hard-sell approaches with natural recommendations
- Maintaining exact original character count

#### **add-cta**
Inserts clear action steps and engagement opportunities by:
- Adding specific instructions that guide readers toward desired actions
- Including verified contact information and engagement pathways
- Creating compelling urgency or valuable incentives
- Making next steps obvious and easily accessible
- Providing multiple engagement options for different preferences
- Using only business information provided in source materials
- Maintaining exact original character count

#### **remove-repetitions**
Eliminates redundancy while preserving content richness by:
- Identifying and consolidating duplicate information or concepts
- Removing redundant examples that don't add new insights
- Eliminating circular reasoning patterns
- Preserving content variety while removing true repetition
- Maintaining all essential information in streamlined format

#### **match-brand**
Aligns content with established brand identity by:
- Applying brand-specific vocabulary and signature phrases
- Adjusting tone and formality to match brand guidelines
- Ensuring consistent point of view and narrative perspective
- Integrating brand's preferred emotional tone and energy level
- Using documented voice and tone standards from brand guide
- Maintaining exact original character count

#### **fix-errors**
Verifies and corrects all factual information by:
- Cross-referencing statistics and claims against provided documentation
- Removing unverified or unsupported statements
- Validating company information against business documentation
- Replacing inaccuracies with properly sourced information
- Ensuring pricing and promotional details reflect current status
- Using only information from Welcome Call, Brand Guide, and Website Summary

### Using Standard Actions

```python
from social_post_model.utils.constants import STANDARD_ACTION_PROMPTS

# Instead of custom query
query = STANDARD_ACTION_PROMPTS["simplify"]

# Then proceed with validation and update as normal
check_query, guardrails_check = await asyncio.gather(
    validate_query_chain(query),
    guardrails_check_chain(query, section),
)
```

## Complete Example

```python
from social_post_model.core.chains.social_post_chains import (
    update_social_post_chain,
    validate_query_chain,
    guardrails_check_chain,
)
import asyncio

async def main():
    # User query (can be custom or from STANDARD_ACTION_PROMPTS)
    query = """Replace technical jargon with accessible, everyday language.
    Break down complex sentences into shorter, clearer statements.
    Ensure output remains within 10 percent of original word count."""
    
    # Text selected by user
    text_to_change = "Posts in this category focus on guiding first-time buyers and seasone"
    
    # Section being updated
    section = "objective"
    
    # Current post data
    current_output = {
        "Post Number": 2,
        "Category": "Real Estate Guidance- Home Buying Support",
        "Objective": "Posts in this category focus on guiding first-time buyers and seasoned purchasers through the home buying process, offering clear, knowledgeable advice tailored to their needs.",
        "Post": "Buying a home this summer can be stress-free with my step-by-step guidance...",
        "Caption": "Guided home buying steps."
    }
    
    # Brand guidelines
    brand_guide = {
        "Short Business Description": "Empower your property journey...",
        "Point of View": "I/Me/My",
        "Voice": [{"Primary": "Sincere", "Secondary": "Knowledgeable"}],
        "Brand Personality Traits": ["Trustworthy", "Dependable", "Professional"],
        "Hashtags": ["#KrystleJeskoRealEstate", "#HomeBuyingSupport"]
    }
    
    # Business information
    welcome_call_details = {
        "businessName": "Krystle Jesko Real Estate",
        "businessType": "Real Estate Agent",
        "targetAudience": "25-65 male or female",
        "timeInBusiness": "10 years"
    }
    
    # Website summary
    website_summary = {
        "Overview of the business": "Krystle Jesko is a sales representative for Royal LePage..."
    }
    
    length_post = 9
    
    # Step 1: Validation
    check_query, guardrails_check = await asyncio.gather(
        validate_query_chain(query),
        guardrails_check_chain(query, section),
    )
    
    print(f"Query Check: {check_query}")
    print(f"Guardrails Check: {guardrails_check}")
    
    # Step 2: Check if both validations passed
    if check_query["score"] == 1 and guardrails_check["score"] == 1:
        # Proceed with content update
        updated_value = await update_social_post_chain(
            query=query,
            text_to_change=text_to_change,
            section=section,
            current_output=current_output,
            brand_guide=brand_guide,
            welcome_call_details=welcome_call_details,
            website_summary=website_summary,
            length_post=length_post,
        )
        print(f"Updated Content: {updated_value}")
    else:
        # Display validation failure reasons to user
        if check_query['score'] == 0:
            print(f"Query validation failed: {check_query['reason']}")
        if guardrails_check['score'] == 0:
            print(f"Guardrails validation failed: {guardrails_check['reason']}")

# Run the async function
asyncio.run(main())
```

## System Workflow

The system uses a simple 2-step process:

1. **Validation**: Use `validate_query_chain()` and `guardrails_check_chain()` to ensure the request meets guidelines
2. **Content Generation**: Use `update_social_post_chain()` to generate the updated content

Both validation functions must pass before proceeding to content generation.

## UI Integration Guidelines

### For Validation Flow:
- Call both validation functions using `asyncio.gather()`
- If either score is 0, display the reason to the user
- Only proceed if both scores are 1

### For Standard Actions:
- Present action buttons in your UI (e.g., "Simplify", "Make Shorter", "Fix Grammar")
- Map button clicks to `STANDARD_ACTION_PROMPTS` keys
- Use the mapped prompt as the query parameter
- Follow normal validation → update workflow

## Key Guidelines

- Always validate before updating content
- Use only verified information from provided business data
- Maintain brand voice and personality traits
- Ensure all content ends with proper punctuation
- Include minimum 2 hashtags from provided list
- No emojis, special characters, or banned words/phrases
- Keep content unique across posts (less than 20% similarity)

## Performance Notes

- Asynchronous parallel execution for validation ensures fastest possible results
- The 3-function workflow provides optimal performance characteristics
- Use `asyncio.gather()` for concurrent validation checks

## Support

For technical issues or questions about implementation, refer to `test_model.py` for complete working examples with exact data formats and usage patterns.