import React from 'react';
import '../styles/JobDetails.scss';

const JobDetails = ({ job }) => {
  if (!job) return null;

  return (
    <div className="job-details">
      <h3>{job.title}</h3>
      <p className="company">{job.company} — {job.location}</p>
      <p className="description">{job.description}</p>
    </div>
  );
};

export default JobDetails;
