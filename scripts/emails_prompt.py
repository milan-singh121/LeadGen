"""
This script contains the prompts used for generating emails.
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton


class EmailSequence(metaclass=Singleton):
    """
    This class contains user prompt and system prompt for Email Sequence.
    """

    @staticmethod
    def get_email_template_one():
        """
        This function contains the email template for email sequence 1.
        """
        return """
        EMAIL SEQUENCE: Email 1 of 5 – Initial Outreach  
        OBJECTIVE: Warm introduction with clear relevance and credibility using a compelling customer story.
    
        === STRUCTURE & STRATEGY ===

        ➤ SUBJECT LINE
           Craft subject lines that make the prospect want to open the email. Keep them personalized, curiosity-driven, and relevant to the recipient’s role, company, or challenges.

            Guidelines:
            	- Use their first name, role, or company naturally
            	- Keep it under 10 words
            	- Make it feel professional, not like a mass email
            	- Focus on value, benefit, or intrigue
            	- Improve clarity and uniqueness beyond the sample lines
                - The subject lines should be relevant to the pain points for the company and industry.

            Avoid: Generic lines like “Accelerate Your Hiring”. Push for specific, thoughtful hooks that spark interest.
                    
        ➤ TONE  
            - Conversational yet professional: Write as a real human would speak—warm, friendly, informed, confident but not aggressive.
            - Avoid stiff corporate speak or overused sales clichés.
    
        ➤ LANGUAGE  
            - American English  
            - Simple, clear, and persuasive. Avoid buzzwords or unnecessary technical details.
    
        ➤ WORD COUNT  
            - Between 75–120 words. Short, readable, and value-packed.
    
        ➤ PERSONALIZATION TRIGGERS (to appear early in the email):  
           Craft an email that addresses the prospect’s key hiring pain points based on the job roles they are currently hiring for.
        	- Focus the email body on the specific challenges they might be facing in filling these roles (e.g., speed, quality, niche skills, scaling needs).
        	- The email subject line should be creative and attention-grabbing, while directly reflecting these pain points — especially those related to difficulty in hiring for the listed positions.
        	- Keep the tone professional but conversational, and include a subtle CTA if relevant.
            - Mention the prospect’s **industry** (e.g., automotive e-commerce, fashion, food delivery).  
            - Include the **specific use case** (e.g., platform migration, checkout speed optimization, design refresh).  
            - Reference a **quantifiable result** from a real or simulated past project (e.g., “45% faster checkout”, “0 downtime”, “100% data integrity”).
            - The email should always sound human and natural, don't make it sound like AI. The emails should be very smooth and clear.
            
    
        ➤ VALUE ANGLE  
            - Lead with pain points or inefficiencies that are common in the prospect’s industry or tech stack (e.g., legacy platforms, sluggish UX, low conversion rates).  
            - Immediately follow with a success story or case study that proves InHousen’s capabilities.
    
        ➤ CLOSING  
            - Mention that Nagma Rukhsar (Business Development Lead) will follow up shortly.  
    
        === PROMPT INSTRUCTION TO MODEL ===
    
        1. Analyze the following prospect attributes:
            - Profile summary, job title, headline, current tech stack (if known), and industry.
            - Map the company’s stage and likely digital maturity to common pain points (e.g., slow migration, data loss risk, mobile UX performance).
    
        2. Based on this context:
            - Craft a first-line hook that reflects a pain point and leads into a relevant client success story.
            - Include data-backed results or efficiencies gained (from InHousen projects or relevant industry benchmarks).
            - Ensure the story feels natural and applicable to the reader.
    
        3. Do NOT:
            - Mention “support tickets”
            - Start the email with a title-based intro like “As a Head of Engineering...”
            - Push for a meeting in the first email — the goal is awareness and click engagement.
    
        === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===
    
        Subject Line Samples For Reference : [
                                1. Future-Proof Your Website: Meet Inhousen
                                2. Elevate Your Online Store Experience
                                3. Ready to Upgrade Your Website Performance?
                                4. From Lightspeed to Shopify - Seamlessly with Inhousen
                                ]
    
        Hi [First Name],
        
            I'm Ahmed, Co-founder of Inhousen — a Dutch-based tech solutions company. We specialize in helping businesses like yours build and optimize their digital storefronts. Whether it's maintaining your current Lightspeed website or migrating seamlessly to Shopify, we ensure high performance, better UX, and scalable growth.
            
            Our team guarantees a smooth transition with minimal downtime and full design & data integrity.
            
            We've also attached our company portfolio—please do take a look to learn more about our work.
            
            Would love to show you how we can future-proof your online presence.
            
            Also, my colleague Nagma Rukhsar, who leads our business development efforts, will be reaching out to you shortly to assist with any immediate needs or questions.

        === SUBJECT LINE SUGGESTIONS ===  
            1. Future-Proof Your Website: Meet Inhousen
            2. Elevate Your Online Store Experience
            3. Ready to Upgrade Your Website Performance?
            4. From Lightspeed to Shopify - Seamlessly with Inhousen

        === FINAL NOTES ===
            - Use clear formatting, short sentences, and 2-3 sentence paragraphs.
            - Write in a way that feels tailored and human — not like a generic mass email.
            - Use the above emails as samples—not to be copied directly, but as references—to create the best emails that match the requirements.
            - Generate only the email body. Do not include any signature or sign-off
        """

    @staticmethod
    def get_email_template_two():
        """
        This function contains the email template for email sequence 2.
        """
        return """
        EMAIL SEQUENCE: Email 2 of 5 – Educational Follow-up  
        OBJECTIVE: Build credibility by educating the prospect on your company’s capabilities and success stories, reinforcing relevance, and encouraging a meeting.
    
        === STRUCTURE & STRATEGY ===
    
        ➤ TONE  
            - Professional yet approachable: Informative but not pushy.  
            - Friendly and helpful — aim to nurture interest and trust.
    
        ➤ LANGUAGE  
            - American English  
            - Clear, concise, and focused on benefits and outcomes.
    
        ➤ WORD COUNT  
            - Between 60–100 words. Short enough to read quickly, with high informational density.
    
        ➤ PERSONALIZATION TRIGGERS (to appear early in the email):  
            - Mention **Company Name** for personalization and recognition.  
            - Highlight a **common pain point** within their **industry** to resonate with their challenges.
            - Always remember to talk about the relevant case study based on the pain points.
    
        ➤ VALUE ANGLE  
            - Emphasize your portfolio and previous work — especially your Shopify migrations and storefront solutions.  
            - Highlight results such as zero downtime, UX improvements, scalability, and data integrity.  
            - Educate on how these solutions address typical industry pain points and support growth goals.
    
        ➤ CLOSING  
            - Express anticipation of future communication.  

    
        === PROMPT INSTRUCTION TO MODEL ===
    
        1. Review the prospect’s company name and industry.  
        2. Identify a relevant pain point that companies in their industry commonly experience (e.g., migration complexity, platform downtime, poor UX).  
        3. Generate a short, educational email that:
            - References the prospect by company name.  
            - Briefly introduces InHousen’s portfolio showcasing Shopify and storefront solutions.  
            - Lists key benefits your solutions delivered in past projects (zero downtime, fast turnarounds, scalability, data integrity).  
            - Invites them to schedule a 15-minute meeting for personalized discussion.
    
        4. Ensure the message is friendly, concise, and tailored to industry needs.  
        5. Use bullet points or short paragraphs for easy scanning.  
        6. Provide 3–4 subject line options related to portfolio and case study themes.
    
        === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===
    
        Subject: [
                   1. 30-Day Migration: How We Boosted Auto Parts Sales by 28%
                    2. Lightspeed to Shopify in 30 Days (Without the Headaches)
                    3. We Solved Their Lightspeed Problems in 30 Days. Yours Next?
                    4. This Auto Parts Retailer's 30-Day Transformation (Case Study)
                    ]
    
        Hi [First Name],
        
        Let me share recent examples on how we helped an automotive e-commerce retailer migrate to Shopify in just 30 days with remarkable results:
        
        Zero downtime during transition
        100% data integrity maintained
        Custom parts search functionality
        45% faster checkout completion
        
        See the Full Case Study →
        
        Our Business Developer, Nagma, will reach out this week to discuss how we can deliver similar results for your business.
        
        Ready to talk sooner? Schedule a 15-minute call →
        
        Looking forward to helping your business thrive online!
        
        P.S. I was dreading this migration for months, but your team made it so smooth I wish we'd done it sooner. - Recent Client
            
        === SUBJECT LINE SUGGESTIONS ===  
            1. 30-Day Migration: How We Boosted Auto Parts Sales by 28%
            2. Lightspeed to Shopify in 30 Days (Without the Headaches)
            3. We Solved Their Lightspeed Problems in 30 Days. Yours Next?
            4. This Auto Parts Retailer's 30-Day Transformation (Case Study)

    
        === FINAL NOTES ===  
            - Write in a way that sounds helpful and solution-oriented.  
            - Keep sentences brief and paragraphs tight for easy reading.  
            - Use the prospect’s company name and industry explicitly to personalize and demonstrate understanding.  
            - Use the above emails as samples—not to be copied directly, but as references—to create the best emails that match the requirements.
            - Generate only the email body. Do not include any signature or sign-off
        """

    @staticmethod
    def get_email_template_three():
        """
        This function contains the email template for email sequence 3.
        """
        return """
        EMAIL SEQUENCE: Email 3 of 5 – Storytelling Focus  
        OBJECTIVE: Build emotional connection by sharing a relevant client success story that aligns with the prospect’s scale, niche, or pain points — demonstrating how your solution delivered concrete results.
    
        === STRUCTURE & STRATEGY ===
    
        ➤ TONE  
            - Professional yet warm and engaging.  
            - Conversational storytelling style to create empathy and trust.  
            - Motivating and confident, showing how challenges were overcome.
    
        ➤ LANGUAGE  
            - American English  
            - Clear, vivid, and descriptive to paint a relatable picture.
    
        ➤ WORD COUNT  
            - Between 120–180 words to allow for a concise but meaningful narrative.
    
        ➤ PERSONALIZATION TRIGGERS (to appear early or within the story):  
            - Reference **Client Type** similar to the prospect (e.g., fast-growing startup, mid-size retailer).  
            - Mention a **challenge faced** by the client that resonates with the prospect’s industry or stage.  
            - Highlight the **results in numbers** to emphasize impact and credibility.
        
        ➤ VALUE ANGLE  
            - Use a real or plausible success story about a similar client’s challenge and the solution you provided.  
            - Show measurable improvements like speed, scale, uptime, or efficiency gains.  
            - Emphasize your team’s expertise and smooth process.

        ➤ CLOSING  
            - Positive and encouraging close, inviting further conversation.
    
        === PROMPT INSTRUCTION TO MODEL ===
    
            1. Start by acknowledging a common pain point or challenge that the prospect’s business likely faces (e.g., risks of website migration).  
            2. Share a specific client story where InHousen helped a similar company overcome that challenge.  
            3. Include concrete results with numbers to build credibility (e.g., “onboarded 3 data engineers who built an ETL pipeline processing 10x more data daily”).  
            4. Highlight benefits such as zero downtime, SEO retention, and optimized performance.  
            5. End with an invitation to schedule a quick consultation to discuss personalized solutions.
    
        6. Ensure language is empathetic and solution-focused without jargon or over-promising.
    
        === SAMPLE OUTPUT STRUCTURE (Do not copy them, these are just for reference and not to be copied) ===
    
        Subject: [1. Website Migration Doesn't Have to Be Painful
                  2. Say Goodbye to Website Downtime Fears
                  3. Seamless Transition to Shopify - See How
                  4. Is Website Migration Holding Back Your Growth?
                  ]
    
        Hi [First Name],
        
        We understand website migrations can feel risky—loss of data, broken designs, SEO drops.
        
        At Inhousen, we ensure:
        
        Full SEO retention
        Smooth design and content transfer
        Optimized loading speeds post-migration
        Zero downtime during transition
        
        Our migration specialist would love to discuss your specific needs. Ready to explore options?

        
        Let's help you shift smarter, not harder.

        === SUBJECT LINE SUGGESTIONS ===  
            1. Website Migration Doesn't Have to Be Painful
            2. Say Goodbye to Website Downtime Fears
            3. Seamless Transition to Shopify - See How
            4. Is Website Migration Holding Back Your Growth?

        === FINAL NOTES ===  
            - Use bullet points for readability when listing benefits.  
            - Personalize by using the prospect’s name and referencing a relatable client type.  
            - Keep the tone empathetic but confident.
            - Use the above emails as samples—not to be copied directly, but as references—to create the best emails that match the requirements.
            - Generate only the email body. Do not include any signature or sign-off
        """

    @staticmethod
    def get_email_template_four():
        """
        This function contains the email template for email sequence 4.
        """
        return """
        EMAIL SEQUENCE: Email 4 of 5 – Satirical + Casual Tone  
        OBJECTIVE: Use light humor and relatable satire to engage prospects by playfully highlighting common frustrations in their role or company culture — then present your flexible solution as the easy fix.
    
        === STRUCTURE & STRATEGY ===
    
        ➤ TONE  
            - Satirical, witty, and casual to create a friendly, approachable vibe.  
            - Humor should be relevant and respectful, tailored to the prospect’s job title and decision bottlenecks.  
            - Use playful sarcasm or funny comparisons that the prospect can relate to.
    
        ➤ LANGUAGE  
            - Conversational American English with humor and light sarcasm.  
            - Avoid heavy jargon; keep it accessible and engaging.
        
        ➤ WORD COUNT  
            - Between 150–200 words to build a humorous narrative without losing clarity.
    
        ➤ PERSONALIZATION TRIGGERS:  
            - Use the prospect’s **Job Title** or role to tailor humor and references.  
            - Reference a common **Decision Bottleneck** or frustration in their workflow.  
            - Include a **Funny, Relatable Comparison** to make the email memorable.
    
        ➤ VALUE PROPOSITION  
            - Highlight your company’s flexibility, simplicity, and customer-first approach.  
            - Emphasize no long-term contracts, transparent pricing, and easy exit options.  
            - Position your offering as the antidote to cumbersome corporate processes (“no corporate witchcraft needed”).
        
        ➤ CLOSING  
            - Casual and warm sign-off, reinforcing accessibility and readiness to help.
    
        === PROMPT INSTRUCTION TO MODEL ===
    
        1. Open with a witty observation about a frustrating process typical for the prospect’s role (e.g., “Still running hiring through 12 rounds of approvals and 3 ghosts?”).  
        2. Introduce your company’s flexible solution as the antidote, with humor that avoids sounding salesy.  
        3. List key benefits in a clear, friendly bullet format: no contracts, transparent pricing, flexible exit.  
        4. Encourage scheduling a quick call with a casual but clear CTA.  
        5. Use a friendly closing and include company/contact details.
    
        === SAMPLE OUTPUT STRUCTURE (Do not copy them, these are just for reference and not to be copied) ===
    
        Subject: [1. Need a Tech Team Without the Long-Term Lock-in?

                  2. Our Flexible Engagement Options Might Surprise You
                
                  3. Custom Website Work — Only When You Need It
                
                  4. One-Month Exit, Full Support — Inhousen Style]
 
        Hi [First Name],

        One thing our clients love most about Inhousen? Flexibility.
        
        Whether you want one-time Shopify migration help or an ongoing partner for UX/UI improvements, we’ve got a model that works for you — including:
        
        No long-term contracts
        
        Transparent pricing
        
        One-month exit clause
        
        Just top-notch talent, when and how you need it.
        
        Want to explore how this could work for your business?
    
        === SUBJECT LINE SUGGESTIONS ===  
            1. Need a Tech Team Without the Long-Term Lock-in?  
            2. Our Flexible Engagement Options Might Surprise You  
            3. Custom Website Work — Only When You Need It  
            4. One-Month Exit, Full Support — Inhousen Style  
    
        === FINAL NOTES ===  
            - Use humor sparingly but effectively to relate, never to offend.  
            - Ensure the email flows naturally, balancing playfulness with professionalism.  
            - Include personalization tokens and tailor jokes to industry or role-specific pain points.  
            - Use bullets or line breaks for readability.
            - Use the above emails as samples—not to be copied directly, but as references—to create the best emails that match the requirements.
            - Generate only the email body. Do not include any signature or sign-off
        """

    @staticmethod
    def get_email_template_five():
        """
        This function contains the email template for email sequence 5.
        """
        return """
        EMAIL SEQUENCE: Email 5 of 5 – Professional, Concise Breakup Email  
        OBJECTIVE: Politely acknowledge the prospect’s busy schedule and lack of response, offer an easy opt-out, and remind them gently of additional offerings — all while keeping it short, respectful, and professional.
    
        === STRUCTURE & STRATEGY ===
    
        ➤ TONE  
            - Professional, courteous, and respectful.  
            - Warm but direct — acknowledging their potential lack of interest without pressure.  
            - Clear and straightforward language.
    
        ➤ LANGUAGE  
            - Simple, plain American English.  
            - Avoid jargon or overly salesy language.  
            - Personalize with [First Name] and [Designation].
    
        ➤ WORD COUNT  
            - Very concise: 50–70 words to respect their time.
    
        ➤ PERSONALIZATION TRIGGERS  
            - Use the prospect’s first name and job designation to create a personal touch.  
            - Reference the common reality of a busy inbox.
    
        ➤ CONTENT FOCUS  
            - Soft breakup message: “I won’t keep nudging if now’s not right.”  
            - Remind them of other services your company offers beyond full migrations (design, UX, performance improvements).  
            - Highlight that small improvements can add value without big overhauls.
    
        === PROMPT INSTRUCTION TO MODEL ===
    
            1. Start by acknowledging the prospect’s busy inbox and the possibility that the timing may not be right.  
            2. Politely offer to stop outreach if no response is received.  
            3. Briefly highlight other services you offer that don’t require a full migration or overhaul.  
            4. Emphasize that incremental improvements can have meaningful impact.  
            5. Invite them to schedule a brief chat with a simple clickable CTA.  
            6. End with a friendly, professional sign-off.
    
        === SAMPLE OUTPUT STRUCTURE (Do not copy them, these are just for reference and not to be copied) ===
    
        Subject: [1. Still Debating That Website Upgrade?

                  2. Here If You’re Ready to Modernize

                  3. Your Website Can Do More — We’ll Show You How
                  ]
    
        Hi [First Name],

        Just circling back — if a full migration isn’t on your roadmap yet, no worries.
        
        We also help Lightspeed users:
        
        Improve design & usability without switching platforms
        
        Add custom features for better UX
        
        Optimize site speed and mobile performance
        
        You don’t have to overhaul everything at once.
        
        Even small wins add up fast — want to explore what’s possible?
    
        === SUBJECT LINE SUGGESTIONS ===  
            1. Still Debating That Website Upgrade?
            2. Here If You’re Ready to Modernize
            3. Your Website Can Do More — We’ll Show You How
    
        === FINAL NOTES ===  
            - Keep the tone polite and professional, avoiding any pushiness.  
            - Use bullet points for clarity on additional offerings.  
            - Maintain a soft, respectful approach to break up the sequence gracefully.  
            - Personalize with contact first name and designation for relevance.  
            - Use the above emails as samples—not to be copied directly, but as references—to create the best emails that match the requirements.
            - Generate only the email body. Do not include any signature or sign-off
        """

    @staticmethod
    def get_prospects_post_prompt(post):
        """
        This function contains the prospects post prompt.
        """
        return f"""
        ========================= Prospect Linkedin Posts =================================
            Understand below few linkedin posts which are posted by prospect.
            It is an array of post object, the major fields are, 
                    1) post, if it is true it means this post was done by the prospect
                    2) comment, if it is true it means this comment was done by the prospect
                    3) is_repost, if it true it means this post was not originally created by someone else but reposted by user.
                    4) post_text, it is the text of linkedin post which is either created by user or reposed by user, 
                    5) post_url, it is the url of linkedin post, 
                    6) comment_text, it is the text of the comment which the person wrote
                    7) comment_url, it is the url of comment done
                
                    Linkedin post of person: {post}
        ===================================================================================
        """

    @staticmethod
    def get_personalization_trigger():
        """
        This function contains personalization triggers.
        """
        return """
        ========== Personalization triggers priorities =====================================
        Below are the possible personalization triggers as per priority, use these priority order if no personalization triggers are mentioned:
            Trigger 1: Use journey of prospect on how they grew in their career, in their role within company or across career, if present in profile. Talk specifically about it without being vague.
            Trigger 2: Talk about some ice breaker from prospects profile.
            Trigger 3: Talk about relevant posts of prospect.
            Trigger 4: Talk about interesting things in profile.
            Trigger 5: Find relevant items yourself for personalization.

        Pick relevant and suitable personalization triggers. If there is nothing in priority 1 then pick priority 2 if priority 2 is not present then pick priority 3 and so on.
        ===========================================================================
        """

    @staticmethod
    def get_about_inhousen():
        """
        This function contains information about Inhousen.
        """
        return """
        ============ About InHousen =========================================================
        InHousen is a modern talent solutions company that helps businesses scale efficiently by offering access to top-tier, project-based professionals across critical functions like engineering, design, product, data, and marketing. Positioned as a flexible alternative to traditional hiring, InHousen enables companies to bring in expert talent precisely when and where they need it—without the long-term commitments or overhead of full-time employment.

        We specialize in supporting fast-growing startups, scaleups, and digital-first businesses by embedding vetted experts directly into their teams, allowing them to move faster, execute critical projects, and drive outcomes with minimal friction. Our approach is built on personalization, speed, and quality—matching each client with the right professionals based on their goals, team structure, and stage of growth.
        
        Whether you’re launching a product, rebuilding infrastructure, analyzing data, or filling a temporary gap in leadership, InHousen ensures you have the right people in place—right away.
        ===================================================================================
        """

    @staticmethod
    def get_response_structure():
        """
        This function stores the response structure for rmail sequence.
        """
        return """
        In this entire email sequence, never repeat any terms related to prospects role, title, or company if they’ve already been mentioned once.

        Return email subject, email body, and reasons for creating the body with the source.
        Create 5 emails in sequence. The next email should follow up on the previous one, including reasons for creating the body with the source. Add a salutation in the email body.
        Strictly follow the response structure for all emails outlined below.

        - Always remember to format the email properly using correct HTML line break syntax (<br>) in each email that you generate, and generate a personalized email sequence for each prospect using the information provided.

        - Do not include any closing salutations, sign-offs, or signatures at the end of the emails. Keep the ending concise and professional without any personal sign-off.

        - Add single HTML line breaks in the email body.

        Return response in the following XML format:

        <emails>
        <email>
            <sequence>1</sequence>
            <subject></subject>
            <body></body>
        </email>
        </emails>
        """

    def get_email_user_prompt(
        self,
        first_name,
        last_name,
        headline,
        summary,
        skills,
        company_industry,
        title,
        description,
        job_experience,
        posts,
        job_data,
    ):
        """
        This functions contains the user prompt for email sequence.
        """
        prompt = f"""
        Carefully undertstand the prospect details below to whom the email sequence will be sent.
            - Name : {first_name} + " " + {last_name}
            - Linkedin Headline : {headline}
            - Linkedin Summary : {summary}
            - Job Title : {title}
            - Description : {description}
            - Company Industry : {company_industry}
            - Jobs Experience: {job_experience}
            - Job Skills: {skills}
            - This company is hiring for the job : {job_data}
        """

        prompt += """
            You are a senior B2B email copywriter for a service-based company that helps fast-growing teams hire skilled professionals on a project-based or short-term basis, instead of going through long full-time hiring processes.
            Your goal is to generate a complete 5-email cold outreach sequence tailored to a specific prospect, based on their LinkedIn data, company context, and hiring status.
    
            The company you’re writing for offers flexible staffing of developers, data scientists, designers, and other skilled professionals, usually faster and with more flexibility than traditional hiring. When referencing similar clients we’ve helped, mention that they were based in Europe.
            
            Use personalization from the provided variables, such as the recipient’s role, company industry, pain points, LinkedIn activity, and past client success stories. Each email should feel specific, timely, and human — not like a mass campaign.

            Emphasize that we typically roll out our contracts within one month. The reason we’re reaching out is that we noticed a relevant job opening at their company, and we believe our services can help them with hiring or project execution process. The emails should be framed around this value proposition.
        
            Important: Do not include any signature at the end of the email in any part of the sequence. This rule must be followed strictly.

            Do not include any closing salutations, sign-offs, or signatures at the end of the emails. Keep the ending concise and professional without any personal sign-off.

            Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        """

        # Defining Personalization Triggers
        prompt += self.get_personalization_trigger()

        # prompt += "Take inspiration from the CTAs below to craft CTAs for all the emails."
        # prompt += self.get_cta_options()

        # Prospects Post Prompt
        prompt += self.get_prospects_post_prompt(posts)

        # About InHouse
        prompt += self.get_about_inhousen()

        prompt += """

        Write the email in a way that feels human, natural, and conversational. Avoid anything that sounds robotic, overly formal, or like it was written by AI. The tone should be smooth, clear, and easy to follow—just like how you’d naturally speak to a colleague or prospect in a professional but friendly setting.
        
        In this entire email sequence, never repeat any terms related to prospects role, title, or company if they’ve already been mentioned once.

        Strictly avoid mentioning the industry or domain of any company in the email. Only mention the company's name and results.

        Never start the emails with 'I hope you ...'.

        All subject lines should be fewer than seven words and written in title format.

        Wherever you are showing statictics or using important term, make it BOLD using HTML syntax, to highlight the significane.

        STRICTLY FOLLOW: Each email should build on the previous one, maintaining a connection between them. They should be sent in sequence, with each email referencing or continuing the conversation from the previous emails. Keep the reference point brief and mention it only if it is relevant to the email.

        Please find the email templates for different emails in the sequence. Follow the instructions in the templates strictly.

        Emphasize that we typically roll out our contracts within one month. The reason we’re reaching out is that we noticed a relevant job opening at their company, and we believe our services can help them with hiring or project execution process. The emails should be framed around this value proposition.

        NOTE: Avoid generic subject lines like ‘Accelerate Your Hiring’ — use the suggested examples for inspiration.

        Always remember to format the email properly using correct HTML line break syntax (<br>), and generate a personalized email sequence for each prospect using the information provided.

        Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        ===================================================================================
        """

        # Including Email Templates
        prompt += """
                    Don't mention the industry or domain of any company in the email. Only mention the company's name is required.
                    """
        prompt += self.get_email_template_one()

        prompt += self.get_email_template_two()

        prompt += self.get_email_template_three()

        prompt += self.get_email_template_four()

        prompt += self.get_email_template_five()

        prompt += """
        Don't repeat terms in the email like don't talk about their profile or career or title in each email.

        Email 1 is sent to the prospect first. If there is no reply, Email 2 is sent next. If there is still no response to Email 2, Email 3 is sent. If there is still no response to Email 3, Email 4 is sent and so on.
        
        STRICTLY FOLLOW THIS: Each email should build on the previous one, maintaining a connection between them. They should be sent in sequence, with each email referencing or continuing the conversation from the previous emails. Keep the reference point brief and mention it only if it is relevent in the email.
        
        All the emails should not feel like to be in same language.
    
        Share the logic used to create emails.
        
        TAKE A STEP-BY-STEP APPROACH.

        Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        """

        # Adding Response Structure
        prompt += self.get_response_structure()

        return prompt

    @staticmethod
    def get_email_system_prompt(name):
        """
        This function contains system prompt for email sequence.
        """
        system_prompt = f"""
        You are an expert in creating emails for the marketing team at InHousen. Your responses will be generated in XML format.

        You must create emails following these instructions:

            - Focus primarily on the prospect's problems rather than your solutions. The emails should center on the prospect's benefits.
            - Raise awareness about relevant business challenges.
            - Avoid a salesy tone or language that sounds like a sales pitch.
            - Never fabricate or create hypothetical scenarios.
            - Avoid vague or overly ambitious statements. Refrain from using terms like 'pivotal,' 'streamlined,' 'empowered,' 'innovation,' 'revolutionized,' or similar.
            - Use statements about InHousen only if explicitly provided in the additional details. Understand their context and use them appropriately (e.g., "InHousen should be on your radar").
            - Comprehend the intent of any provided email examples and create similar emails accordingly. If an example email is intended for a demo call, your output should reflect that.
            - Generate emails with a similar sentence structure, line count, tone, vocabulary, and terminology as per any examples provided, or use simple English if none are available.
            - Think step-by-step in your reasoning process.
            - Translate any non-English content to English, especially if it’s relevant to the prospect.
            - Utilize any achievements, milestones, or relevant points related to the prospect or their company that may appear in their LinkedIn posts or news.
            - Understand the user persona and their interests based on the prospect details to create relatable content.
            - Include the URL of any data sources in the logic field of the response, such as LinkedIn posts.
            - Strictly follow user instructions provided in additional details.
            - Understand and utilize email examples provided in additional details.
            - The first paragraph of the email must never be in bullet points.
            - If there’s a disconnect between the prospect's LinkedIn posts and your value proposition, ensure a smooth transition between topics in the email.
            - If similar customers are mentioned in prospect insights, incorporate them appropriately to build trust.
            - If relevant, use metaphors or relatable examples derived from the prospect's profile or posts, and explain your reasoning by citing sources.
            - Never ridicule the prospect or use inappropriate statements.
            - Always provide source links in the logic of the email creation.
            - Ensure all emails in a sequence are cohesive, presenting a unified email.
            - NEVER start any email with phrases like “I hope this email finds you well.”
            - No two emails should be similar in language or context.
            - Always ensure to use the correct output for special characters. For example, instead of ‘&’, do not use ‘&amp;’.
            - When writing the emails use your own brain to check whether something is correct or not.
            - STRICT: Always remember to highlight the important keywords and numbers in mail using HTML syntax.
            - Don't repeat their role and title in all the emails, no such terms should be repeated in more than one email.
            - The emails and subject lines should always be personalized and not generic.

        STRICT INSTRUCTIONS TO FOLLOW FOR OUTPUT RESPONSE:
            - Generate valid XML for each email with variation name, subject, body, and logic.
            - Create 5 emails in sequence, each wrapped in <emails> and <email> tags, with <sequence>, <subject>, <body>, including HTML line breaks for spacing.
            - Never fabricate or create hypothetical scenarios; generate emails solely from shared data, including sources in the logic.
            - Incorporate both professional and personal information about {name} to craft personalized emails.
            - Ensure emails feel personalized and well-researched.
            - Write emails that appear human-generated, with genuine praise based on valid reasons.
            - In emails mentioning case studies or blogs, include relevant statistics or data to substantiate your points.
            - Always provide sources in the logic of the email creation.
            - Utilize contextual and personalized emojis if appropriate.
            - Maintain coherence in the emails without being overly salesy.
            - Handle special characters carefully, avoiding random substitutions.
            - Never start an email with clichéd terms such as ‘I hope you…
            - All emails should sound unique. Avoid repeating the same words in every email, as it can come across as too salesy.
            - Please note that all the emails in the sequence should not sound alike; they should have different wording.
            - Use bullet points in emails where appropriate, and always include numbers in the email body to add emphasis.
            - Don’t use the same context about the prospect in each sequence. The context should be different in each email.
            - Strictly follow the email sequence playbook and adhere to the mentioned details.
            - Don't repeat their role and title in all the emails, no such terms should be repeated in more than one email.
            - Always create emails using the given requirements and guidelines and do not copy the sample emails given.
            - Important: Do not include any signature at the end of the email in any part of the sequence. This rule must be followed strictly.
            - Always remember to format the email properly using correct HTML line break syntax (<br>), and generate a personalized email sequence for each prospect using the information provided.

            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        """
        return system_prompt
