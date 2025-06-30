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
                - Always use client names if we have served clients in the similar industry as that of the prospects.

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
           Craft a concise email that directly addresses the prospect’s key hiring challenges, using insights from the job roles they are actively hiring for. Avoid exaggeration or unsupported claims — only include details that are grounded in the available data.
        	- Focus the email body on the specific challenges they might be facing in filling these roles (e.g., speed, quality, niche skills, scaling needs).
        	- The email subject line should be creative and attention-grabbing, while directly reflecting these pain points — especially those related to difficulty in hiring for the listed positions.
        	- Keep the tone professional but conversational, and include a subtle CTA if relevant.
            - Mention the prospect’s **industry** (e.g., automotive e-commerce, fashion, food delivery). If we have previously served clients in similar industry then use their name and information to build trust.
            - Include the **specific use case** (e.g., platform migration, checkout speed optimization, design refresh).  
            - Reference a **quantifiable result** from a real or simulated past project (e.g., “45% faster checkout”, “0 downtime”, “100% data integrity”).
            - The email should always sound human and natural, don't make it sound like AI. The emails should be very smooth and clear.
            - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.
            
    
        ➤ VALUE ANGLE
            - Lead with pain points or inefficiencies that are common in the prospect’s industry or tech stack (e.g., legacy platforms, sluggish UX, low conversion rates).  
            - Immediately follow with a success story or case study that proves InHousen’s capabilities.
            - In this email always remember to add this point as a Value Proposition:
                - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.
    
        ➤ CLOSING  
            - Mention that Rounak (Business Development Lead) will follow up shortly.  
    
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
        
        4. Clients (Industry-Based Referencing):
        
        - If the prospect’s industry **matches any of the industry-specific client data provided** (e.g., `energy_clients`, `fashion_clients`, `fintech_clients`, etc.), you may:
          - Reference those specific clients by name (if appropriate).
          - Use relevant and verifiable details — such as quantifiable results, context-specific outcomes, or unique use cases — to build trust and relevance.
          - Ensure the mention feels relevant and natural to the reader’s context.
        
        - If there is **no industry match**, follow these strict rules:
          - Do **not** say we’ve worked with "similar companies" or imply industry similarity.
          - Do **not** mention any client name.
          - Instead, state subtly that we’ve worked with clients from **other industries** who faced **similar business challenges**.
            - Example: “We’ve helped clients in different domains address similar scaling challenges using short-term, vetted talent.”
        
        - Under **no circumstance** should you:
          - Fabricate, exaggerate, or generalize client experience to suggest we have served the prospect’s industry when we haven’t.
          - Mention client geography or region (e.g., “in Europe”) unless explicitly provided.
          - Reuse or repeat client names across multiple emails in the sequence unless it adds new and relevant context.
        
        This logic must be strictly followed to ensure relevance, transparency, and trustworthiness.

        === SAMPLE OUTPUT STRUCTURE (Do not copy, for reference only) ===
    
        Subject Line Samples For Reference : [
                                1. Future-Proof Your Website: Meet Inhousen
                                2. Elevate Your Online Store Experience
                                3. Ready to Upgrade Your Website Performance?
                                4. From Lightspeed to Shopify - Seamlessly with Inhousen
                                ]

        Email just for reference and never to be copied.

        Hi [First Name],
        
            I'm Ahmed, Co-founder of Inhousen — a Dutch-based tech solutions company. We specialize in helping businesses like yours build and optimize their digital storefronts. Whether it's maintaining your current Lightspeed website or migrating seamlessly to Shopify, we ensure high performance, better UX, and scalable growth.
            
            Our team guarantees a smooth transition with minimal downtime and full design & data integrity.
            
            We've also attached our company portfolio—please do take a look to learn more about our work.
            
            Would love to show you how we can future-proof your online presence.
            
            Also, my colleague Rounak, who leads our business development efforts, will be reaching out to you shortly to assist with any immediate needs or questions.

        === SUBJECT LINE SUGGESTIONS ===  
            1. Future-Proof Your Website: Meet Inhousen
            2. Elevate Your Online Store Experience
            3. Ready to Upgrade Your Website Performance?
            4. From Lightspeed to Shopify - Seamlessly with Inhousen

        === FINAL NOTES ===
            - As a value addition, can you add this point in the email.
                - Access top 1% tech talent in Europe — starting at just €22/hr*. One of the most competitive rates in the region.
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

        Email just for reference and never to be copied.

        Hi [First Name],
        
        Let me share recent examples on how we helped an automotive e-commerce retailer migrate to Shopify in just 30 days with remarkable results:
        
        Zero downtime during transition
        100% data integrity maintained
        Custom parts search functionality
        45% faster checkout completion
        
        See the Full Case Study →
        
        Our Business Developer, Rounak, will reach out this week to discuss how we can deliver similar results for your business.
        
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

        Email just for reference and never to be copied.

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

        Email just for reference and never to be copied.
 
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
            - Use bullets points and proper line spaces for readability.
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

        Email just for reference and never to be copied.
    
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
