import { useState } from 'react';
import axios from 'axios';
import DOMPurify from 'dompurify';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';
import { getApiUrl, getAuthHeaders } from '../utils/api';

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
        onResult(null);

        try {
            const response = await axios.post(getApiUrl('api/sales/draft'), {
                contact_name: contactName || "",
                company_name: companyName || "",
                prospect_email: prospectEmail,
                sender_name: senderName,
                product_description: productDescription
            }, {
                headers: getAuthHeaders()
            });

            if (response.data.draft) {
                setCurrentDraft(response.data.draft);
                setDraftMode(true);
            } else {
                onResult({ status: 'error', result: "Failed to generate draft." });
            }
        } catch (error) {
            onResult(handleApiError(error));
        } finally {
            setLoading(false);
        }
    };

    const handleSendEmail = async () => {
        setLoading(true);
        try {
            await axios.post(getApiUrl('api/sales/send'), {
                to_email: currentDraft.to_email,
                subject: currentDraft.subject,
                html_body: currentDraft.html_body
            }, {
                headers: getAuthHeaders()
            });

            // Success! Reset UI
            setDraftMode(false);
            setCurrentDraft(null);
            onResult({ status: 'success', result: "Email sent successfully!" });
        } catch (error) {
            onResult(handleApiError(error));
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
            <div className="form-container form-container-wide">
                <h2 className="form-title">Review Email Draft</h2>

                <div className="draft-preview">
                    <div className="draft-meta">
                        <p><strong>From:</strong> Agent Squad &lt;info@samirautanen.fi&gt;</p>
                        <p><strong>To:</strong> {currentDraft.to_email}</p>
                        <p><strong>Subject:</strong> {currentDraft.subject}</p>
                    </div>
                    {/* Render HTML content safely */}
                    <div dangerouslySetInnerHTML={{ __html: DOMPurify.sanitize(currentDraft.html_body) }} />
                </div>

                <div className="draft-actions">
                    <button
                        onClick={handleSendEmail}
                        className="submit-button sales draft-btn draft-btn-send"
                    >
                        🚀 Approve & Send
                    </button>

                    <button
                        onClick={() => {
                            const text = currentDraft.html_body.replace(/<[^>]*>?/gm, '');
                            navigator.clipboard.writeText(text);
                            alert("Text content copied to clipboard!");
                        }}
                        className="submit-button draft-btn draft-btn-copy"
                    >
                        📋 Copy Text
                    </button>

                    <a
                        href={`mailto:${currentDraft.to_email}?subject=${encodeURIComponent(currentDraft.subject)}&body=${encodeURIComponent(currentDraft.html_body.replace(/<[^>]*>?/gm, ''))}`}
                        className="submit-button draft-btn draft-btn-mail"
                    >
                        ✉️ Open in Mail App
                    </a>

                    <button
                        onClick={handleDiscard}
                        className="submit-button draft-btn draft-btn-discard"
                    >
                        🗑️ Discard
                    </button>
                </div>

                <p className="draft-hint">
                    <em>Tip: If the automatic send fails (daily limit), use the Copy or Open buttons above.</em>
                </p>
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
