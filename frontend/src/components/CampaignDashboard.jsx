import React, { useState, useEffect } from 'react';
import axios from 'axios';
import JobList from './JobList';
import JobDetails from './JobDetails';
import MessageForm from './MessageForm';
import StrategyCard from './StrategyCard';
import ActionTimeline from './ActionTimeline';
import MessageFlow from './MessageFlow';
import Insight from './Insight';
import MessageComposerModal from './MessageComposerModal';
import '../styles/CampaignDashboard.scss';

const CampaignDashboard = () => {
  const [selectedJob, setSelectedJob] = useState(null);
  const [message, setMessage] = useState('');
  const [user, setUser] = useState(null);

  useEffect(() => {
    axios
      .get('http://localhost:8000/jobsearch/user/1')
      .then((res) => {
        console.log("✅ Loaded user:", res.data);
        setUser(res.data);
      })
      .catch((err) => console.error("Failed to load user:", err));
  }, []);

  return (
    <div className="dashboard-container">
      <div className="dashboard-top">
        <div>
          <JobList
            onSelectJob={(job) => {
              setSelectedJob(job);
              setMessage('');
            }}
          />
        </div>
        <div className="message-flow-wrapper">
          <MessageFlow job={selectedJob} />
          {selectedJob && (
            <button
              className="button-primary"
              onClick={() => setMessage('trigger')}
            >
              Compose Message
            </button>
          )}
        </div>
      </div>

      {selectedJob && (
        <div className="job-details-wrapper">
          <JobDetails job={selectedJob} />
        </div>
      )}

      {selectedJob && message === 'trigger' && user && (
        <MessageForm job={selectedJob} user={user} setMessage={setMessage} />
      )}

      {selectedJob && message && message !== 'trigger' && user && (
        <MessageComposerModal
          message={message}
          user={user}
          job={selectedJob}
          onClose={() => setMessage('')}
        />
      )}

      <div className="dashboard-grid">
        <StrategyCard />
        <ActionTimeline />
        <Insight />
      </div>
    </div>
  );
};

export default CampaignDashboard;
