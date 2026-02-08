import { useState } from 'react';

const LoginPage = ({ onSuccess }) => {
    const [pin, setPin] = useState('');
    const [error, setError] = useState('');
    const [loading, setLoading] = useState(false);

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setError('');

        try {
            const response = await fetch('http://localhost:8000/api/auth/verify', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ pin }),
            });

            if (response.ok) {
                onSuccess(pin);
                localStorage.setItem('agent_platform_pin', pin);
            } else {
                setError('Invalid PIN code');
                setPin('');
            }
        } catch (err) {
            setError('Connection error. Is backend running?');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="login-container">
            <div className="login-card">
                <div className="login-icon">🛡️</div>
                <h1 className="login-title">Secure Access</h1>
                <p className="login-subtitle">Please enter the platform PIN to continue.</p>

                <form onSubmit={handleSubmit}>
                    <input
                        type="password"
                        className="pin-input"
                        value={pin}
                        onChange={(e) => setPin(e.target.value)}
                        placeholder="••••"
                        maxLength={4}
                        autoFocus
                        disabled={loading}
                    />

                    <button type="submit" className="submit-button" disabled={loading}>
                        {loading ? 'Verifying...' : 'Unlock Platform'}
                    </button>
                </form>

                {error && <div className="error-message" style={{ marginTop: '1rem' }}>{error}</div>}
            </div>
        </div>
    );
};

export default LoginPage;
