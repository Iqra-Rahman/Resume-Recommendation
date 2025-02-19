import os
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from modules.extract_text import extract_text
from modules.extract_details import extract_candidate_details

def match_resumes(job_desc, resume_folder):
    resume_scores = []
    resumes_data = []

    for resume_file in os.listdir(resume_folder):
        resume_path = os.path.join(resume_folder, resume_file)
        text = extract_text(resume_path)
        if text:
            details = extract_candidate_details(text)
            resumes_data.append({"filename": resume_file, "text": text, "details": details})

    # Use TF-IDF for text similarity
    all_texts = [job_desc] + [resume["text"] for resume in resumes_data]
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # Store matching scores
    for i, resume in enumerate(resumes_data):
        resume_scores.append((resume, similarity_scores[i]))

    # Sort by highest match
    resume_scores.sort(key=lambda x: x[1], reverse=True)
    return resume_scores[:3]  # Return top 3 matches
