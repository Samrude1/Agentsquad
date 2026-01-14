import { useState } from 'react';
import axios from 'axios';
import ProcessLog from './ProcessLog';
// Removed react-markdown import as we are previewing HTML directly

export default function SalesForm({ onResult }) {
    const [contactName, setContactName] = useState('');
    const [companyName, setCompanyName] = useState('');
    const [prospectEmail, setProspectEmail] = useState('');
    const [senderName, setSenderName] = useState('');
    const [productDescription, setProductDescription] = useState('');
    const [loading, setLoading] = useState(false);

    // Draft State
    const [draftMode, setDraftMode] = useState(false);
    const [currentDraft, setCurrentDraft] = useState(null);

    const handleGenerateDraft = async (e) => {
        e.preventDefault();

        // Validate: at least one of contact or company must be filled
        if (!contactName && !companyName) {
            onResult({ status: 'error', result: 'Please provide either a contact name or company name.' });
            return;
        }

        setLoading(true);
        onResult(null); // Clear previous final results

        try {
            // Note: Updated endpoint to /api/sales/draft
            const response = await axios.post('http://localhost:8000/api/sales/draft', {
                contact_name: contactName || "",
                company_name: companyName || "",
                prospect_email: prospectEmail,
                sender_name: senderName,
                product_description: productDescription
            });

            // The backend returns { status: "success", draft: { status: "draft_created", html_body: "...", ... } }
            if (response.data.draft) {
                setCurrentDraft(response.data.draft);
                setDraftMode(true);
            } else {
                onResult({ status: 'error', result: "Failed to generate draft." });
            }

        } catch (error) {
            onResult({ status: 'error', result: error.message });
        } finally {
            setLoading(false);
        }
    };

    const handleSendEmail = async () => {
        setLoading(true);
        try {
            await axios.post('http://localhost:8000/api/sales/send', {
                to_email: currentDraft.to_email,
                subject: currentDraft.subject,
                html_body: currentDraft.html_body
            });

            // Success! Reset UI
            setDraftMode(false);
            setCurrentDraft(null);
            onResult({ status: 'success', result: "Email sent successfully!" });

        } catch (error) {
            onResult({ status: 'error', result: "Failed to send email: " + error.message });
        } finally {
            setLoading(false);
        }
    };

    const handleDiscard = () => {
        setDraftMode(false);
        setCurrentDraft(null);
    };

    // --- RENDER ---

    if (loading) {
        return (
            <div className="form-container">
                <h2 className="form-title">Processing...</h2>
                <ProcessLog agentType="sales" />
            </div>
        );
    }

    if (draftMode && currentDraft) {
        return (
            <div className="form-container" style={{ maxWidth: '800px' }}>
                <h2 className="form-title">Review Email Draft</h2>

                <div className="draft-preview" style={{
                    border: '1px solid #e5e7eb',
                    padding: '2rem',
                    marginBottom: '1.5rem',
                    background: 'white',
                    borderRadius: '8px'
                }}>
                    <div style={{ marginBottom: '1rem', borderBottom: '1px solid #eee', paddingBottom: '1rem' }}>
                        <p><strong>To:</strong> {currentDraft.to_email}</p>
                        <p><strong>Subject:</strong> {currentDraft.subject}</p>
                    </div>
                    {/* Render HTML content safely */}
                    <div dangerouslySetInnerHTML={{ __html: currentDraft.html_body }} />
                </div>

                <div style={{ display: 'flex', gap: '1rem' }}>
                    <button
                        onClick={handleSendEmail}
                        className="submit-button sales"
                        style={{ backgroundColor: '#16a34a' }} // Green for go
                    >
                        Approve & Send Email
                    </button>
                    <button
                        onClick={handleDiscard}
                        className="submit-button"
                        style={{ backgroundColor: '#dc2626' }} // Red for stop
                    >
                        Discard & Try Again
                    </button>
                </div>
            </div>
        );
    }

    // Default Form View
    return (
        <div className="form-container">
            <h2 className="form-title">Sales Email Generator</h2>

            <form onSubmit={handleGenerateDraft}>
                <div className="form-group">
                    <label className="form-label">Contact Name (optional if company)</label>
                    <input
                        type="text"
                        value={contactName}
                        onChange={(e) => setContactName(e.target.value)}
                        className="form-input"
                        placeholder="e.g., John Smith"
                    />
                </div>

                <div className="form-group">
                    <label className="form-label">Company Name (optional if contact)</label>
                    <input
                        type="text"
                        value={companyName}
                        onChange={(e) => setCompanyName(e.target.value)}
                        className="form-input"
                        placeholder="e.g., Sony, Microsoft"
                    />
                </div>

                <div className="form-group">
                    <label className="form-label">Prospect Email</label>
                    <input
                        type="email"
                        value={prospectEmail}
                        onChange={(e) => setProspectEmail(e.target.value)}
                        className="form-input"
                        placeholder="Enter prospect email"
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

                <div className="form-group">
                    <label className="form-label">Product/Service Description</label>
                    <textarea
                        value={productDescription}
                        onChange={(e) => setProductDescription(e.target.value)}
                        className="form-input"
                        placeholder="What are you offering? (e.g. Premium Coffee Beans, Web Design services...)"
                        rows="4"
                        required
                    ></textarea>
                </div>

                <button
                    type="submit"
                    className="submit-button sales"
                >
                    Generate Draft
                </button>
            </form>
        </div>
    );
}
