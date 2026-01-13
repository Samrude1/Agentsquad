# Future Plans: Agent Combinations

This document outlines 6 distinct "Personalities" for the **Manager + Deep Researcher** agent architecture. All share the same underlying code structure but serve different workplace domains.

## 1. The Sales Director (Original Plan)
**Use Case:** Highly personalized B2B Outreach.
*   **Manager Role:** "Sales Director". Evaluates drafts, ensures tone, and decides when to send.
*   **Researcher Role:** "Sales Development Rep (SDR)". Researches a prospect's company news, recent funding, and pain points.
*   **Interaction:**
    1.  User: "Send a cold email to Satya Nadella at Microsoft."
    2.  Manager asks Researcher: "Find recent Q3 earnings calls and strategic shifts for Microsoft in 2026."
    3.  Manager directs Copywriter Agent: "Draft an email connecting our product to their new 'AI First' strategy found in the research."
    4.  **Output:** A sent email that feels hand-written and deeply researched.

## 2. The R&D Lead (Science & Tech)
**Use Case:** Accelerating scientific research or technical feasibility studies.
*   **Manager Role:** "Principal Investigator". Defines the hypothesis or technical problem.
*   **Researcher Role:** "Lab Assistant". Deep dives into ArXiv, Google Scholar, and patent databases.
*   **Interaction:**
    1.  User: "Find a biodegradable alternative to plastic packaging."
    2.  Manager asks Researcher: "Find top 3 cited papers on biodegradable polymers from 2024-2025."
    3.  **Output:** A **Grant Proposal** or **Feasibility Report** summarizing the findings.

## 3. The Curriculum Architect (Education)
**Use Case:** Creating up-to-date educational courses or corporate training.
*   **Manager Role:** "Course Designer". Focuses on pedagogy and structure.
*   **Researcher Role:** "Subject Matter Expert". Scours the web for latest docs, tutorials, and changes.
*   **Interaction:**
    1.  User: "Create a module on Agentic AI."
    2.  Manager asks Researcher: "Get me the official documentation for LangChain v0.5."
    3.  **Output:** A complete **Course Syllabus** and **Lecture Notes**.

## 4. The Product Strategist (Product Management)
**Use Case:** Market analysis and competitive intelligence.
*   **Manager Role:** "Product Manager". Focuses on user needs and business value.
*   **Researcher Role:** "Market Analyst". Looks for competitor features and user reviews.
*   **Interaction:**
    1.  User: "Should we build a Voice Mode?"
    2.  Manager asks Researcher: "What are the common complaints about OpenAI's voice mode on Reddit?"
    3.  **Output:** A **Product Requirements Document (PRD)** with a "Competitive Advantage" section.

## 5. The Talent Scout (HR & Recruitment)
**Use Case:** Executive search and candidate analysis.
*   **Manager Role:** "Recruitment Lead". Focuses on culture fit.
*   **Researcher Role:** "Sourcing Specialist". Deep dives into a candidate's public footprint.
*   **Interaction:**
    1.  User: "Prepare for an interview with John Doe."
    2.  Manager asks Researcher: "Find John Doe's open source contributions and recent talks."
    3.  **Output:** A personalized **Interview Script** and **Candidate Profile**.

## 6. The Investment Analyst (Finance)
**Use Case:** Due diligence for investment.
*   **Manager Role:** "Portfolio Manager". Decides on strategy and risk.
*   **Researcher Role:** "Financial Analyst". Reads 10-K reports and earnings calls.
*   **Interaction:**
    1.  User: "Evaluate NVIDIA's robotics strategy."
    2.  Manager asks Researcher: "Find recent partnerships NVIDIA announced regarding robotics."
    3.  **Output:** An **Investment Memo** with a "Buy/Hold/Sell" recommendation.

---

## Shared Architecture
To toggle between these modes, we only need to change the **System Instructions** (Prompts) of the Manager and Researcher agents. The underlying Python code (API, Tool calling, Handoffs) remains identical.
