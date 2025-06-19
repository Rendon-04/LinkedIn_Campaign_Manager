import React from 'react';
import '../styles/Insight.scss';

const Insight = () => {
  const sampleStats = {
    sent: 20,
    opened: 15,
    responded: 5,
  };

  const conversionRate = ((sampleStats.responded / sampleStats.sent) * 100).toFixed(1);

  return (
    <div className="insight-card">
      <h3 className="insight-title">📊 Agent Insights</h3>
      <div className="insight-metric">
        <span className="label">📤 Messages Sent:</span>
        <span className="value">{sampleStats.sent}</span>
      </div>
      <div className="insight-metric">
        <span className="label">📬 Opened:</span>
        <span className="value">{sampleStats.opened}</span>
      </div>
      <div className="insight-metric">
        <span className="label">💬 Responses:</span>
        <span className="value">{sampleStats.responded}</span>
      </div>
      <div className="insight-metric highlight">
        <span className="label">✅ Conversion Rate:</span>
        <span className="value">{conversionRate}%</span>
      </div>
    </div>
  );
};

export default Insight;
