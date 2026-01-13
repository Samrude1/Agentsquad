import { useState } from 'react';
import axios from 'axios';
import ProcessLog from './ProcessLog';

export default function SalesForm({ onResult }) {
    const [prospectName, setProspectName] = useState('');
    const [senderName, setSenderName] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        // Clear previous result
        onResult(null);

        try {
            const response = await axios.post('http://localhost:8000/api/sales', {
                prospect_name: prospectName,
                sender_name: senderName
            });
            onResult(response.data);
        } catch (error) {
            onResult({ status: 'error', result: error.message });
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="form-container">
            <h2 className="form-title">Sales Email Generator</h2>

            {loading ? (
                <ProcessLog agentType="sales" />
            ) : (
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label className="form-label">Prospect Name</label>
                        <input
                            type="text"
                            value={prospectName}
                            onChange={(e) => setProspectName(e.target.value)}
                            className="form-input"
                            placeholder="Enter prospect name"
                            required
                        />
                    </div>

                    <div className="form-group">
                        <label className="form-label">Sender Name</label>
                        <input
                            type="text"
                            value={senderName}
                            onChange={(e) => setSenderName(e.target.value)}
                            className="form-input"
                            placeholder="Enter your name"
                            required
                        />
                    </div>

                    <button
                        type="submit"
                        className="submit-button sales"
                    >
                        Generate Email
                    </button>
                </form>
            )}
        </div>
    );
}
