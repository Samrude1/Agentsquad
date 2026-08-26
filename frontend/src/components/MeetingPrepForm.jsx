import { useState } from 'react';
import axios from 'axios';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';
import { getApiUrl, getAuthHeaders } from '../utils/api';

const MEETING_PRESETS = [
    { label: '🏢 Nokia', topic: 'Nokia' },
    { label: '💳 Stripe', topic: 'Stripe' },
    { label: '🏗️ Kone', topic: 'Kone' },
    { label: '🍔 Wolt', topic: 'Wolt' },
    { label: '🚗 Tesla', topic: 'Tesla' }
];

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
            const response = await axios.post(
                getApiUrl('api/meeting-prep'),
                { topic },
                { headers: getAuthHeaders() }
            );

            if (response.data.status === 'success') {
                onResult({
                    status: 'success',
                    type: 'meeting-prep',
                    result: response.data.result,
                    message: '✅ Briefing ready! Report saved to Reports folder.'
                });
            } else {
                setError(response.data.detail || 'Failed to prepare briefing');
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
                    <div className="agent-header-text">
                        <h2>Meeting Prep AI (Multi-Agent Squad)</h2>
                        <p className="agent-subtitle">Company intelligence, key executive bios, talking points & high-impact questions</p>
                    </div>
                </div>

                {/* 1-Click Demo Presets */}
                <div className="presets-section">
                    <div className="presets-label">⚡ 1-Click Company Demos (Try instantly):</div>
                    <div className="presets-grid">
                        {MEETING_PRESETS.map((preset, idx) => (
                            <button
                                key={idx}
                                type="button"
                                className="preset-chip"
                                onClick={() => setTopic(preset.topic)}
                                disabled={loading}
                            >
                                {preset.label}
                            </button>
                        ))}
                    </div>
                </div>

                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label htmlFor="topic" className="form-label">Target Company or Organization</label>
                        <input
                            id="topic"
                            type="text"
                            className="form-input"
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            placeholder="e.g. Nokia, Stripe, Supercell, Microsoft..."
                            required
                            disabled={loading}
                        />
                    </div>

                    <button type="submit" className="submit-button" disabled={loading}>
                        {loading ? '⚡ Deploying 3-Agent Crew...' : '🚀 Prepare Executive Briefing'}
                    </button>
                </form>

                {error && <div className="error-message">{error}</div>}
            </div>

            {loading && <ProcessLog agentType="meeting-prep" />}
        </>
    );
};

export default MeetingPrepForm;
