import React from "react";

const ResumeCard = ({ resume }) => {
  if (!resume || !resume.skills) {
    return <p>Error: Resume data is missing</p>;
  }

  return (
    <div className="resume-card">
      <h3>{resume.name || "Unknown Candidate"}</h3>
      {/* <p><strong>Email:</strong> {resume.email || "Not Available"}</p>
      <p><strong>Phone:</strong> {resume.phone || "Not Available"}</p> */}

      {/* Only show email if it's available */}
      {resume.email && <p><strong>Email:</strong> {resume.email}</p>}

      {/* Only show phone if it's available */}
      {resume.phone && <p><strong>Phone:</strong> {resume.phone}</p>}

      <p><strong>Skills:</strong> {resume.skills.length > 0 ? resume.skills.join(", ") : "No skills found"}</p>
      <a href={`http://127.0.0.1:5000/resume/${resume.filename}`} target="_blank" rel="noopener noreferrer">
        View Resume
      </a>
    </div>
  );
};

export default ResumeCard;
