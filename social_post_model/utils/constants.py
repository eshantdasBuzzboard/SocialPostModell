STANDARD_ACTION_PROMPTS = {
    "fix-language": """Perform comprehensive scan to identify unnatural phrasing, forced transitions, and clunky sentence structures that disrupt reading flow
Replace overly complex word combinations with natural, conversational alternatives that maintain professional tone
Restructure sentences that sound robotic, stilted, or artificially constructed to create smoother, more engaging prose
Eliminate awkward repetition of identical words or phrases appearing too close together within paragraphs
Preserve the exact semantic meaning, core message, and original content length while improving readability and natural flow
""",
    "make-shorter": """Systematically remove unnecessary filler words, redundant qualifiers, and verbose phrases that add no meaningful value to the content
Identify and consolidate sentences or paragraphs that express the same concept multiple times in different ways
Eliminate wordy introductory phrases, unnecessary transitional elements, and verbose explanations that can be streamlined
Cut redundant adjectives, adverbs, and descriptive elements while maintaining the essential descriptive quality of the content
Achieve targeted reduction of 20-30 percent in total word count while absolutely preserving all critical information, data points, and key messaging
""",
    "simplify": """Replace technical jargon, industry-specific terminology, and complex vocabulary with accessible, everyday language that broader audiences understand
Break down long, complex sentences into multiple shorter, clearer statements that improve comprehension and readability
Convert passive voice constructions to active voice to create more direct, engaging, and easier-to-follow content
Substitute sophisticated or academic language with simpler alternatives while maintaining the professional credibility of the content
Ensure final output remains within 10 percent of original word count while significantly improving accessibility and understanding for target audience
""",
    "improve-consistency": """
Establish and apply uniform terminology, key phrases, and vocabulary across all selected posts to create cohesive messaging experience
Standardize tone, formality level, and communication style throughout the entire set of content pieces for brand coherence as provided in the BrandGuide
Identify and resolve contradictory statements, conflicting information, or misaligned messaging that appears across different posts
Create logical thematic connections and ensure complementary messaging flow between related content pieces within the selected set
Align all posts with consistent brand voice characteristics, ensuring unified presentation that reinforces overall marketing objectives
Maintain original Content length of  character exactly same as that.
""",
    "more-salesy": """Integrate compelling benefit-focused language that emphasizes outcomes, results, and value propositions to motivate reader action
Add strategic urgency elements and time-sensitive language that creates motivation to act quickly without appearing pushy
Highlight unique selling points, competitive advantages, and distinctive features that differentiate the offering from alternatives
Incorporate persuasive elements including social proof indicators, success metrics, and credibility markers that build confidence
Strengthen and multiply calls-to-action throughout the content to guide readers toward desired conversion behaviors and engagement
Do not claim/offer/inform about unverified business information which is not provided in the  Brand guide or Welcome call or Website summary
Maintain original Content length of  character exactly same as that.

""",
    "less-salesy": """Remove aggressive promotional language, pushy sales tactics, and overly direct marketing approaches that may alienate readers
Transform product-focused messaging into value-driven, educational content that builds relationships before introducing commercial elements
Establish helpful, consultative tone that positions the brand as trusted advisor rather than aggressive seller pushing products
Lead with educational value, useful insights, and practical information before introducing any commercial offers or product mentions
Replace hard-sell approaches with soft recommendations and natural suggestions that feel organic within valuable, informative content
Maintain original Content length of  character exactly same as that.
""",
    "add-cta": """Insert clear, specific action steps and instructions that guide readers toward desired behaviors with unambiguous direction
Include comprehensive contact information, links, and multiple pathways for readers to engage or respond to the content. Make sure all of these are sourced via Business Information provided to you. 
Do not generate URL or any links ,if not provided to you.
CTA should Create compelling urgency or valuable incentives that motivate immediate action without using high-pressure sales tactics
Make the next logical step obvious and easily accessible, removing friction and barriers that might prevent reader engagement
Develop multiple engagement options and response mechanisms to accommodate different reader preferences and comfort levels with taking action
Maintain original Content length of  character exactly same as that.
Make sure cta is always added towards the end of the section and not in the middle of it. It is compulsory.
""",
    "remove-repetitions": """Conduct thorough analysis to identify information, concepts, or points that are presented multiple times in different formats throughout the content
Consolidate duplicate messaging into single, comprehensive statements that maintain all essential information while eliminating redundancy
Remove redundant examples, case studies, or illustrations that reinforce the same point without adding new insights or perspectives
Eliminate circular reasoning patterns where conclusions are restated multiple times without advancing the argument or providing new information
Preserve content variety and supporting detail richness while systematically removing true repetition that adds no value to reader understanding
""",
    "match-brand": """Apply established brand-specific vocabulary, signature phrases, and distinctive communication patterns that reinforce brand identity throughout content
Adjust overall formality level, tone characteristics, and communication style to precisely match documented brand guidelines and personality traits as provided in the Brand guide or Welcome call.
Ensure consistent point of view, narrative perspective, and voice characteristics that align with brand's established communication approach
Integrate brand's preferred emotional tone, energy level, and personality markers that create recognizable brand experience for readers
Harmonize all language choices, style elements, and communication approaches with brand's documented voice and tone standards for authentic representation as provided in the Brand Guide
Maintain original Content length of  character exactly same as that.
""",
    "fix-errors": """Perform comprehensive cross-referencing of all statistics, data points, claims, and factual assertions against Welcome call, BrandGuide, Website content .
Identify and remove unverified claims, unsupported statements, and assertions that cannot be substantiated through provided business information.
Verify all company-specific information, product details, service descriptions, and organizational facts against provided business information documentation
Replace identified inaccuracies with properly sourced information that maintains content integrity and credibility only through Welcome call, BrandGuide, Website content .
Ensure all pricing information, promotional offers, availability claims, and time-sensitive details reflect current, accurate status and remain legally compliant and sourced ONLY through information provided to you
""",
    "standardize-mobile": """Identify all phone numbers, mobile numbers, and contact numbers throughout the content in their various existing formats
Convert all identified numbers to the standardized format: (XXX) XXX-XXXX, ensuring consistent presentation across all content
Apply uniform formatting with parentheses around the area code, space after closing parenthesis, and hyphen between the third and fourth digits of the local number
Ensure all contact numbers maintain clickability and proper formatting for different platforms (web, mobile, print) while preserving readability
Verify all standardized numbers match actual business contact information from Welcome call, Brand Guide, or Website content to prevent formatting errors that could break valid contact details
Maintain original Content length of character exactly same as that.
""",
    "optimize-hashtags": """Perform comprehensive review of all hashtags used in the content against the official hashtags list provided in Brand Guide and Implementation Guidelines
Identify and flag any hashtags that are not part of the approved hashtags list for removal or replacement with authorized alternatives
Verify that approved hashtags from the guidelines have been properly implemented and are being used consistently across the content
Ensure hashtag placement, spacing, and formatting follows best practices and brand standards as specified in Implementation Guidelines
Add missing strategic hashtags from the approved list that are relevant to the content topic and would enhance discoverability and reach
Validate hashtag relevance to ensure all included hashtags align with content theme, target audience, and marketing objectives
Maintain original Content length of character exactly same as that.
""",
}


formal_langauge_restrictions = """
**AVOID OVERLY FORMAL LANGUAGE** - Use conversational, natural tone instead of corporate/business language

**List of OVER FORMAL WORDS and PHRASES to be avoided in content:**
Format of the following dictionary: {{"FORMAL WORD/PHRASE to be avoided" : "Simple WORD/PHRASE that can be used instead"}}
[{{"Greetings of this nature": "I hope you're doing well","I trust this message finds you well": "I hope you're doing well","Yours sincerely": "Best regards","Yours faithfully": "Best","With the utmost respect": "Respectfully","Commence": "Start", "Cease": "Stop", "Terminate": "End", "Procure": "Get", "Ascertain": "Find out", "Facilitate": "Help", "Endeavor": "Try", "Render": "Give", "Articulate": "Say", "Refrain": "Avoid","Commencement": "Start", "Termination": "End", "Perusal": "Review", "Assistance": "Help", "Inquiry": "Question", "Documentation": "Papers", "Remuneration": "Pay", "Residence": "Home", "Venue": "Place","In the event that": "If", "At this juncture": "Now", "It is incumbent upon": "It is necessary for", "As per your request": "As you requested", "Please be advised that": "Please note that", "With regard to": "About", "With reference to": "About", "Notwithstanding the fact that": "Although", "In light of the fact that": "Because", "In the near future": "Soon", "Subsequent to": "After","Ample": "Plenty", "Sufficient": "Enough", "Optimal": "Best", "Pertinent": "Relevant", "Expedient": "Useful", "Exemplary": "Outstanding", "Verbatim": "Word for word", "Therewith": "With it", "Henceforth": "From now on","It would be greatly appreciated if": "Please", "I remain at your disposal": "Let me know if you need anything", "I am writing to apprise you of": "I'm letting you know about", "Kindly revert at your earliest convenience": "Please reply when you can", "Permit me to convey my sincerest gratitude": "Thank you", "Your cooperation in this matter is greatly appreciated": "Thanks for your help", "In the meantime, I trust you will": "For now, I hope you will","Heretofore": "Until now", "Forthwith": "Immediately", "Aforementioned": "Mentioned earlier", "Hereby": "By this", "Hereinafter": "Later in this document", "In accordance with": "Under", "Pursuant to": "According to", "The undersigned": "I", "Be that as it may": "However","Disseminate": "Share", "Elucidate": "Explain", "Augment": "Increase", "Rectify": "Fix", "Apprehend": "Understand", "Contemplate": "Think about", "Consummate": "Complete", "Accord": "Give", "Exhibit": "Show", "Surmise": "Guess", "Undertake": "Take on","Inasmuch as": "Because", "In the absence of": "Without", "For the purpose of": "To", "At this point in time": "Now", "In the final analysis": "In the end", "In due course": "Soon","Obsequious": "Overly eager to please", "Inordinate": "Excessive", "Cumbersome": "Awkward", "Prevalent": "Common", "Superfluous": "Unnecessary", "Prominent": "Well-known", "Imperative": "Necessary", "Convoluted": "Complicated","By virtue of": "Because of", "In order to": "To", "In like manner": "Similarly", "It is with great pleasure that": "I'm happy to", "As such": "Therefore", "Under separate cover": "In another email", "In accordance with your instructions": "As you instructed", "It is my considered opinion that": "I think", "Attached herewith": "Attached", "Owing to the fact that": "Because","Ab initio": "From the start", "Mutatis mutandis": "With changes", "Prima facie": "At first glance", "Abide by": "Follow", "In toto": "Completely", "Deem": "Consider", "Hereto attached": "Attached here", "Whereupon": "After which","Expound upon": "Explain", "Delve into": "Explore", "Constitutes": "Is", "Mitigate": "Lessen", "Implemented": "Used", "Enumerate": "List", "Substantiate": "Prove","Despite the fact that": "Although", "Due to the fact that": "Because", "In the majority of cases": "Usually", "On account of the fact that": "Because", "It is evident that": "Clearly", "At an earlier date": "Earlier", "During the course of": "During", "Until such time as": "Until"}}]

**LIST OF FORMAL WORDS**
[[Commence,Cease,Procure,Facilitate,Ascertain,Render,Articulate,Endeavor,Refrain,Adorn,Elucidate,Exhibit,Perusal (e.g., "for your perusal"), Remuneration, Documentation, Endeavor, Termination, Commencement, Inquiry, Residence, Venue, Circumstances, Modifications, Accommodations, Adjectives/Adverbs, Pertinent, Ample, Sufficient, Optimal, Exemplary, Expedient, Prominent, Prevalent, Superfluous, Cumbersome, Verbatim, Therewith, Henceforth,Inasmuch as, Notwithstanding, Pursuant to, At this juncture, In the final analysis, Forthwith, Herewith, Hereby, With regard to, Notwithstanding the fact that, In accordance with,Convoluted, Inordinate, Obsequious, Prodigious, Magnanimous, Serendipitous, Ostentatious, Antiquated, Transcendent, Pervasive,It is incumbent upon, Please be advised, Attached herewith, With the utmost respect, By virtue of, In light of the fact that, As per your request, Permit me to, Pursuant to your inquiry, In due course]]
"""
