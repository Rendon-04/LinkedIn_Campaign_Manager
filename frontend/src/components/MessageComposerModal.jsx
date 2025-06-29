import React from 'react';
import '../styles/MessageComposerModal.scss';

const MessageComposerModal = ({ message, onClose }) => {
  if (!message) return null;

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <div className="modal-header">
          <h3>Generated Outreach Message</h3>
          <button onClick={onClose} className="close-button">×</button>
        </div>

        <textarea
          readOnly
          value={message}
          rows={10}
          style={{
            width: '100%',
            marginBottom: '1rem',
            fontFamily: 'sans-serif',
          }}
        />

        <button
          className="copy-button"
          onClick={() => navigator.clipboard.writeText(message)}
        >
          Copy to Clipboard
        </button>
      </div>
    </div>
  );
};

export default MessageComposerModal;
