import React, { useState } from "react";
import ResumeCard from "./components/ResumeCard";

const App = () => {
  const [jobDescription, setJobDescription] = useState("");
  const [skills, setSkills] = useState("");
  const [resumes, setResumes] = useState([]);
  const [loading, setLoading] = useState(false);

  const fetchResumes = async () => {
    if (!jobDescription || !skills) {
      alert("Please enter job description and skills");
      return;
    }

    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:5000/match", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ job_description: jobDescription, skills: skills.split(",") }),
      });

      const data = await response.json();
      setResumes(data);
    } catch (error) {
      console.error("Error fetching resumes:", error);
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>Resume Recommendation System</h1>
      <div className="input-box">
        <textarea
          placeholder="Enter job description..."
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
        />
        <input
          type="text"
          placeholder="Enter skills (comma-separated)..."
          value={skills}
          onChange={(e) => setSkills(e.target.value)}
        />
        <button onClick={fetchResumes} disabled={loading}>
          {loading ? "Searching..." : "Find Best Resumes"}
        </button>
      </div>

      <div className="resume-list">
        {resumes.length > 0 ? (
          resumes.map((resume, index) => <ResumeCard key={index} resume={resume} />)
        ) : (
          <p>No resumes found. Try different keywords.</p>
        )}
      </div>
    </div>
  );
};

export default App;
