import React from 'react';
import { useUser } from '../context/UserContext';
import '../styles/MessageFlow.scss';

const MessageFlow = ({ job }) => {
  const { user } = useUser();

  return (
    <div className="message-flow-card">
      <h3 className="message-flow-title">Suggested Message Flow</h3>
      {!job ? (
        <p className="message-flow-placeholder">
          Select a job from the left to view messaging suggestions.
        </p>
      ) : (
        <>
          <div className="message-flow-step">
            Hello <strong>{user?.name || 'there'}</strong>, here’s a quick suggestion for reaching out about <strong>{job.title}</strong> at <strong>{job.company}</strong>.
          </div>
          <div className="message-flow-step">
            <strong>Recommended Skills to Highlight:</strong> {user?.skills?.join(', ') || 'N/A'}
          </div>
          <div className="message-flow-step">
            Want help writing a message? Click <strong>Compose Message</strong> to use the Message Generator.
          </div>
        </>
      )}
    </div>
  );
};

export default MessageFlow;
