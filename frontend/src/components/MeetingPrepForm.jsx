import { useState } from 'react';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';

const MeetingPrepForm = ({ onResult }) => {
    const [topic, setTopic] = useState('');
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError(null);
        onResult({ status: 'running', agent: 'Meeting Prep', message: 'Preparing your briefing...' });

        try {
            const response = await fetch('http://localhost:8000/api/meeting-prep', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ topic }),
            });

            const data = await response.json();
            if (data.status === 'success') {
                onResult({
                    status: 'success',
                    type: 'meeting-prep',
                    result: data.result,
                    message: '✅ Briefing ready! Report saved to Reports folder.'
                });
            } else {
                setError(data.detail || 'Failed to prepare briefing');
            }
        } catch (err) {
            const errorResult = handleApiError(err);
            setError(errorResult.result);
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <div className="form-container">
                <div className="agent-header">
                    <div className="agent-icon">📋</div>
                    <div>
                        <h3>Meeting Prep AI</h3>
                        <p className="agent-subtitle">Prepare for important meetings in minutes</p>
                    </div>
                </div>

                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="topic" className="form-label">Company Name</label>
                        <input
                            id="topic"
                            type="text"
                            className="form-input"
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            placeholder="e.g. Nokia, Microsoft, Tesla..."
                            required
                            disabled={loading}
                        />
                    </div>

                    <button type="submit" className="submit-button" disabled={loading}>
                        {loading ? (
                            <span className="loading-content">
                                <span className="pulse-dot"></span>
                                Deploying Crew...
                            </span>
                        ) : (
                            'Prepare Briefing'
                        )}
                    </button>
                </form>

                {error && <div className="error-message">{error}</div>}
            </div>

            {loading && <ProcessLog agentType="meeting-prep" />}
        </>
    );
};

export default MeetingPrepForm;
