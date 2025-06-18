import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/JobList.scss';

const JobList = ({ onSelectJob }) => {
  const [jobs, setJobs] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/jobs')
      .then(res => setJobs(res.data))
      .catch(err => console.error("Error fetching jobs:", err));
  }, []);

  return (
    <div className="job-list">
      <h2>Suggested Jobs</h2>
      <ul>
        {jobs.map((job, index) => (
          <li key={index} onClick={() => onSelectJob(job)} className="job-card">
            <div className="job-title">{job.title}</div>
            <div className="job-company">{job.company}</div>
            <div className="job-location">{job.location}</div>
            <button className="apply-button">View</button>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default JobList;
