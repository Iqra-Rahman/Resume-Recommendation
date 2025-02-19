import os
from modules.resume_matcher import match_resumes

RESUME_FOLDER = "resumes"

def main():
    print("\n📌 Enter Job Description:")
    job_description = input("> ")

    print("\n🔍 Finding the best matches...")
    top_resumes = match_resumes(job_description, RESUME_FOLDER)

    print("\n✅ Top 3 Recommended Resumes:")
    for i, (resume, score) in enumerate(top_resumes, 1):
        details = resume["details"]
        print(f"\n🔹 {i}. {details['name']} (Match Score: {score:.2f})")
        print(f"   📧 Email: {details['email']}")
        print(f"   📞 Phone: {details['phone']}")
        print(f"   🏆 Matching Skills: {', '.join(details['skills']) if details['skills'] else 'Not Found'}")
        print(f"   📄 Resume File: {resume['filename']}")

if __name__ == "__main__":
    main()
