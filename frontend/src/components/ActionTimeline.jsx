import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/ActionTimeline.scss';

const ActionTimeline = () => {
  const [steps, setSteps] = useState([]);
  const [actionLog, setActionLog] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/agent/next_steps/1')
      .then(res => setSteps(res.data.steps))
      .catch(err => console.error("Error fetching next steps:", err));
  }, []);

  const handleLog = async () => {
    const newAction = {
      user_id: 1,
      action: 'Messaged a recruiter',
      timestamp: new Date().toISOString()
    };
    await axios.post('http://localhost:8000/agent/actions', newAction);
    setActionLog(prev => [...prev, newAction]);
  };

  return (
    <div className="action-timeline">
      <h3 className="section-title">📌 Next Steps</h3>
      <ul className="step-list">
        {steps.map((step, idx) => (
          <li key={idx} className="step-item">➡️ {step}</li>
        ))}
      </ul>

      <button className="log-button" onClick={handleLog}>
        Log “Messaged a recruiter”
      </button>

      <h4 className="log-title">🕒 Action Log</h4>
      <ul className="log-list">
        {actionLog.map((log, idx) => (
          <li key={idx} className="log-entry">
            <span className="timestamp">{new Date(log.timestamp).toLocaleTimeString()}</span>
            <span className="action">{log.action}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActionTimeline;
