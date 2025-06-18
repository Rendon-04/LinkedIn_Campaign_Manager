// CampaignDashboard.jsx
import React, { useState } from 'react';
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

      {selectedJob && message === 'trigger' && (
        <MessageForm job={selectedJob} setMessage={setMessage} />
      )}

      {selectedJob && message && message !== 'trigger' && (
        <MessageComposerModal
          message={message}
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
