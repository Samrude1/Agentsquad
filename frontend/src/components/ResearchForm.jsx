import { useState } from 'react';
import axios from 'axios';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';

export default function ResearchForm({ onResult }) {
    const [topic, setTopic] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        onResult(null);

        try {
            const response = await axios.post('http://localhost:8000/api/research', {
                topic: topic
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
                <h2 className="form-title">Deep Research Agent</h2>

                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label className="form-label">Research Topic</label>
                        <input
                            type="text"
                            value={topic}
                            onChange={(e) => setTopic(e.target.value)}
                            className="form-input research"
                            placeholder="Enter research topic"
                            required
                            disabled={loading}
                        />
                    </div>

                    <button
                        type="submit"
                        className="submit-button research"
                        disabled={loading}
                    >
                        {loading ? 'Research in Progress...' : 'Start Research'}
                    </button>
                </form>
            </div>

            {loading && <ProcessLog agentType="research" />}
        </>
    );
}
