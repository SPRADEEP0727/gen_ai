import openai
import os
from openai import RateLimitError
from dotenv import load_dotenv
load_dotenv()

class ResumeAnalyzer:
    INDUSTRY_KEYWORDS = {
        "Software": ["Python", "Java", "C++", "Agile", "Git", "REST", "API", "Microservices", "CI/CD", "Docker", "javascript", "React", "Node.js", "SQL", "NoSQL", "Cloud Computing", "AWS", "Azure", "DevOps"],
        "Data Science": ["Data Analysis", "Machine Learning", "Python", "Pandas", "Statistics", "Deep Learning", "TensorFlow", "PyTorch", "Data Visualization", "SQL"],
        "Project Management": ["Project Management", "Scrum", "Agile", "Stakeholder", "Risk", "Kanban", "Budget", "Timeline", "Resource Allocation", "Gantt"],
        "Marketing": ["SEO", "Content", "Campaign", "Analytics", "Brand", "Social Media", "Email Marketing", "PPC", "Market Research", "Copywriting"],
        "Finance": ["Financial Analysis", "Budgeting", "Forecasting", "Excel", "Accounting", "Investment", "Risk Management", "Auditing", "Tax", "Compliance"],
        "Healthcare": ["Patient Care", "Clinical", "EMR", "HIPAA", "Diagnosis", "Treatment", "Healthcare Management", "Medical Records", "Nursing", "Pharmacy"],
        "Education": ["Curriculum", "Instruction", "Assessment", "Classroom Management", "Lesson Planning", "EdTech", "Special Education", "STEM", "Literacy", "Professional Development"],
        "Sales": ["Lead Generation", "CRM", "Negotiation", "Sales Strategy", "Pipeline", "Quota", "B2B", "B2C", "Account Management", "Closing Deals"],
        "Human Resources": ["Recruitment", "Onboarding", "Employee Relations", "Payroll", "Benefits", "Compliance", "Training", "Performance Management", "HRIS", "Talent Acquisition"],
    }

    def __init__(self, industry="Software"):
        self.insights = []
        self.industry = industry

    def analyze_resume(self, resume_text):
        self.insights.clear()
        self.insights.append(self.check_length(resume_text))
        self.insights.append(self.check_keywords(resume_text))
        self.insights.append(self.check_format(resume_text))
        self.insights.append(self.rate_resume(resume_text))
        self.insights.append(self.check_contact_info(resume_text))
        self.insights.append(self.check_action_verbs(resume_text))
        self.insights.append(self.check_achievements(resume_text))
        return self.insights

    def check_length(self, resume_text):
        word_count = len(resume_text.split())
        if word_count < 300:
            return "❌ Resume is too short. Consider adding more details."
        elif word_count > 2000:
            return "❌ Resume is too long. Try to keep it concise."
        return "✅ Resume length is appropriate."

    def check_keywords(self, resume_text):
        keywords = self.INDUSTRY_KEYWORDS.get(self.industry, [])
        resume_text_lower = resume_text.lower()
        found_keywords = [kw for kw in keywords if kw.lower() in resume_text_lower]
        if len(found_keywords) < 3:
            return f"❌ Only found {len(found_keywords)} relevant keywords: {', '.join(found_keywords)}. Consider adding more industry-specific terms."
        return f"✅ Found relevant keywords: {', '.join(found_keywords)}"

    def check_format(self, resume_text):
        if not any(line.strip() for line in resume_text.splitlines() if line.strip()):
            return "❌ Resume appears to be empty or improperly formatted."
        return "✅ Resume format looks good."

    def rate_resume(self, resume_text):
        keywords = self.INDUSTRY_KEYWORDS.get(self.industry, [])
        resume_text_lower = resume_text.lower()
        found_keywords = [kw for kw in keywords if kw.lower() in resume_text_lower]
        rating = min(int((len(found_keywords) / len(keywords)) * 5), 5)
        if rating >= 3:
            return f"✅ Resume rating for {self.industry}: {rating}/5"
        else:
            return f"❌ Resume rating for {self.industry}: {rating}/5"

    def check_contact_info(self, resume_text):
        import re
        email_found = bool(re.search(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", resume_text))
        phone_found = bool(re.search(r"\b\d{10}\b|\(\d{3}\)\s*\d{3}-\d{4}", resume_text))
        if email_found and phone_found:
            return "✅ Contact information (email and phone) found."
        elif email_found:
            return "❌ Email found, but phone number is missing."
        elif phone_found:
            return "❌ Phone number found, but email is missing."
        else:
            return "❌ Contact information missing (email and phone)."

    def check_action_verbs(self, resume_text):
        action_verbs = ["achieved", "managed", "developed", "designed", "implemented", "led", "created", "improved", "increased", "reduced"]
        resume_text_lower = resume_text.lower()
        found_verbs = [verb for verb in action_verbs if verb in resume_text_lower]
        if len(found_verbs) < 2:
            return "❌ Consider using more action verbs to describe your achievements (e.g., achieved, managed, developed)."
        return f"✅ Good use of action verbs: {', '.join(found_verbs)}"

    def check_achievements(self, resume_text):
        if "%" in resume_text or "$" in resume_text or "increased" in resume_text.lower() or "reduced" in resume_text.lower():
            return "✅ Achievements with measurable impact detected."
        return "❌ Consider quantifying your achievements (e.g., increased sales by 20%)."

    def gpt_analysis(self, resume_text, industry):
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = (
            f"Analyze the following resume for a {industry} position. "
            "Provide strengths, weaknesses, and suggestions for improvement:\n\n"
            f"{resume_text}"
        )
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.5,
            )
            return response.choices[0].message.content.strip()
        except RateLimitError:
            return "OpenAI API quota exceeded. Please check your plan and billing details."

    def gpt_analysis(self, resume_text, industry):
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = (
            f"Analyze the following resume for a {industry} position. "
            "Provide strengths, weaknesses, and suggestions for improvement:\n\n"
            f"{resume_text}"
        )
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.5,
            )
            return response.choices[0].message.content.strip()
        except RateLimitError:
            return "OpenAI API quota exceeded. Please check your plan and billing details."