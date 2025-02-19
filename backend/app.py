import os
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from modules.resume_matcher import match_resumes

app = Flask(__name__)
CORS(app)  

RESUME_FOLDER = "resumes"

@app.route("/match", methods=["POST"])
def get_recommendations():
    data = request.json
    job_description = data.get("job_description", "")
    skills = data.get("skills", [])

    if not job_description or not skills:
        return jsonify({"error": "Job description and skills are required"}), 400

    top_resumes = match_resumes(job_description, RESUME_FOLDER)

    # ✅ Ensure skills are always returned in API response
    formatted_resumes = []
    for resume, score in top_resumes:
        details = resume["details"]
        formatted_resumes.append({
            "name": details.get("name", "Unknown"),
            "email": details.get("email", "Not Found"),
            "phone": details.get("phone", "Not Found"),
            "skills": details.get("skills", []),  # Ensure this is always an array
            "filename": resume["filename"],
            "score": round(score, 2)
        })

    return jsonify(formatted_resumes)

@app.route("/resume/<filename>")
# def download_resume(filename):
#     return send_from_directory(RESUME_FOLDER, filename)
def serve_resume(filename):
    resume_folder = "resumes"  
    return send_from_directory(resume_folder, filename, as_attachment=False, mimetype="application/pdf")

if __name__ == "__main__":
    app.run(debug=True)
