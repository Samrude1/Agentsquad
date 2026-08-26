import { useState } from 'react';
import axios from 'axios';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';
import { getApiUrl, getAuthHeaders } from '../utils/api';

const RESEARCH_PRESETS = [
    { label: '🤖 AI Agents in Healthcare', topic: 'Autonomous AI Agents in Healthcare: Clinical trials, diagnostics, and regulatory landscape 2025-2026' },
    { label: '🔋 Solid-State Batteries', topic: 'Solid-state battery commercialization timeline: Key automotive players, chemistry breakthroughs, and scaling challenges' },
    { label: '🛡️ Post-Quantum Cryptography', topic: 'Post-Quantum Cryptography (PQC) standards and enterprise migration strategies for banking' },
    { label: '⚡ Edge Small Language Models', topic: 'Small Language Models (SLMs) running locally on mobile and edge devices: Latency vs accuracy analysis' }
];

export default function ResearchForm({ onResult }) {
    const [topic, setTopic] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        onResult(null);

        try {
            const response = await axios.post(getApiUrl('api/research'), {
                topic: topic
            }, {
                headers: getAuthHeaders()
            });
            onResult(response.data);

        } catch (error) {
            onResult(handleApiError(error));
        } finally {
            setLoading(false);
        }
    };

    return (
        <>
            <div className="form-container">
                <div className="agent-header">
                    <div className="agent-icon">🔬</div>
                    <div className="agent-header-text">
                        <h2>Deep Research Agent</h2>
                        <p className="agent-subtitle">Multi-source web crawler, entity cross-referencing & executive report synthesis</p>
                    </div>
                </div>

                {/* 1-Click Demo Presets */}
                <div className="presets-section">
                    <div className="presets-label">⚡ 1-Click Quick Topics (Try instantly):</div>
                    <div className="presets-grid">
                        {RESEARCH_PRESETS.map((preset, idx) => (
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
                        <label className="form-label">Research Topic or Question</label>
                        <input
                            type="text"
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            className="form-input"
                            placeholder="e.g. AI-driven cybersecurity threats and defensive orchestration 2026..."
                            required
                            disabled={loading}
                        />
                    </div>

                    <button
                        type="submit"
                        className="submit-button"
                        disabled={loading}
                    >
                        {loading ? '🔍 Multi-vector Research in Progress...' : '🚀 Start Deep Research'}
                    </button>
                </form>
            </div>

            {loading && <ProcessLog agentType="research" />}
        </>
    );
}
