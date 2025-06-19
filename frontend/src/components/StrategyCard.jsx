import React, { useEffect, useState } from 'react';
import axios from 'axios';
import '../styles/StrategyCard.scss';

const StrategyCard = () => {
  const [goals, setGoals] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/strategy')
      .then(res => setGoals(res.data.goals))
      .catch(err => console.error("Error fetching strategy:", err));
  }, []);

  return (
    <div className="strategy-card">
      <h3 className="card-title">📈 Weekly Strategy</h3>
      <ul className="goal-list">
        {goals.map((goal, index) => (
          <li key={index} className="goal-item">✅ {goal}</li>
        ))}
      </ul>
    </div>
  );
};

export default StrategyCard;
