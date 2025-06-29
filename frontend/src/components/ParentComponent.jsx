import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MessageForm from './MessageForm';
import MessageComposerModal from './MessageComposerModal';
console.log("ParentComponent mounted");
const ParentComponent = ({ job }) => {
  const [user, setUser] = useState(null);
  const [message, setMessage] = useState('');
  const [modalOpen, setModalOpen] = useState(false);
  

  useEffect(() => {
    axios
      .get('http://localhost:8000/jobsearch/user/1')
      .then((res) => setUser(res.data))
      console.log("Loaded user:", res.data)
      .catch((err) => console.error('Failed to fetch user:', err));
  }, []);

  const handleGenerateMessage = (msg) => {
    setMessage(msg);
    setModalOpen(true);
  };

  if (!user) {
    return <p>Loading user data...</p>;
  }
  console.log("user in ParentComponent:", user);
  console.log("job in ParentComponent:", job);

  return (
    <div>
      <MessageForm
        job={job}
        user={user}
        setMessage={handleGenerateMessage}
      />

      {modalOpen && (
        <MessageComposerModal
          message={message}
          user={user}
          job={job}
          onClose={() => setModalOpen(false)}
        />
      )}
    </div>
  );
};

export default ParentComponent;
