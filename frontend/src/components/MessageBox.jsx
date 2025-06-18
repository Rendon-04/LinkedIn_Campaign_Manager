import React from 'react'
import '../styles/MessageBox.scss';

const MessageBox = ({ message }) => {
  if (!message) return null

  return (
    <div className="message-box">
      <h3>Campaign Manager</h3>
      <textarea value={message} readOnly rows={6} />
      <button onClick={() => navigator.clipboard.writeText(message)}>
        Copy Message
      </button>
    </div>
  )
}

export default MessageBox
