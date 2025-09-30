from social_post_model.core.chains.social_post_chains import (
    update_social_post_chain,
    validate_query_chain,
    guardrails_check_chain,
)
import asyncio


## Inputs
query = """Replace technical jargon, industry-specific terminology, and complex vocabulary with accessible, everyday language that broader audiences understand
Break down long, complex sentences into multiple shorter, clearer statements that improve comprehension and readability
Convert passive voice constructions to active voice to create more direct, engaging, and easier-to-follow content
Substitute sophisticated or academic language with simpler alternatives while maintaining the professional credibility of the content
Ensure final output remains within 10 percent of original word count while significantly improving accessibility and understanding for target audience
"""

text_to_change = "Posts in this category focus on guiding first-time buyers and seasone"

section = "objective"

current_output = {
    "Post Number": 2,
    "Category": "Real Estate Guidance- Home Buying Support",
    "Objective": "Posts in this category focus on guiding first-time buyers and seasoned purchasers through the home buying process, offering clear, knowledgeable advice tailored to their needs.",
    "Post": "Buying a home this summer can be stress-free with my step-by-step guidance. I clarify each part of the process and answer your questions, so you feel confident every step. Let's discuss your goals—reach out for support designed just for you. #HomeBuyingSupport #LondonOntarioRealEstate",
    "Source": None,
    "Why this post": "Empowers buyers with clear, actionable guidance for the summer market, reinforcing Krystle's supportive approach.",
    "Schedule Date": "Jul 4, 2025",
    "Image Recommendations": [
        {
            "description": "Krystle Jesko reviewing listings with a client at a sunlit desk, both smiling and engaged."
        },
        {
            "description": "A joyful new homeowner holding keys in front of their London, Ontario house."
        },
        {
            "description": "A map of London, Ontario neighborhoods with personalized notes and highlights."
        },
    ],
    "Caption": "Guided home buying steps.",
}

brand_guide = {
    "Short Business Description": "Empower your property journey in London, Ontario, with expert insight and genuine guidance. Connect to achieve your real estate goals today.",
    "Detailed Business Overview": "Krystle Jesko Real Estate delivers client-focused real estate solutions in London, Ontario, drawing on 10 years of hands-on expertise. Krystle specializes in residential buying, selling, investment guidance, relocation assistance, and home renovation advice. Her background as a former licensed nutritionist enriches her personalized, supportive approach. Whether you're a first-time buyer, investor, or navigating life transitions, Krystle offers market knowledge, practical renovation insight, and staging support. Reach out for tailored service from a trustworthy local expert dedicated to your success.",
    "Website Font": [{"Title": "monaco", "Body": "Arial"}],
    "Recommended Font": [{"Title": "Open Sans", "Body": "Roboto"}],
    "Website Colors": ["#313131", "#000000", "#0051C3"],
    "Recommended Color": {
        "Primary_color": {"Hex Code": "#313131", "Color name": "Charcoal Gray"},
        "Secondary_color": {"Hex Code": "#0051C3", "Color name": "Royal Blue"},
        "Accent_color": [
            {"Hex Code": "#F2C6CF", "Color name": "Soft Pink"},
            {"Hex Code": "#E3E3E3", "Color name": "Light Silver Gray"},
        ],
    },
    "Point of View": "I/Me/My",
    "Voice": [{"Primary": "Sincere", "Secondary": "Knowledgeable"}],
    "Brand Personality Traits": [
        "Trustworthy",
        "Dependable",
        "Professional",
        "Personable",
        "Friendly",
        "Knowledgeable",
        "Minimal (Visual Trait)",
    ],
    "Hashtags": [
        "KrystleJeskoRealEstate",
        "HomeBuyingSupport",
        "OntarioPropertySellingExpert",
        "RealEstateInvestingTips",
        "LifeTransitionRealEstate",
        "LondonOntarioRealEstate",
        "RoyalLePageShelterSupport",
    ],
}

welcome_call_details = {
    "websiteId": "66005c03-e4fa-4410-b06b-2cae4c76a8c0",
    "aboutYourCommunity": "1399 Commissioners Rd W\n23\nLondon, Ontario CA N6K4G9\nCanada about a 60 mile radius",
    "bizShowHours": False,
    "saleChannels": {"physicalLocation": True},
    "competitiveStandout": "Connecting with\nHer client's personality and life experience, and she is personable.Life experience. Estate sale, she can handle or a divorce, she can handle any situation",
    "currentWebsiteExists": "yes",
    "longDescription": "I'm Krystle Jesko, a real estate sales representative with nearly a decade of experience in property management, real estate investing, and full-scale home renovations. My journey began with a deep passion for helping people through life's transitions—something I carried from my former career as a licensed nutritionist. That background taught me how to listen, support, and guide others through important decisions—skills I use daily with buyers, sellers, and investors. I bring a calm, confident presence, a coach's mindset, and a sharp eye for potential others might miss. Whether it's guiding first-time buyers, advising investors, or helping families with estate sales and staging, I empower my clients with knowledge and clarity. My mission is to make real estate less overwhelming and more meaningful—every step of the way. I'm also proud to support the Royal LePage Shelter Foundation, helping provide safe housing for women and children.",
    "hasProductsUpToDate": "yes",
    "howDoYouReferYourBusiness": "I",
    "keyTerms": "Services, Real estate listings she offers, ",
    "ongoingSocialPostApproval": True,
    "partnershipGoals": "Hoping to help with social media presence and help gain clients and brand awareness",
    "reviewApproval": True,
    "showContactInfo": "yes",
    "targetAudience": "25-65 male or female",
    "timeInBusiness": "10 years",
    "areasOfFocus": [
        "I bring close to ten years of hands-on experience in real estate sales, property management, investing, and full-scale home renovations",
        "Offering tailored real estate guidance for buyers, sellers, and investors—ranging from market education and full-service staging to strategic investment insights and support with estate sales",
        "Specialized in helping first-time home buyers feel confident, assisting families navigating estate transitions, and identifying hidden value in properties for both personal and investment purposes",
        "What sets me apart is how I combine practical renovation knowledge with compassionate, client-focused care, giving my clients a clear vision of a property's potential and the guidance to act on it with confidence",
        "I regularly share updates on market trends, property tips, open houses, and community initiatives I support—especially those tied to the Royal LePage Shelter Foundation",
    ],
    "brandAttributes": [
        "Trustworthy",
        "Dependable",
        "Professional",
        "Personable",
        "Friendly",
        "Knowledgeable",
    ],
    "brandKitColors": [
        {
            "name": "Black",
            "colorCode": "#000000",
            "guidelines": "This color and its shades will be used most often in your posts. It may be featured in backgrounds, design elements, and text.",
        },
        {
            "name": "white",
            "colorCode": "#ffffff",
            "guidelines": "This color and its shades will be used most often in your posts. It may be featured in backgrounds, design elements, and text.",
        },
        {
            "name": "Red",
            "colorCode": "#cb1f1f",
            "guidelines": "This color and its shades will be used most often in your posts. It may be featured in backgrounds, design elements, and text.",
        },
    ],
    "brandKitFonts": {
        "primary": {
            "font": "open-sans",
            "guidelines": "The title font is used for headlines and short phrases on social media graphics.",
        },
        "alternate": {
            "font": "roboto",
            "guidelines": "The body font will be used for social media graphics with a lot of text, like testimonials.",
        },
    },
    "brandReference": "Black, White, soft pink do not use the mustard or red on the website , she does not like that. ",
    "hashtags": [
        "#KrystleJeskoRealEstate",
        "#HomeBuyingSupport",
        "#OntarioPropertySellingExpert",
        "#RealEstateInvestingTips",
        "#LifeTransitionRealEstate",
    ],
    "imageGuidelines": [""],
    "implementationGuidelines": [""],
    "logo": {
        "url": "https://img1.wsimg.com/blobby/go/66005c03-e4fa-4410-b06b-2cae4c76a8c0/1744072064810_1744007908332_Spiritual_20Sanctu.png",
        "guidelines": "Your primary logo will appear in posts that utilize the custom backgrounds we've designed for you.",
    },
    "shortBrandDescription": "Navigate your real estate journey with confidence through personalized guidance and practical insight. Let's talk about your home goals, connect with me today!",
    "voiceToneGuidelines": [
        "I use minimal visual style while designing the content",
        "Voice: Reliable, sincere",
        "Hashtags: Use a minimum of one for each week",
        "Service Areas:   Serving clients throughout London, Ontario and surrounding area around 60 miles radius",
        "Target Audience: Individuals aged between 25-65, couples, and families navigating home buying, selling, or life transitions with personalized, knowledgeable real estate guidance\n",
    ],
    "businessName": "Krystle Jesko Real Estate ",
    "businessType": "Real Estate Agent",
    "domain": "https://krystlejesko.royallepage.ca/",
    "phoneNumbers": [{"type": "cell", "phone": "+1.5197777942"}],
    "marketingServicesPlan": "difyMarketingServicesNwPremium",
}

website_summary = {
    "Overview of the business": "Website Summary\nOverview of the business\nKrystle Jesko is a sales representative for Royal LePage Triland Realty, based at Waterloo St. brokerage in London, Ontario. She specializes in real estate services, offering expertise in buying, selling, relocating, and home renovation advice.\n\nAbout the business\nKrystle transitioned into real estate full-time after a successful career as a Licensed Nutritionist. With almost a decade of experience as a Real Estate investor and Property Manager, she provides hands-on advice and first-class service. Born and raised in London, she has in-depth knowledge of the local community and real estate market.\n\nMission and Vision of the business\nMission: To provide exceptional real estate services with a focus on client satisfaction, leveraging extensive market knowledge and hands-on experience. Vision: To be the go-to real estate agent in the London, Ontario area for excellent customer service, comprehensive market understanding, and valuable home renovation advice.\n\nList of Primary and secondary Products or Services they provide\nPrimary Services: Buying and selling residential properties, Home renovation advice, Real estate investment consultancy, Relocation services.Secondary Services: Market analysis, Open house events, Eco-friendly home listings, Senior (55+) community real estate.\nTarget Audience\nThe target audience includes home buyers, sellers, investors, individuals seeking relocation, and those needing home renovation advice within the London, Ontario area.\n\nBusiness Category\nReal Estate Services and Consultancy\n\nLocal area\nLocated in London, Ontario, known as 'The Forest City,' the business operates out of 103-240 Waterloo St.\n\nAbout the community they serve\nKrystle serves the vibrant and diverse community of London, Ontario, which offers a mix of cultural, recreational, and educational opportunities. She focuses on areas significant to families, professionals, investors, and retirees.\n\nCompetitive standout\nKrystle's background in nutrition, combined with extensive experience in real estate investment and property management, sets her apart. Her knowledge of home renovations and local market insights make her a trusted advisor.\n\nNew customer demographics\nNew customers include individuals or families looking for residential properties, investors seeking lucrative opportunities, and seniors looking for age-friendly housing.\n\nUnique selling proposition\nKrystle combines her passion for improving quality of life with her practical real estate experience, providing comprehensive and personalized services to her clients. Her compassionate, knowledgeable, and dedicated approach ensures client satisfaction and success in their real estate endeavors."
}

length_post = 9


# Query Validator
async def main():
    check_query, guardrails_check = await asyncio.gather(
        validate_query_chain(query),
        guardrails_check_chain(query, section),
    )
    print(check_query)
    print(guardrails_check)

    if check_query["score"] == 1 and guardrails_check["score"] == 1:
        updated_value = await update_social_post_chain(
            query=query,  # Use the final_message (either original or mapped standard action)
            text_to_change=text_to_change,
            section=section,
            current_output=current_output,
            brand_guide=brand_guide,
            welcome_call_details=welcome_call_details,
            website_summary=website_summary,
            length_post=length_post,
        )
        print(updated_value)


asyncio.run(main())
