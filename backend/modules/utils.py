import os

def load_resumes(resume_folder):
    return [os.path.join(resume_folder, file) for file in os.listdir(resume_folder) if file.endswith((".pdf", ".docx"))]
