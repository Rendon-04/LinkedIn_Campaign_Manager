import React, { useState } from 'react';
import axios from 'axios';
import '../styles/MessageForm.scss';

const MessageForm = ({ job, setMessage }) => {

  const user = {
    name: 'Ivan Rendon',
    job_goal: 'Software Engineer',
    industry: 'Tech',
    skills: ['React', 'FastAPI', 'PostgreSQL'],
  };

  const [formData, setFormData] = useState({
    recipient_name: '',
    tone: 'Professional',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    const payload = {
      recipient_name: formData.recipient_name,
      tone: formData.tone,
      user,
      job,
    };

    try {
      const res = await axios.post('http://localhost:8000/generate_message', payload);
      setMessage(res.data.message);
    } catch (err) {
      console.error('Error generating message:', err);
    }
  };

  return (
    <form className="message-form" onSubmit={handleSubmit}>
      <h3>Compose Outreach Message</h3>

      <label>Recipient Name</label>
      <input
        name="recipient_name"
        placeholder="e.g. Alicia Patel"
        value={formData.recipient_name}
        onChange={handleChange}
      />

      <label>Tone</label>
      <select name="tone" value={formData.tone} onChange={handleChange}>
        <option value="Professional">Professional</option>
        <option value="Friendly">Friendly</option>
      </select>

      <button type="submit">Generate Message</button>
    </form>
  );
};

export default MessageForm;

