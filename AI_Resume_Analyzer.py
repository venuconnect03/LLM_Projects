from google import genai
import os

client = genai.Client(
    api_key=os.getenv("GENAI_API_KEY")
)

with open("Resume.txt", "r", encoding="utf-8") as file:
    resume = file.read()

with open("Job_Description.txt", "r", encoding="utf-8") as file:
    job_description = file.read()


prompt = f"""
You are an AI Resume Analyzer and ATS Optimization Assistant.

Analyze the resume against the job description.

RESUME:
{resume}

JOB DESCRIPTION:
{job_description}

perform the following tasks:

1. Give an estimated resume match score out of 100.
2. Identify skills present the resume that match the job requirements.
3. Identify required skills that are missing or not clearly demonstrated in the resume.
4. Explain the resume's strengths.
5. Explain the areas that need improvement.
6. Suggest five specific resume improvements.
7. Rewrite the career objective to better match the job.

Rules:
- Base your analysis on the supplied resume and the job description.
- Don not invent qualifications, skills, projects, or experience.
- Clearly distinguish skills from the skills that are simply not demonstrated in the resume.
- Explain the results in simple English
- Treat the match score as an estimate, not an official ATS score.
"""

response = client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
)

print("\n===========AI RESUME ANALYSIS===========\n")
print(response.text)
print("\n========================================")
