import re
import nltk
nltk.download('punkt_tab')
from nltk.tokenize import word_tokenize
from nltk.corpus import words

nltk.download("punkt")
nltk.download("words")

SKILLS_LIST = {"python", "java", "c++", "machine learning", "deep learning", "data analysis",
               "sql", "django", "flask", "javascript", "react", "angular", "html", "css"}

def extract_candidate_details(text):
    # Extract email
    email = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", text)
    email = email[0] if email else "Not Found"

    # Extract phone number
    phone = re.findall(r"\+?\d[\d\s()-]{8,}\d", text)
    phone = phone[0] if phone else "Not Found"

    # Extract name (assume first capitalized words are names)
    tokens = word_tokenize(text)
    english_words = set(words.words())  # Load English words for filtering
    name = " ".join([word for word in tokens[:5] if word.istitle() and word.lower() not in english_words])

    # Extract skills
    found_skills = {skill for skill in SKILLS_LIST if skill.lower() in text.lower()}

    return {"name": name or "Not Found", "email": email, "phone": phone, "skills": list(found_skills)}
