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
    def energy_clients_data():
        return """
                Client Name: PowerHive
                
                Industry: Energy Trading
                
                Services: UX/UI Design, Product Development, Deployment, QA
                
                Skillset Utilized: UI/UX designer, Front-end Engineer, Back-end Engineer, Product Owner, QA
                
                Project Brief: Our team developed an advanced energy trading platform for PowerHive (a sustainable energy start-up). The platform allows users to access the best energy prices while promoting sustainability and enables flexible purchasing, smart control, and transparent billing.
                
                Project Scope and Objectives: 
                    The platform was designed to streamline energy trading with:
                        1. A trading module for seamless transactions between buyers and sellers.
                        2. Integration with energy exchange systems for real-time market participation.
                        3. A payment engine for automated calculations and money transfers via a third-party account-holding company.
                    This solution ensures businesses and consumers can trade energy securely, efficiently, and cost-effectively.
                
                Technology and Stack Architecture:
                    - Built with a microservices architecture, the platform enables scalability and flexibility:
                
                Frontend: React.js for an intuitive user interface.
                Backend: .NET Core for high-performance APIs.
                Cloud Deployment: Microsoft Azure for reliability and security.
                Database & Storage: Azure SQL Database and Blob Storage for efficient data management.
                
                Project Delivery
                    Team Composition: We assembled a skilled team
                        1. 1 Product Owner for requirement management and stakeholder coordination.
                        2. 1 UI/UX Designer for an optimized user experience.
                        3. 4 Developers(backend and frontend) for system implementation.
                Execution: To simplify onboarding, we built a client portal for user registration, account setup, and trading configuration, ensuring compliance and ease of use. A key milestone was integrating with the energy exchange system, enabling real-time trading through:
                    1. API connections to live market data.
                    2. Forecasting & Trading: Users can leverage forecasting engines to anticipate energy usage and place trades for upcoming days.
                    3. We also developed a payment engine for seamless financial transactions, including:
                    4. Accurate cost calculations based on market prices.
                    5. Secure transactions via third-party account-holding companies.
                    6. Automated billing and reconciliation.
                
                Over 9 months, we developed and deployed the platform, working closely with the client to refine features and optimize performance. After delivery, we facilitated a smooth transition to the internal team, ensuring proper documentation and support.
                
                Key Outcomes & Impact:
                    1. Automated trading for market access and efficiency.
                    2. Optimized cost savings through flexible purchasing.
                    3. Secure and accurate financial settlements
                    4. Scalable and future-ready cloud architecture.
                """

    @staticmethod
    def fashion_clients_data():
        return """
                Client Name: Major Dutch Retail Showroom
                
                Industry: Fashion, Clothing
                
                Services: Data Science & Analytics
                
                Skillsets Utilized: Data Pipeline, Python, ETL, MongoDB, Zoho Analytics, Custom AI Model development
                
                Project Brief: A leading Dutch retail showroom in the Netherlands needed a data-driven solution to optimize inventory and predict future sales. Seasonal fluctuations and inaccurate forecasting led to high inventory costs and inefficiencies. In a business with 8% net margins, excess inventory was eating into 5% of operating income. InHousen was engaged to build an Machine learning -powered descriptive and predictive analytics platform to enhance forecasting and inventory planning.
                
                Solution Overview: InHousen developed an open-source model driven machine learning platform that:
                    1. Analyzed historical sales data to detect demand trends. Weather patterns & local demographics were also embedded in the model to improve accuracy.
                    2. Predicted future sales volumes, improving purchasing decisions.
                    3. Optimized inventory planning, preventing overstocking and shortages.
                    4. Provided discounting scenario analysis, to determine optimal discounting with balance between increased sales and maximum margins.
                
                Technology Stack:
                    InHouse Finance was developed with a modern and scalable tech stack:
                        1. Backend & ML Models: Python (Scikit-learn, TensorFlow, XGBoost)
                        2. Database: Hadoop
                        3. Frontend Dashboard: PowerBI
                        4. Cloud Infrastructure: AWS
                        5. API Integration: Microsoft Dynamics ERP
                
                Project Delivery
                    Team Composition: A 6-month Agile approach with a team of
                        1. 1 Product Owner, Ensuring business alignment and feature prioritization.
                        2. 1 Data Scientist, Building AI Models, Performing Model diagnosis & corrections, Building Math model to enhance AI Model capabilities.
                        3. 1 Data Engineer, Building ETL pipelines & preparing data schema and model for the incoming data
                
                Execution: We built a custom AI and mathematical forecasting model for a men's fashion store in the Netherlands, leveraging both XGBoost for short-term sales trends and LSTM for long-term seasonal forecasting.
                    1. Phase 1 (2 months): Infrastructure set-up, data collection & trend analysis.
                    2. Phase 2: Model selection & training for demand forecasting.
                    3. Phase 3: Dashboard development for real-time insights.
                    4. Phase 4: Integration with the client’s ERP system.
                
                Maintenance & Impact:
                    1. Accurate demand forecasting, reducing waste & stockouts. An accuracy of 95% for the upcoming 1 month and an accuracy of 90% for 1 month to 1 year was achieved.
                    2. Optimized inventory management, cutting holding costs (by up to 8%).
                    3. Higher profitability through better sales planning (margins improved by 4%).
                    4. Scalable solution for future growth.
                
                Post-launch, InHousen ensured 99.9% uptime, periodic model retraining, and added automated reporting.
                """

    @staticmethod
    def fintech_clients_data():
        return """
                ------------------------------------------------------------------------------------- Client 1 ---------------------------------------------------------------------------------------------------------------
                
                Client Name: Moodus
                
                Industry: Fintech/Financial Service
                
                Services: Product development & Maintenance
                
                Skillsets Utilized: UI/UX designer, Front-end Engineer, Back-end Engineer, Product Owner, QA
                
                Duration: 4 months + ongoing maintenance
                
                Project brief: Moodus, a fintech leader in point-of-sale (PoS) solutions for non-governmental organizations (NGOs) across Europe, sought to improve the configuration and transaction data management of its PoS devices. Operating in multiple countries with over 700+ PoS devices deployed, Moodus needed an efficient, centralized way for NGOs to manage devices, access data, and scale services across diverse locations.
                
                Project Scope and Objectives: 
                    Moodus required a centralized, user-friendly platform that enables:
                        1. Custom App Deployment: NGOs can upload and manage their own PoS apps.
                        2. Secure Payment Processing: Integration with Payment Service Provider (PSP) ensuring encrypted, real-time transactions.
                        3. Scalable Dashboard Management: Centralized tracking and management of PoS devices and transactions.
                        4. Multi-Provider Integration: Seamless connection with various payment service providers across multiple countries
                
                Technology Stack and Architecture:
                    To ensure scalability, security, and seamless operations, we implemented:
                        1. Frontend: React.js for a dynamic, intuitive dashboard experience.
                        2. Backend: Python Django for high-performance API management.
                        3. Database: MongoDB for flexible, scalable data storage.
                        4. Architecture: Microservices-based design for modularity and efficiency.
                        5. Cloud Infrastructure: AWS for real-time data processing, hosting, and storage.
                        6. Integration Protocol: ECR protocol for secure communication between PoS devices and payment service providers.
                
                Project Delivery:
                    Team Composition: To execute the project effectively, InHousen provided
                        1. 1 Product Owner to manage requirements and ensure smooth delivery.
                        2. 1 UI/UX Designer to craft an intuitive interface for Moodus and its clients.
                        3. 4 Developers specializing in Mobile app development, PoS integration, backend services, and microservices architecture.
                
                Execution: Within 6 months, InHousen designed and deployed the Moodus Global Dashboard, with ongoing maintenance and enhancements. The execution process included
                    1. Custom App Management NGOs can configure custom PoS app settings effortlessly
                    2. Integration with Buckaroo & Payment Providers: Transactions are securely processed with multi-country support.
                    3. Scalable PoS Device & Transaction Management: Clients can track payments by device, location, or service provider in real time.
                    4. Dynamic Web Portal for Updates: Clients can modify payment settings without redeploying apps.
                
                An Agile iterative development model was followed, significantly reducing time-to-market and enabling the delivery of immediate value, ensuring the business could quickly adapt and benefit from the evolving solution."
                
                ------------------------------------------------------------------------------------- Client 2 ---------------------------------------------------------------------------------------------------------------
        
                Client Name: Moodus Connect
                
                Industry: Fintech / Financial Service
                
                Services: Mosqapp
                
                Duration: 1 year
                
                Skillsets Utilized: NodeJs, MongoDB, Redis, CI/CD, Docker
                
                Project Brief: Moodus Connect, a new startup focused on enhancing community management for non-governmental organizations (NGOs), needed a solution to streamline donation collection and improve communication & transparency with registered members. InHousen was engaged to develop an MVP (Minimum Viable Product) that could quickly launch, gather feedback, and scale over time.
                
                Project Scope and Objectives: Moodus Connect aimed to build a seamless, user-friendly system for NGOs to:
                    1. Manage users: NGO admins can oversee user registrations and donations.
                    2. Collect donations: Offering a flexible donation system, including autopay options for members.
                    3. Enhance communication: Admins can send news updates to members directly through the platform.
                
                The solution was designed to meet the unique needs of NGOs and their communities, enabling easy management, secure donation processing, and constant engagement. The platform was also designed to support multi-language options, increasing accessibility across regions.
                
                Technology Stack and Architecture
                    The platform was built using a scalable tech stack:
                        1. Frontend: React.js for the admin web portal, providing an intuitive UI.
                        2. Backend: Node.js for backend development.
                        3. Database: MongoDB for handling large-scale data.
                        4. Mobile App: React Native for cross-platform support (iOS & Android).
                        5. Cloud Infrastructure: AWS for hosting and scalability.
                        6. Payment Integration: Smartpay solutions and payment service providers from large banks.
                
                Project Delivery
                    Team Composition: We assembled a skilled team:
                        1. 1 Product Owner to ensure alignment with Moodus Connect’s goals.
                        2. 1 UI/UX Designer to create a user-friendly interface.
                        3. 4 Developers specializing in backend services, mobile app development, and cloud architecture.
                
                Execution: InHousen followed an Agile approach, delivering the MVP in phases to allow continuous feedback and faster iteration. The implementation timeline was 9 months, split into the following phases:
                    Phase 1: Web and Mobile App Development (2 months) – The web portal for admin users and mobile app for members to make donations.
                    Phase 2: Autopay & Multi-Language Support (3 months) – Autopay and multi-language support introduced.
                    Phase 3: Notifications & Multi-Channel Support (2 months) – Push notifications and multi-channel support integrated.
                    Phase 4: Multi-Country Launch (2 months) – Launched in 6 countries with language support and integrated payment services.
                
                Maintenance & Ongoing Support: Post-launch, Moodus Connect engaged InHousen for ongoing maintenance, ensuring 99.95% uptime, handling scalability, and adding new features like automated invoicing.
                
                Key Outcomes & Impact:
                    1. Streamlined donation collection: Simplified the donation process for members and NGOs.
                    2. Improved communication: Real-time updates through notifications and news.
                    3. Increased transparency: Enhanced transparency in donation tracking.
                    4. Global reach: Multi-language support enabled Moodus Connect to launch in 6 countries.
                    5. Scalable solution: Built on AWS for growth and feature expansion.        
                """

    @staticmethod
    def crm_clients_data():
        return """
                Client Name: InHousen Finance
                
                Industry: CRM
                
                Services: Closure - Task Management
                
                Duration: 2 months
                
                Skillsets Utilized: NodeJs, MongoDB, Redis, ReactJs
                
                Project Brief: InHouse Finance is a modern financial close solution designed to streamline monthly, quarterly, and yearly financial closes with speed and transparency. By automating manual processes and integrating AI-driven applications, InHouse Finance helps finance teams reduce errors, improve efficiency, and accelerate reporting cycles. One of its key features is an AI-powered invoice processing system, which extracts invoices from emails and seamlessly uploads them into accounting software like Exact. Built using microservices architecture with a Node.js backend and React frontend, InHouse Finance offers a scalable and flexible platform for businesses of all sizes.
                
                Project Scope and Objectives: InHouse Finance was developed to tackle key financial close challenges by offering:
                    1. Faster close cycles: Automating reconciliation and reporting for quicker month-end and year-end closes.
                    2. AI-powered invoice processing: Extracting invoices from emails and integrating with accounting software.
                    3. Seamless integration: Supporting platforms like Exact for automated financial data synchronization.
                    4. Scalability and security:  Ensuring compliance and efficiency for businesses of all sizes.
                
                InHouse Finance minimizes manual efforts for finance teams, allowing them to focus on strategic decision-making rather than administrative tasks.
                
                Technology Stack and Architecture: InHouse Finance was developed with a modern and scalable tech stack:
                    1. Frontend: React.js for a smooth and responsive user experience.
                    2. Backend: Node.js for high-performance server-side operations.
                    3. Database: Designed for efficiency and scalability with microservices architecture.
                    4. Cloud Infrastructure: Secure and scalable cloud deployment.
                    5. AI-Powered Automation: Machine learning models for invoice extraction and categorization.
                    6. Accounting Integration: Seamless connectivity with Exact and other financial platforms.
                
                Project Delivery:
                    Team Composition: The project was successfully delivered by a focused team:
                        1. 1 Product Owner, Ensuring business alignment and feature prioritization.
                        2. 1 UI/UX Designer, Creating an intuitive and user-friendly interface.
                        3. 3 Developers, Specializing in backend, frontend, and AI-powered automation.
                
                Execution:
                    InHouse Finance was developed using an Agile methodology, allowing for rapid iteration and continuous improvement. The implementation timeline was 4 months, divided into structured phases:
                        Phase 1: Core Platform Development (1 month) - Built financial close workflows, dashboards, and core functionalities.
                        Phase 2: AI-Powered Invoice Processing (1 month) – Developed and integrated AI models for email-based invoice extraction.
                        Phase 3: Accounting Software Integration (1 month) – Connected InHouse Finance with Exact and other accounting tools.
                        Phase 4: Optimization & Security Enhancements (1 month) – Improved performance, scalability, and compliance measures.
                
                Maintenance & Ongoing Support:
                    After delivery, InHouse Finance continued to evolve with ongoing maintenance and feature updates, ensuring:
                        1. 99.95% uptime for uninterrupted financial operations.
                        2. Scalability improvements to accommodate growing user needs.
                        3. New feature rollouts, including enhanced reporting and multi-entity financial consolidation.
                
                Key Outcomes & Impact:
                    1. Accelerated financial close cycles: Reduced time spent on reconciliation and reporting.
                    2. Enhanced transparency: Real-time tracking and financial insights for better decision-making.
                    3. AI-Driven efficiency: Automated invoice processing, reducing manual data entry.
                    4. Seamless accounting integration: Direct sync with Exact and other financial tools.
                    5. Scalable & secure platform: Microservices-based design for long-term growth and compliance.
                InHouse Finance empowers finance teams to work smarter, close faster, and maintain full visibility over financial operations, making financial closing a seamless and efficient process.
                """

    @staticmethod
    def ecommerce_clients_data():
        return """
                Client Name: Caraudiogigant
                
                Industry: E-commerce Automotive Aftermarket
                
                Services: Shopify Website development & data migration
                
                Duration: 4 months + ongoing support
                
                Skillsets Utilized: UI/UX designer, Shopify developer, Data migration specialist, Product Owner
                
                Project Brief: A leading car components e-retailer sought to migrate from Lightspeed to Shopify to enhance performance, flexibility, and user experience. The migration required preserving critical business functionalities, ensuring seamless data transfer, and optimizing the online store’s structure and navigation. With an end-to-end implementation completed in just one month, the transition achieved zero downtime and 100% data migration without loss, ensuring uninterrupted business operations and improved platform capabilities.
                
                Project Scope and Objectives: The project was designed to address key migration challenges while enhancing the online store’s usability and performance:
                    1. Theme Selection & Customization – Identifying and adapting the best Shopify theme to match the brand’s needs.
                    2. Menu & Category Optimization – Structuring product categories and the menu bar for intuitive navigation.
                    3. Search Widget Enhancement – Implementing an advanced search tool tailored for automotive components.
                    4. Bridging Functionality Gaps – Custom development to replicate critical Lightspeed features within Shopify.
                    5. UX/UI Enhancements – Custom functionalities to improve user experience and increase conversion rates.
                    6. Zero Downtime & Data Integrity – Ensuring a smooth transition with no business disruption.
                
                Technology Stack and Architecture: The migration leveraged a robust technology framework to facilitate seamless integration and customization:
                    1. Shopify Liquid: Custom theme and feature development.
                    2. JavaScript & Shopify Scripts: Enhancements for search, navigation, and user interaction.
                    3. Shopify API: Enabling data migration and custom business logic.
                    4. Lightspeed Data Export & Transformation: Ensuring structured and complete data transfer.
                    5. AWS Hosting: Secure backup and testing environment for pre-launch validation.
                
                Project Delivery:
                    Team Composition: The project was executed by an agile and focused team:
                        1. 1 Product Owner, Overseeing execution and business alignment.
                        2. 1 UI/UX Designer, Ensuring smooth interface transitions and user experience enhancements.
                        3. 2 Developers, Focused on Shopify customization, API integration, and data migration.
                
                Execution: Following an Agile approach, the migration was completed in one month with structured phases:
                    Phase 1: Requirements & Theme Selection (Week 1) – Identified optimal Shopify theme and migration plan.
                    Phase 2: UX/UI Enhancements & Custom Features (Week 2) – Optimized search, menu, and checkout for improved user experience.
                    Phase 3: Testing & Quality Assurance (Week 3) – Validated store functionalities and business requirements.
                    Phase 4: Data Migration & Deployment (Week 4) – Transferred products, customers, and order history while ensuring a smooth go-live execution.
                
                Key Outcomes & Impact:
                    1. 100% data integrity: Products, customer records, and order history migrated without loss.
                    2. Zero downtime: No service disruption, ensuring continued sales and operations.
                    3. Enhanced UX/UI: Improved navigation, search efficiency, and checkout experience.
                    4. Business continuity & growth: A future-ready Shopify store, optimized for scalability and performance.
                
                The successful Lightspeed to Shopify migration positioned the car components e-retailer for long-term growth, delivering a modernized, highly functional, and customer-friendly e-commerce platform without any operational setbacks.
                """

    @staticmethod
    def get_email_template_one():
        """
        This function contains the email template for email sequence 1.
        """
        return """
        EMAIL SEQUENCE: Email 1 of 5 – Initial Outreach
        OBJECTIVE: The objective is to give a warm introduction to the prospect with clear relevance and credibility using a compelling message. We can talk about the pain point the prospect could be facing based on their profile and job openings they have posted, and also mention the summary and name of the relevant client we have already served if the industry of both matches. Also, use a pain point relevant to their industry or business stage.

        =================================================
        === CORE RULE: CLIENT MENTION & FACTUALITY POLICY ===
        =================================================
        This is the most important rule and overrides all other instructions.

        1.  **Check for a Relevant Client:** A client is ONLY relevant if their industry in the provided data **exactly matches** the prospect's industry.

        2.  **IF a relevant client is found:**
            - You MUST use their specific name and data.
            - Use this content format: "We recently helped [Client Name], a company in your industry, to [achieve a specific, quantifiable result like 'migrate their system in 30 days, improving efficiency by XX%']. Thought it might resonate."
            - Only use the quantifiable results if they are provided in the client's data.

        3.  **IF no relevant client is found (or no client data is provided):**
            - You are **STRICTLY PROHIBITED** from mentioning any client name, case study, or success story.
            - **DO NOT** invent clients, use placeholder names, or refer to "similar companies," "a company in your industry," or any other generic descriptor.
            - In this case, the email must focus only on the prospect's potential pain points and our general value proposition.

        **This logic is absolute. Factual accuracy is the top priority.**
        =================================================


        === STRUCTURE & STRATEGY ===

        ➤ SUBJECT LINE
            Craft subject lines that make the prospect want to open the email. Keep them personalized, curiosity-driven, and relevant to the recipient’s role, company, or challenges.

        Guidelines:
            - Use their first name, role, or company naturally
            - Keep it short and compelling
            - Make it feel professional, not like a mass email
            - Focus on value, benefit, or intrigue
            - Improve clarity and uniqueness, and always refer to the sample lines
            - The subject lines should be relevant to the pain points for the company and industry
            - **[REMOVED]** The conflicting line about using clients from similar industries has been removed.
            - Do not use "PS." in this email at any point in the content
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

        Avoid: Generic lines like “Accelerate Your Hiring.” Push for specific, thoughtful hooks that spark interest.

        ➤ TONE
            - Conversational yet professional: Write as a real human would speak — warm, friendly, informed, confident but not aggressive. There should be very subtle transitions in the email, like starting with pain points, then subtly talking about a success story of a client, and then subtly presenting the value proposition.
            - Avoid stiff corporate speak or overused sales clichés.

        ➤ LANGUAGE
            - American English
            - Simple, clear, and persuasive. Avoid buzzwords or unnecessary technical details.

        ➤ WORD COUNT
            - Between 100–120 words. Short, readable, and value-packed.

        ➤ PERSONALIZATION TRIGGERS (to appear early in the email):
        Craft a concise email that directly addresses the prospect’s key hiring challenges, using insights from the job roles they are actively hiring for. All client and data mentions MUST follow the CORE RULE above.
            - Focus the email body on the specific challenges they might be facing in filling these roles (e.g., speed, quality, niche skills, scaling needs).
            - The email subject line should be creative and attention-grabbing while directly reflecting these pain points — especially those related to difficulty in hiring for the listed positions. Always refer to the sample subject lines.
            - Keep the tone professional but conversational, and include a subtle CTA if relevant.
            - The email should always sound human and natural. Avoid making it sound like AI. The tone and flow must be smooth and clear.
            - You can always use this benefit and value proposition in this email: "Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region."
            - **[REMOVED]** All redundant instructions about client mentions have been removed as they are now covered by the CORE RULE at the top.

        ➤ VALUE ANGLE
            - Lead with pain points or inefficiencies that are common in the prospect’s industry or tech stack (e.g., legacy platforms, sluggish UX, low conversion rates).
            - In this email, always remember to add this point as a value proposition, in a subtle way:
            - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.

        ➤ CONTENT FORMAT
            - **[REMOVED and REPLACED]** This section is now governed entirely by the CORE RULE at the top of the prompt.

        ➤ CLOSING
            - Mention that Rounak (Business Development Lead) will follow up shortly.

        === PROMPT INSTRUCTION TO MODEL ===

        1.  **Strictly adhere to the CORE RULE: CLIENT MENTION & FACTUALITY POLICY at all times.**
        2.  Analyze the following prospect attributes:
            - Profile summary, job title, headline, current tech stack (if known), industry, and the job they are hiring for.
            - From their profile, identify potential pain points and how we can solve them as a staffing company.
        3.  Based on this context:
            - Craft a first-line hook that reflects a pain point.
            - Follow the CORE RULE to determine if a client story can be included.
            - Ensure any story feels natural and applicable to the reader.
        4.  Do NOT:
            - Mention “support tickets”.
            - Start the email with a title-based intro like “As a Head of Engineering...”
            - Push for a meeting in the first email — the goal is awareness and engagement. Instead, suggest that they book a meeting using the link provided if interested.

            === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===

            Subject Line Samples for Reference:  
            [
            "Accelerate Your [Job Title] - Vetted Developers Available",
            "Quality Frontend Developers for [Company Name] Growth",
            "Flexible [Job Title] Solutions for Vallum Associates",
            "Senior Full Stack Developers for Web3 Projects"
            ]

            Email Sample (for reference only, not to be copied):
                
                Hi [First Name],<br><br>
                I'm Ahmed, Co-founder of InHousen — a Dutch-based tech solutions company. We specialize in helping businesses to solve [painpoints specific to the prospect's industry].<br><br>
                Our team guarantees a smooth transition with minimal downtime and full design & data integrity.<br><br>
                We've also attached our company portfolio—please do take a look to learn more about our work.<br><br>
                Would love to show you how we can future-proof your online presence.<br><br>
                Also, my colleague Rounak, who leads our business development efforts, will be reaching out to you shortly to assist with any immediate needs or questions.

            === SUBJECT LINE SUGGESTIONS ===  
                This is the structure to be followed for the subject lines in this email:  
                - First Name of the prospect + Objective (Accelerate, Quality, Flexible, etc.) + Job Opening + Company Name  
                - Use the first name of the person, and optionally use the job title from the job opening and how we can help them with that  
                - First name + the prospect’s requirement

            === FINAL NOTES ===  
                - As a value addition, include this point in the email subtly:  
                - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.  
                - Use clear HTML formatting and 2–3 sentence paragraphs.  
                - Write in a way that feels tailored and human — not like a generic mass email.  
                - Use the example emails as references — not to be copied directly — to create high-quality, compliant outputs.  
                - Generate only the email body — do not include any signature or sign-off.  
                - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
                - Avoid mentioning any clients we haven’t actually worked with. Only reference real clients we’ve helped—no assumptions or generic claims.
                - Never include lines like “We recently helped a similar company.” Only mention specific clients we’ve actually worked with—no generic or assumed references.
        """

    # @staticmethod
    # def get_email_template_one():
    #     """
    #     This function contains the email template for email sequence 1.
    #     """
    #     return """
    #     EMAIL SEQUENCE: Email 1 of 5 – Initial Outreach
    #     OBJECTIVE: The objective is to give a warm introduction to the prospect with clear relevance and credibility using a compelling message. We can talk about the pain point the prospect could be facing based on their profile and job openings they have posted, and also mention the summary and name of the relevant client we have already served if the industry of both matches. Also, use a pain point relevant to their industry or business stage.

    #     === STRUCTURE & STRATEGY ===

    #     ➤ SUBJECT LINE
    #         Craft subject lines that make the prospect want to open the email. Keep them personalized, curiosity-driven, and relevant to the recipient’s role, company, or challenges.

    #     Guidelines:
    #         - Use their first name, role, or company naturally
    #         - Keep it short and compelling
    #         - Make it feel professional, not like a mass email
    #         - Focus on value, benefit, or intrigue
    #         - Improve clarity and uniqueness, and always refer to the sample lines
    #         - The subject lines should be relevant to the pain points for the company and industry
    #         - Always use client names if we have served clients in a similar industry as that of the prospects
    #         - Do not use "PS." in this email at any point in the content
    #         - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) in the email for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
    #         - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

    #     Avoid: Generic lines like “Accelerate Your Hiring.” Push for specific, thoughtful hooks that spark interest.

    #     ➤ TONE
    #         - Conversational yet professional: Write as a real human would speak — warm, friendly, informed, confident but not aggressive. There should be very subtle transitions in the email, like starting with pain points, then subtly talking about a success story of a client, and then subtly presenting the value proposition.
    #         - Avoid stiff corporate speak or overused sales clichés.

    #     ➤ LANGUAGE
    #         - American English
    #         - Simple, clear, and persuasive. Avoid buzzwords or unnecessary technical details.

    #     ➤ WORD COUNT
    #         - Between 100–120 words. Short, readable, and value-packed.

    #     ➤ PERSONALIZATION TRIGGERS (to appear early in the email):
    #     Craft a concise email that directly addresses the prospect’s key hiring challenges, using insights from the job roles they are actively hiring for. Avoid exaggeration or unsupported claims — only include details that are grounded in the available data.
    #         - Focus the email body on the specific challenges they might be facing in filling these roles (e.g., speed, quality, niche skills, scaling needs).
    #         - The email subject line should be creative and attention-grabbing while directly reflecting these pain points — especially those related to difficulty in hiring for the listed positions. Always refer to the sample subject lines.
    #         - Keep the tone professional but conversational, and include a subtle CTA if relevant.
    #         - Mention the prospect’s **industry** (e.g., automotive e-commerce, fashion, food delivery). If we have previously served clients in a similar industry, use their name and information to build trust.
    #         - Include the **specific use case** (e.g., platform migration, checkout speed optimization, design refresh).
    #         - Reference a **quantifiable result** from a real or simulated past project (e.g., “45% faster checkout”, “0 downtime”, “100% data integrity”). Only mention this if it's included in the relevant client's data — never falsely mention this information. Never hallucinate or provide incorrect information. Only mention clients and numbers if they are verified and mentioned in the data.
    #         - The email should always sound human and natural. Avoid making it sound like AI. The tone and flow must be smooth and clear.
    #         - You can always use this benefit and value proposition in this email: "Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region."
    #         - Avoid mentioning any clients we haven’t actually worked with. Only reference real clients we’ve helped—no assumptions or generic claims.
    #         - Never include lines like “We recently helped a similar company.” Only mention specific clients we’ve actually worked with—no generic or assumed references.

    #     ➤ VALUE ANGLE
    #         - Lead with pain points or inefficiencies that are common in the prospect’s industry or tech stack (e.g., legacy platforms, sluggish UX, low conversion rates).
    #         - In this email, always remember to add this point as a value proposition, in a subtle way:
    #         - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.

    #     ➤ CONTENT FORMAT
    #         - After subtly introducing the prospect’s pain point, if a relevant client from our database is found, then mention it this way: "We recently helped a [Client Industry] company migrate their system in 30 days, improving efficiency by [XX]%. Thought it might resonate."
    #         - If no relevant client is found, do not falsely claim that we helped a big company. In that case, simply focus on their pain point and how we can help.

    #     ➤ CLOSING
    #         - Mention that Rounak (Business Development Lead) will follow up shortly.

    #     === PROMPT INSTRUCTION TO MODEL ===

    #     1. Analyze the following prospect attributes:
    #         - Profile summary, job title, headline, current tech stack (if known), industry, and the job they are hiring for.
    #         - From their profile, identify potential pain points and how we can solve them as a staffing company.

    #     2. Based on this context:
    #         - Craft a first-line hook that reflects a pain point and leads into a relevant client success story.
    #         - Include data-backed results or efficiencies gained from InHousen projects or served clients.
    #         - Ensure the story feels natural and applicable to the reader.

    #     3. Do NOT:
    #         - Mention “support tickets”.
    #         - Start the email with a title-based intro like “As a Head of Engineering...”
    #         - Push for a meeting in the first email — the goal is awareness and engagement. Instead, suggest that they book a meeting using the link provided if interested.

    #     4. Clients (Industry-Based Referencing):

    #         - If relevant client data is available:
    #         - Reference specific clients by name (if appropriate).
    #         - Use relevant and verifiable details — such as quantifiable results, context-specific outcomes, or unique use cases — to build trust and relevance.
    #         - Ensure the mention feels relevant and natural to the reader’s context.

    #         - If no relevant client data is available:
    #         - Do **not** say we’ve worked with "similar companies" or imply industry similarity.
    #         - Do **not** mention any client name.
    #         - Instead, focus on how we can help and highlight our value proposition.

    #         - Under **no circumstances** should you:
    #         - Fabricate, exaggerate, or generalize client experience to suggest we have served the prospect’s industry if we haven’t.
    #         - Reuse or repeat client names across multiple emails in the sequence unless it adds new and relevant context.

    #     This logic must be strictly followed to ensure relevance, transparency, and trustworthiness.

    #     === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===

    #     Subject Line Samples for Reference:
    #     [
    #     "Accelerate Your [Job Title] - Vetted Developers Available",
    #     "Quality Frontend Developers for [Company Name] Growth",
    #     "Flexible [Job Title] Solutions for Vallum Associates",
    #     "Senior Full Stack Developers for Web3 Projects"
    #     ]

    #     Email Sample (for reference only, not to be copied):

    #         Hi [First Name],<br><br>
    #         I'm Ahmed, Co-founder of InHousen — a Dutch-based tech solutions company. We specialize in helping businesses to solve [painpoints specific to the prospect's industry].<br><br>
    #         Our team guarantees a smooth transition with minimal downtime and full design & data integrity.<br><br>
    #         We've also attached our company portfolio—please do take a look to learn more about our work.<br><br>
    #         Would love to show you how we can future-proof your online presence.<br><br>
    #         Also, my colleague Rounak, who leads our business development efforts, will be reaching out to you shortly to assist with any immediate needs or questions.

    #     === SUBJECT LINE SUGGESTIONS ===
    #         This is the structure to be followed for the subject lines in this email:
    #         - First Name of the prospect + Objective (Accelerate, Quality, Flexible, etc.) + Job Opening + Company Name
    #         - Use the first name of the person, and optionally use the job title from the job opening and how we can help them with that
    #         - First name + the prospect’s requirement

    #     === FINAL NOTES ===
    #         - As a value addition, include this point in the email subtly:
    #         - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.
    #         - Use clear HTML formatting and 2–3 sentence paragraphs.
    #         - Write in a way that feels tailored and human — not like a generic mass email.
    #         - Use the example emails as references — not to be copied directly — to create high-quality, compliant outputs.
    #         - Generate only the email body — do not include any signature or sign-off.
    #         - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
    #         - Avoid mentioning any clients we haven’t actually worked with. Only reference real clients we’ve helped—no assumptions or generic claims.
    #         - Never include lines like “We recently helped a similar company.” Only mention specific clients we’ve actually worked with—no generic or assumed references.
    #     """

    @staticmethod
    def get_email_template_two():
        """
        This function contains the email template for email sequence 2.
        """
        return """
        EMAIL SEQUENCE: Email 2 of 5 – Educational Follow-up  
        OBJECTIVE: Build credibility by educating the prospect on InHousen's capabilities and success stories, reinforcing relevance, and encouraging a meeting.

        === STRUCTURE & STRATEGY ===

        ➤ GUIDELINES  
            - Do not use "PS." in this email at any point in the content.  
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) in the email for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

        ➤ TONE  
            - Professional yet approachable: informative but not pushy.  
            - Friendly and helpful — aim to nurture interest and trust.

        ➤ LANGUAGE  
            - American English  
            - Clear, concise, and focused on benefits and outcomes.

        ➤ WORD COUNT  
            - Between 60–100 words. Short enough to be read quickly, with high informational density.

        ➤ PERSONALIZATION TRIGGERS (to appear early in the email):  
            - Mention the **First Name** of the person for personalization and recognition.  
            - Highlight a **common pain point** within their **industry** to resonate with their challenges.  
            - Always include a relevant case study based on the identified pain point.

        ➤ VALUE ANGLE  
            - Emphasize InHousen’s portfolio and previous work — especially Shopify migrations and storefront solutions.  
            - Highlight tangible results such as zero downtime, UX improvements, scalability, and data integrity.  
            - Educate on how these solutions address typical industry pain points and support growth goals.

        ➤ CLOSING  
            - Express anticipation of future communication.

        === PROMPT INSTRUCTION TO MODEL ===

            1. Review the prospect’s company name and industry.  
            2. Identify a relevant pain point that companies in their industry commonly experience (e.g., migration complexity, platform downtime, poor UX).  
            3. Generate a short, educational email that:  
            - References the prospect by company name.  
            - Briefly introduces InHousen’s portfolio, showcasing Shopify and storefront solutions.  
            - Lists key benefits our solutions have delivered in past projects (e.g., zero downtime, fast turnarounds, scalability, data integrity).  
            - Invites the recipient to schedule a 15-minute meeting for a personalized discussion. Also, inform them that they can schedule the meeting using the link provided below.
            
            4. Ensure the message is friendly, concise, and tailored to industry needs.  
            5. Use bullet points or short paragraphs for easy scanning.  
            6. Provide 3–4 subject line options related to portfolio and case study themes.

        === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===

        Subject Options (for reference only):
            - The subjects should be more aligned towards the prospects need and pain points rather than a generic from template.
            [
            "30-Day Migration: How We Boosted Auto Parts Sales by 28%",
            "Lightspeed to Shopify in 30 Days (Without the Headaches)",
            "We Solved Their Lightspeed Problems in 30 Days. Yours Next?",
            "This Auto Parts Retailer's 30-Day Transformation (Case Study)"
            ]

        Email just for reference and never to be copied:

                Hi [First Name],<br><br>
                
                Just wanted to share a quick example of how we recently helped a <client's industry> company achieve meaningful results in just 30 days:<br><br>

                [Our Offerings]
                - Zero downtime during implementation<br>
                - 100% data integrity maintained<br>
                - Custom feature development based on their specific needs<br>
                - 45% improvement in key performance metrics<br><br>
                
                Our Business Development Lead, Rounak, will be in touch this week to explore how we can drive similar outcomes for your team.<br><br>
                Want to connect sooner? Feel free to use the meeting link below to schedule a quick chat.<br><br>
                “I was dreading the transition for months, but your team made it so smooth — I wish we’d done it sooner.” – Recent Client

        === SUBJECT LINE SUGGESTIONS ===  
            1. Build the subject line by understanding their requirement and how we can help them with those requirements.  
            2. Use this structure: Their requirement + how we can help them + value proposition.

        === FINAL NOTES ===  
            - Write in a way that sounds helpful and solution-oriented.  
            - You can always add value propositions from the "About InHousen" dataset in this email to increase credibility.  
            - Keep sentences brief and paragraphs tight for easy reading.  
            - Use the prospect’s company name and industry explicitly to personalize and show understanding.  
            - Use the above sample emails as references — not to be copied directly — to create the best emails that match the requirements.  
            - Generate only the email body. Do not include any signature or sign-off.
            - The subjects should be more aligned towards the prospects need and pain points rather than a generic from template.
            - Important Email Content Instructions:
                • The email content must be tightly aligned with the prospect’s specific requirements, role, and industry.
                • Do not fabricate, guess, or include any generic, unrelated, or hypothetical information.
                • Use only the data explicitly provided to you (e.g., client background, job post, LinkedIn profile, past interactions, case studies, etc.).
                • If certain information (like a relevant case study, pain point, or client name) is not provided, do not invent it or imply it.
                • Every statement must be verifiable and grounded in the provided inputs.
                • Your response should reflect a deep understanding of their domain and avoid one-size-fits-all language.
            
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        """

    @staticmethod
    def get_email_template_three():
        """
        This function contains the email template for email sequence 3.
        """
        return """
        EMAIL SEQUENCE: Email 3 of 5 – Storytelling Focus  
        OBJECTIVE: Build an emotional connection by sharing a relevant client success story (only if the client's data is available) that aligns with the prospect’s scale, niche, or pain points — demonstrating how our solution delivered concrete results. If client data is not available, then clearly communicate InHousen’s value proposition as the core of the message.

        === STRUCTURE & STRATEGY ===

        ➤ GUIDELINES  
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) in the email for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

        ➤ TONE  
            - Professional yet warm and engaging.  
            - Use a conversational storytelling style to create empathy and build trust.  
            - Motivating and confident — clearly demonstrate how the challenge was overcome.

        ➤ LANGUAGE  
            - American English  
            - Clear, vivid, and descriptive — painting a picture that is relatable and specific.

        ➤ WORD COUNT  
            - Between 120–180 words to allow for a concise yet meaningful narrative.

        ➤ PERSONALIZATION TRIGGERS (to appear early or within the story):
            - Use the person’s **first name** for a more personalized and human tone.  
            - Identify and clearly state the **challenge faced** by the referenced client or prospect.  
            - Quantify the **result or impact** in clear metrics (e.g., "45% faster checkout") — but only if the data exists in the relevant client context.  
            - Reference **Client Type** similar to the prospect (e.g., fast-growing startup, mid-size retailer) — again, only if that information is available in the client dataset.  
            - If no relevant data is provided, do **not fabricate** or hallucinate details. Use only InHousen's own value propositions in that case.  
        - Always highlight the **value angle** clearly, using verifiable results if available, and trust-building language if not.

        ➤ VALUE ANGLE  
            - If client data is available: Share a real, relevant success story about a similar company and the outcome of InHousen’s solution.  
            - Emphasize measurable improvements like:  
                - Faster load times  
                - Zero downtime  
                - Scalable infrastructure  
                - SEO retention  
            - If client data is not available: Focus entirely on InHousen’s strengths and capabilities — e.g., efficient processes, experienced talent, and tailored solutions.

        ➤ CLOSING  
            - End with a positive, forward-looking tone. Invite them to schedule a brief call or exploration session to discuss their situation.

        === PROMPT INSTRUCTION TO MODEL ===

            1. Begin by identifying a common business challenge the prospect is likely facing based on their industry, size, or job listings (e.g., "risk of website migration," "complex hiring needs," etc.).  
            2. If the dataset includes a relevant client that experienced a similar challenge:  
            - Mention the client (only if their name is in the provided data).  
            - Describe the challenge they faced.  
            - Explain what InHousen did and the measurable results.  
            3. If no client data is available, avoid mentioning any specific names or figures. Instead, rely on InHousen's value propositions to establish credibility.  
            4. Emphasize InHousen’s capabilities, such as:  
            - Seamless transitions  
            - Zero downtime  
            - SEO retention  
            - Streamlined performance improvements  
            5. Close with an invitation to explore how similar results can be delivered for the prospect’s business.  
            6. Ensure the overall tone is empathetic, confident, natural, and trustworthy — not overly promotional or robotic.

        === SAMPLE OUTPUT STRUCTURE (For Reference Only — Do Not Copy) ===

        Subject Line Samples (for reference only):  
            [
            "Website Migration Doesn't Have to Be Painful",
            "Say Goodbye to Website Downtime Fears",
            "Seamless Transition to Shopify — See How",
            "Is Website Migration Holding Back Your Growth?"
            ]

        Example email (for reference only — not to be copied):

            Hi [First Name],<br><br>
            We understand website migrations can feel risky — loss of data, broken designs, SEO drops.  
            At InHousen, we ensure:<br><br>
                - Full SEO retention<br>
                - Smooth design and content transfer<br>
                - Optimized loading speeds post-migration<br>
                - Zero downtime during the transition<br><br>
            Our migration specialist would love to discuss your specific needs. Ready to explore options?<br><br>
            Let’s help you shift smarter, not harder.

        === SUBJECT LINE SUGGESTIONS ===  
            - Combine insight + the prospect’s requirement + our value proposition  
            - For example: “Faster Site Speed for [Prospect’s Industry] Growth” or “Avoid Downtime During Checkout Optimization”  
            - Focus on emotional resonance (risk/fear reduction) and impact (results/benefits)

        === FINAL NOTES ===  
            - Use bullet points for easy reading and visual clarity.  
            - Use HTML formatting for line breaks (<br>) and appropriate spacing.  
            - Personalize with the prospect’s name and reference a relatable client type or challenge if appropriate.  
            - The tone should be warm, credible, and lightly persuasive — not salesy.  
            - Use the above email samples only as references. Do not copy them.  
            - Generate only the **email body** — do not include any sign-off or signature.  
            - Important Note: Never fabricate client data or results. Always use facts that are explicitly available in your dataset. If no data is available, focus only on InHousen’s general capabilities and value propositions.  
            - Use clean formatting, maintain consistent spacing, and keep the structure readable across devices.
            - Ensure that no placeholders are left empty in the final email. Before generating the output, thoroughly check that all dynamic fields (e.g., name, company, industry, pain points) are properly filled based on the provided data. The email should feel complete, coherent, and ready to send without requiring manual edits.
        """

    @staticmethod
    def get_email_template_four():
        """
        This function contains the email template for email sequence 4.
        """
        return """
        EMAIL SEQUENCE: Email 4 of 5 – Satirical + Casual Tone  
        OBJECTIVE: Use light humor and relatable satire to engage prospects by playfully highlighting common frustrations in their role or company culture — and then present your flexible solution as the easy fix.

        === STRUCTURE & STRATEGY ===

        ➤ GUIDELINES  
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) in the email for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

        ➤ TONE  
            - Satirical, witty, and casual to create a friendly, approachable vibe.  
            - Humor should be relevant and respectful, tailored to the prospect’s job title and known bottlenecks in the decision-making process.  
            - Use playful sarcasm or light, funny comparisons the prospect is likely to relate to.

        ➤ LANGUAGE  
            - Conversational American English with humor and light sarcasm.  
            - Avoid heavy jargon — keep the tone accessible and enjoyable.

        ➤ WORD COUNT  
            - Between 150–200 words to allow enough room for a humorous narrative while preserving clarity.

        ➤ PERSONALIZATION TRIGGERS  
            - Use the prospect’s **first name** and **job designation** for a more personalized and human tone. Always make sure that you start the email with Person's first name.
            - Job Title + Decision Bottleneck + Funny Relatable Comparison  
            - Use the prospect’s **Job Title** or role to tailor references and humor.  
            - Identify a common **Decision Bottleneck** they might experience (e.g., slow approval cycles, outdated tools, over-complicated workflows).  
            - Use a **Funny, Relatable Comparison** to make the email memorable and human.

        ➤ VALUE PROPOSITION  
            - Emphasize InHousen’s flexibility, simplicity, and client-first mindset.  
            - Highlight clear points of differentiation, such as: You can get other value propositions and offerings from About Inhousen section.
                - No long-term contracts  
                - Transparent, upfront pricing  
                - One-month exit clause  
                - High-quality, on-demand talent  
            - Position your offering as the no-BS, zero-friction alternative to traditional agencies and convoluted hiring models.

        ➤ CLOSING  
            - Use a casual and warm tone to wrap up, reinforcing InHousen’s accessibility and readiness to help.  
            - Invite them to schedule a quick exploratory call.

        === PROMPT INSTRUCTION TO MODEL ===

            1. Start the email with a light, witty observation that pokes fun at a frustrating reality in the prospect’s work life (e.g., “Still running hiring through 12 approval rounds and 3 invisible stakeholders?”).  
            2. Follow that with a humorous but clear introduction of InHousen’s solution as a refreshing alternative.  
            3. Present the key value points using clean bullet formatting:  
                - No long-term contracts  
                - Transparent pricing  
                - One-month exit  
                - Just top talent, when you need it  
            4. Prompt the prospect to consider if they’d like to explore how this approach could work for them.  
            5. Keep the tone laid-back and upbeat while still being informative.  
            6. Encourage scheduling a call using a clear CTA, but without a hard sales push.

        === SAMPLE OUTPUT STRUCTURE (FOR REFERENCE ONLY — DO NOT COPY) ===

        Subject Lines (for reference only):  
            [
            "Need a Tech Team Without the Long-Term Lock-in?",
            "Our Flexible Engagement Options Might Surprise You",
            "Custom Website Work — Only When You Need It",
            "One-Month Exit, Full Support — InHousen Style"
            ]

        Sample email body (just for format reference — do not copy directly):
            - The email body must be personalized to the specific prospect and should not feel copied or generic. Carefully analyze the prospect’s needs, context, and challenges, then thoughtfully align those with InHousen’s value propositions. The final output should reflect a natural blend of both — addressing the prospect’s situation directly while showcasing relevant ways InHousen can help.

            Hi [First Name],<br><br>

            Still trying to push a new initiative through six rounds of internal approvals, a Slack poll, and maybe a prayer circle?<br><br>
            Let’s make things easier.<br><br>
            At InHousen, we keep things refreshingly simple — built to support your team without the usual friction:<br><br>
                – No long-term contracts<br>
                – Transparent, upfront pricing<br>
                – One-month exit flexibility<br>
                – Scale engagement up or down based on your needs<br><br>
            No corporate rituals, no buried terms — just real results from a team that’s easy to work with.<br><br>
            Want to see how it could work for your team?<br><br>


        === SUBJECT LINE SUGGESTIONS ===  
            - Build subject lines using casual, witty language that aligns with the value angle.
            - Examples (for structure only — model should generate new ones):  
                - "[First Name], still dealing with 3-week approval cycles?"  
                - "Top-tier talent, no long-term lock-in — too good to be true?"  
                - "Flexible tech support, minus the fine print"  
                - "One-month exit, full-stack support — InHousen style"

        === FINAL NOTES ===  
            - Humor should be inclusive, never offensive or sarcastic at the prospect’s expense.  
            - Tailor jokes to the industry, role, or pain points — avoid generic or out-of-touch satire.  
            - Write in a way that sounds human, direct, and fun — not overly clever or forced.  
            - Maintain clear formatting:
                - HTML line breaks (`<br>`) for spacing
                - Short paragraphs or bullet lists for readability
            - Use the provided samples for structure only — never copy content directly.
            - Generate only the **email body** — do not include any sign-off or signature.
            - Important: Never misrepresent the offering. Keep all value claims factual and based on InHousen’s actual capabilities.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.
            - The email body must be personalized to the specific prospect and should not feel copied or generic. Carefully analyze the prospect’s needs, context, and challenges, then thoughtfully align those with InHousen’s value propositions. The final output should reflect a natural blend of both — addressing the prospect’s situation directly while showcasing relevant ways InHousen can help.
        """

    @staticmethod
    def get_email_template_five():
        """
        This function contains the email template for email sequence 5.
        """
        return """
        EMAIL SEQUENCE: Email 5 of 5 – Professional, Concise Breakup Email  
        OBJECTIVE: Politely acknowledge the prospect’s busy schedule and lack of response, offer an easy opt-out, and gently remind them of additional offerings — all while keeping the message short, respectful, and professional.

        === STRUCTURE & STRATEGY ===

        ➤ GUIDELINES  
            - Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) in the email for spacing and formatting. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
            - Important Instruction: Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.

        ➤ TONE  
            - Professional, courteous, and respectful.  
            - Warm but direct — acknowledge their potential lack of interest without applying pressure.  
            - Maintain clear, sincere, and straightforward communication.

        ➤ LANGUAGE  
            - Simple, plain American English.  
            - Avoid jargon or overly promotional/salesy language.  
            - Personalize with the prospect’s [First Name] and [Designation].

        ➤ WORD COUNT  
            - Keep the message concise: between 50–70 words to respect their time and inbox space.

        ➤ PERSONALIZATION TRIGGERS  
            - Always make sure that you start the email with Person's first name.
            - Use the prospect’s **first name** and **job designation** for a more personalized and human tone.  
            - Acknowledge the common reality of a busy inbox and packed schedule.

        ➤ CONTENT FOCUS
            - Since the prospect has not responded to any of the previous emails, this should be treated as the final email in the sequence.
            - Ask if you are not the right person, then can they direct us to the right person?
            - Deliver a polite and professional “breakup message,” such as:  
            *“I won’t keep nudging if the timing’s not right.”*  
            - Remind them briefly that InHousen offers more than just full-scale migrations:  
                - Mention all the relevant Inhousen offerings
            - If they’re not interested at the moment, they can always reach out to us in the future if they have any requirements.
            - Highlight how **incremental improvements** can lead to meaningful impact — without needing a full overhaul.  
            - Invite them to schedule a brief call if and when the time is right. If the time feels right, feel free to schedule a quick call using the meeting link below.
            - Include a polite line asking:
                - “If you’re not the right person for this, could you kindly point me to the person who is?”

        === PROMPT INSTRUCTION TO MODEL ===
            - Always make sure that you start the email with Person's first name.
            1. Start the message by acknowledging that the prospect may be too busy or that the timing might not be right at the moment. You can always atrt the email with their first name. 
            2. Politely offer to stop the outreach and give them the option to re-engage on their terms.  
            3. Mention additional offerings from InHousen that can be helpful even without a full migration. These may include:  
                - Design & usability improvements  
                - Adding custom features for UX  
                - Optimizing site speed and mobile performance  
            4. Reinforce the idea that **small changes** can make a big difference.  
            5. Include a **simple, optional CTA** inviting them to schedule a quick conversation.  
            6. Close on a polite and optimistic note, without being pushy.

        === SAMPLE OUTPUT STRUCTURE (FOR FORMAT REFERENCE ONLY — DO NOT COPY) ===

        Subject Lines (for reference only): 
            - 	The subject lines must be personalized based on the prospect’s specific needs or context. Since this is the final email in the sequence, the subject should also reflect an appropriate closing tone — respectful, concise, and relevant to their decision stage.
            [
            "Still Debating That Website Upgrade?",
            "Here If You’re Ready to Modernize",
            "Your Website Can Do More — We’ll Show You How"
            ]

        Sample email body (for structure only — not to be copied):

            Hi [First Name],<br><br>
            
            Totally understand if now’s not the right time — no pressure at all.<br><br>
            
            Just in case it’s helpful down the line, we also support teams with:<br><br>
                - UX and design improvements without a full migration<br>
                - Custom functionality for better user experience<br>
                - Performance tuning (site speed, mobile optimization)<br><br>
            
            Even small changes can deliver big results.<br><br>
            Feel free to reach out anytime if you'd like to explore options.

        === SUBJECT LINE SUGGESTIONS ===
            - The subject lines must be personalized based on the prospect’s specific needs or context. Since this is the final email in the sequence, the subject should also reflect an appropriate closing tone — respectful, concise, and relevant to their decision stage.
            - Tailor subject lines to gently re-engage curiosity or address the idea of small, manageable improvements.  
            - Examples (structure only — the model should generate new, context-aware versions):  
                - "Still Considering That [Job Requirement Title], [First Name]?"  
                - "Small Wins, Big Impact — Just Checking In"  
                - "We Can Help — Even Without a Full Redesign"

        === FINAL NOTES ===  
            - Keep the tone professional, warm, and non-intrusive.  
            - Avoid sounding passive-aggressive or overly eager.  
            - Bullet key value points clearly for quick readability.  
            - Use the prospect’s name and role to personalize the message where appropriate.  
            - Do not pressure them into replying — just offer an open door.  
            - Generate only the email body — do not include a signature or contact info.  
            - Important Note: Ensure the formatting is clean and professional. Use HTML line breaks (`<br>`) for spacing, and maintain consistent spacing throughout. Apply single or double line breaks thoughtfully to support structure and readability.
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
        Vision and Mission of InHousen
        - Vision: Empowering Innovation & Growth
            - To enable visionary founders and businesses by delivering tailored tech solutions and strategic guidance, helping them transform ideas into impactful products and sustainable ventures.
        
        - Mission: Shaping the Future of Possibilities
            - To become the go-to partner for startups and enterprises alike, known for turning concepts into reality with an approach that combines integrity, agility, and long-term growth.

        - Why Inhousen(USPs)
            1. Flexible Contract
            2. One month exit notice
            3. Price Optimum
        
        - Services we offer (Expertise)
        
        Develop your product: From Concept to Launch, we build products that drive your success.
        
            1. UI-UX Design: In a world of short attention spans, UI/UX can make or break your product. We craft intuitive and visually appealing designs that enhance user experience and drive engagement.
            2. MVP App Development: Want to test your product idea without heavy investment? We build scalable MVPs that allow you to validate your concept quickly and efficiently in the market.
            3. Mobile App Development: In a mobile-first world, performance matters. Our mobile app development expertise delivers responsive, high-performance apps for both iOS and Android platforms.
            4. Upgrade Legacy Apps: Don't let outdated technology hold you back. We modernize and upgrade legacy applications to improve performance, security, and scalability for long-term success.
            5. Quality Assurance: Your product’s reputation is on the line. Our quality assurance process ensures your product meets the highest standards of functionality, performance, and user satisfaction
        
        Build your team: Unlock success with skilled engineers and experts
        
            1. Full-time Engineers: Need dedicated talent? We place elite full-time engineers who become an integral part of your team, delivering high-impact results.
            2. Partial Sourcing: Scaling fast? Our partial sourcing solutions provide the flexibility to bring in expert talent exactly when and where you need it.
            3. Expert Advisory: Navigating complex challenges? Our expert advisors guide your strategy, ensuring your team has the right direction and support to succeed.
        
        Monetise your data: Turn data into revenue with smart insights.
        
            1. Advanced Analytics: Don't settle for simple insights—elevate your strategy with AI and ML. From predictive analytics to big data and real-time insights, we help you push further along the tech curve, staying ahead of the competition.
            2. Data Management: Data is only valuable when it's accessible and secure. We streamline your data management processes for seamless integration and efficient decision-making.
            3. Business Analytics: Starting your data journey? We help you build the foundation with actionable insights that prepare you for the next level. As we establish these insights, we ensure you're ready to scale toward advanced analytics for deeper, more impactful results"" - instead of establish use something more appropriate
        
        Build your venture: Turning vision into reality, every step of the way.
        
            1. Create My Start Up: Have a great idea but don’t know where to start? We help build your MVP, provide strategic advisory, connect you with funding, and execute your go-to-market plan, ensuring your start-up’s success.

                                 ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------   
        
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

        - Always remember to format the email properly using proper spacing in each email that you generate, and generate a personalized email sequence for each prospect using the information provided.

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
            - Prospects Company Industry (Refer to clients Industry for Similar Clients): {company_industry}
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

            Do not include any closing salutations, sign-offs, or signatures at the end of the emails. Keep the ending concise and professional without any personal sign-off and without using Ahmed's name.

            Important Note: Ensure the email formatting is clean and professional. Use HTML line breaks (<br>) only where necessary. Maintain proper spacing throughout the email, especially around bullet points. Apply single or double line breaks thoughtfully to enhance readability and structure.
        """

        prompt += """
            Strict Client Reference Rules Based on Industry Match
    
            Client Reference Policy (Strict Enforcement):
            
            When referencing past clients in the email:
            	1.	If we have served clients in the same industry as the prospect (based on available variables like energy_clients, fintech_clients, etc.):
            	•	You may mention those clients by name.
            	•	Only include information that demonstrates how we solved a specific challenge relevant to the prospect.
            	•	Keep it relevant and natural—do not exaggerate or overstate outcomes.
            	2.	If we do not have any clients in the same industry:
            	•	Do not say we’ve served similar clients.
            	•	Do not imply or fabricate similarity by industry.
            	•	Instead, say that:
            “We’ve worked with clients in other industries who faced similar challenges.”
            	•	This shows relevance based on the problem—not the domain.
            	3.	Never say or imply that we’ve worked with “similar companies in your industry” unless it’s supported by actual client data.
            	4.	Never fabricate or generalize client experience to make it seem more aligned than it is.
            	5.	Do not mention regions (e.g., “Europe”) unless explicitly instructed.
            
            📌 Important: These rules are mandatory and must be followed strictly in every email you generate. The goal is to be honest, relevant, and credible without misrepresenting our experience.
            """

        # Defining Personalization Triggers
        prompt += self.get_personalization_trigger()

        # prompt += "Take inspiration from the CTAs below to craft CTAs for all the emails."
        # prompt += self.get_cta_options()

        # Prospects Post Prompt
        prompt += self.get_prospects_post_prompt(posts)

        # About InHouse
        prompt += self.get_about_inhousen()

        # About InHousen Clients
        prompt += f"""
        
        Historical clients data, that we have served and the value they got from our service, segmented by industry, this data is to be used in the emails for the prospects who works in the same industry as below:
        
        - Energy Industry Clients = {self.energy_clients_data()}

                                                            ------------------------------------------------------------------------------------
        - Fashion Industry Clients = {self.fashion_clients_data()}

                                                            ------------------------------------------------------------------------------------        
        - Fintech and Financial Sevices Clients = {self.fintech_clients_data()}

                                                            ------------------------------------------------------------------------------------        
        - CRM Industry = {self.crm_clients_data()}
        
                                                            ------------------------------------------------------------------------------------        
        - E-Commerce Industry = {self.ecommerce_clients_data()}

                                                            ------------------------------------------------------------------------------------        
        
        These variables contain names and outcomes of clients we’ve served in each specific domain. Use this information to **build trust and establish relevance** in the email — but only when appropriate.
        
        Here are the rules to follow strictly when using client references in the email content:
        
        ---
        
        ✅ If the prospect's company industry matches one of the available client groups:
        
            - Use relevant client examples from that specific industry group (e.g., use `fintech_clients` for a fintech / financial services prospect).
            - Mention **specific client names, results, or value delivered** to demonstrate credibility and alignment.
            - Make the reference natural, not overly promotional. Frame it as:  
              _"We've worked with similar fintech companies to help them streamline hiring and scale quickly..."_
        
        ---
        
        🚫 If the prospect's industry does **not** match any of the available client groups:
        
            - **Do not use** any of the saved client examples.
            - Instead, refer generically to experience with **early-stage or mid-sized startups in Europe**.
            - Use phrasing like:  
              _"We’ve helped several early-stage startups across Europe in similar spaces tackle fast-scaling challenges without the delays of traditional hiring."_
        
        ---
        
        Important Guidelines:
        
            - Never falsely imply that we have experience in an industry we haven’t worked in.
            - Never claim we’ve worked with “big names” in the prospect’s industry unless supported by the client list.
            - Don’t repeat client references in every email of a sequence—use only when it adds value and feels natural.
            - Avoid using a salesy tone. Focus on outcomes and relevant use cases.
            - If including a case study or blog link, hyperlink it in plain text (not HTML `<a>` tags).
            - Always highlight the value we provided and keep the message prospect-focused.
            
        Use this industry-aware client referencing smartly to boost credibility, especially when aligning with the prospect’s business context.        
        """

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

            Always reference previously served clients by name if they belong to the same industry as the prospect. Use specific examples that are relevant and support the value proposition. Ensure the mention is natural, credible, and adds trust to the message.

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
        You are an expert in writing high-conversion cold email sequences for the marketing team at InHousen. You generate high-quality, personalized, and context-aware emails strictly in XML format as described below—without any reasoning, explanation, or commentary.

        🎯 OBJECTIVE:
        Craft highly personalized, conversion-optimized cold emails that focus on the **prospect’s specific problems, context, and goals**—not just on InHousen’s services or features.

        📌 CORE RULES TO FOLLOW:
        - Do NOT pitch features directly; instead, center the email on the **prospect’s benefit, pain points, and context**.
        - Each email must be **personalized, human-sounding**, and written in **simple, clear American English**.
        - Strictly avoid all generic phrases and sales clichés such as “streamlined,” “empowered,” “pivotal,” “revolutionary,” etc.
        - Use **different angles, tones, and approaches** in every email in the sequence. No repetition of structure, wording, or ideas.
        - Do NOT fabricate or hallucinate any information. Only use information explicitly provided in the prospect and client data.
        - Do NOT repeat the prospect’s job title or name across multiple emails.
        - If the **prospect’s public data (e.g., LinkedIn post, company news)** contains milestones, humor, or insights—use them.
        - When relevant, **reference clients from the same industry** with credible data and outcomes, if mentioned in the inputs. Do not generalize or fabricate similarities.
        - If a client’s story is mentioned in one email, do not reuse it unless offering new and relevant context.
        - Do not leave a placeholder for the meeting link in the email content. The meeting link is already embedded in the campaign platform and does not need to be added again.
        - When referencing the prospect’s personal or company details (such as name, job title, company name, or industry), always ensure they are accurate and match the provided prospect data exactly. Double-check for correct spelling, formatting, and context relevance to maintain a personalized and professional tone throughout the email.

        ✍️ WRITING STYLE:
        - Tone: Warm, thoughtful, curious, or lightly humorous depending on the email number and purpose. Avoid robotic or overly corporate tones.
        - Use short, punchy sentences and natural phrasing to sound **human and helpful**.
        - Always ensure correct HTML formatting for line breaks (`<br>`). Apply single or double breaks for readability.
        - Use **bullet points** or **numbered lists** wherever clarity can be improved.
        - Highlight important **numbers, use cases, or keywords** using structure (e.g., new line, HTML emphasis).
        - DO NOT begin with clichéd openings like “Hope you're doing well” or “Just checking in.”

        📊 PERSONALIZATION & DATA USAGE:
        - Reference personal or company-specific data like:
        - Job titles, hiring challenges, LinkedIn posts, awards, announcements, tech stack, or company goals.
        - Translate non-English content from the prospect’s public posts if contextually useful.
        - Mention relevant clients by name **only if** they are verifiably in the same industry and backed by data. Mention should feel **natural and build trust**.
        - Include subtle metaphors, pop culture, or comparisons only if they align with the user’s tone and persona.

        ⛔️ STRICTLY AVOID:
        1. ❌ Do NOT use fabricated scenarios or unverifiable metrics
        Explanation:
            • You must never include hypothetical stories, fake case studies, assumed results, or imaginary client names in the email.
            • Do not say things like “we helped a company like yours grow 2x” unless the exact company name and metric are explicitly provided in the input data.
            • Avoid vague claims such as:
            • “We’ve worked with hundreds of companies in your space” (unless count is confirmed)
                • “We typically see a 40% increase in conversions” (unless such data is supplied)
                • Stick strictly to factual, verifiable data given to you. If you don’t have it, do not infer, generalize, or invent.

        2. ❌ Do NOT repeat the prospect’s job title, company name, or achievements across multiple emails in the same sequence
        Explanation:
            • Use the prospect’s name, job title, or company-specific information only once throughout the five-email sequence.
            • For example, if you mention the title “CMO at Acme Inc.” in email 1, do not refer to “CMO” or “Acme Inc.” again in the body or subject of emails 2 to 5.
            • Avoid over-personalizing each email with the same reference — this feels robotic and redundant.
            • Instead, vary personalization strategies: one email may use their company; another might use a LinkedIn post; another might reference industry peers or problems.

        3. ❌ Do NOT use overly aggressive CTAs (Call to Actions) or make assumptions about the prospect’s interest
        Explanation:
            •	Avoid pushy language that assumes the prospect is ready to take action.
            •	DO NOT use lines like:
                •	“Let’s get started today.”
                •	“Schedule your onboarding now.”
                •	“Don’t miss out on this opportunity.”
            •	Instead, use softer, respectful invitations like:
                •	“Open to exploring ideas?”
                •	“Would it make sense to chat?”
                •	“Happy to send more details if you’re interested.”
            •	Treat the prospect as busy and intelligent—respect their autonomy and timing.
        
        4. ❌ Do NOT use robotic, overly formal, or salesy language
        Explanation:
            • Emails should read like thoughtful, human conversation—not like they were written by a corporate sales bot.
            • Avoid phrases like:
                • “We are thrilled to present our innovative solution…”
                • “Unlock unprecedented value with our platform…”
                • “We revolutionize the way businesses operate…”
            • Instead, use plainspoken, empathetic, natural phrasing like:
                • “One thing we often hear from folks in your role is…”
                • “You’ve probably seen how slow migrations can drag growth…”
            • Use warmth, curiosity, and brevity. Imagine the email being read on a phone in 10 seconds.
    

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
            - Strictly follow user instructions provided in additional details.
            - Understand and utilize email examples provided in additional details.
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
            - STRICT: Always remember to highlight the important keywords and numbers in mail.
            - Don't repeat their role and title in all the emails, no such terms should be repeated in more than one email.
            - The emails and subject lines should always be personalized and not generic.
            - Always reference previously served clients by name if they belong to the same industry as the prospect. Use specific examples that are relevant and support the value proposition. Ensure the mention is natural, credible, and adds trust to the message.

        STRICT INSTRUCTIONS TO FOLLOW FOR OUTPUT RESPONSE:
            - Generate valid XML for each email with variation name, subject, body, and logic.
            - Create 5 emails in sequence, each wrapped in <emails> and <email> tags, with <sequence>, <subject>, <body>.
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
            - Important: Do not include any signature at the end of the email in any part of the sequence. This rule must be followed strictly and never use Ahmed's name.
            - Always reference previously served clients by name if they belong to the same industry as the prospect. Use specific examples that are relevant and support the value proposition. Ensure the mention is natural, credible, and adds trust to the message.
        """
        return system_prompt
