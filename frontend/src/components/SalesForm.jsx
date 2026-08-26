import { useState } from 'react';
import axios from 'axios';
import DOMPurify from 'dompurify';
import ProcessLog from './ProcessLog';
import { handleApiError } from '../utils/errorHandler';
import { getApiUrl, getAuthHeaders } from '../utils/api';

const PRESETS = [
    {
        label: '🚀 B2B AI Agent Pitch',
        contact: 'Mikko Virtanen',
        company: 'Nokia',
        email: 'mikko.virtanen@example.com',
        sender: 'Sami Rautanen',
        desc: 'Agent Squad AI: Multi-agent platform that cuts B2B market research and executive briefing prep time by 80% with automated web intel and structured Pydantic reports.'
    },
    {
        label: '💳 FinTech Solution',
        contact: 'Sarah Jenkins',
        company: 'Stripe',
        email: 'sarah.j@example.com',
        sender: 'Sami Rautanen',
        desc: 'Enterprise workflow automation for developer-first fintech platforms, streamlining regulatory compliance briefings.'
    },
    {
        label: '⚡ Cloud Ops Advisory',
        contact: 'Alex Rivera',
        company: 'Wolt',
        email: 'alex.r@example.com',
        sender: 'Sami Rautanen',
        desc: 'Autonomous microservice monitoring and incident report summarization tailored for fast-growing scale-ups.'
    }
];

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

    const applyPreset = (preset) => {
        setContactName(preset.contact);
        setCompanyName(preset.company);
        setProspectEmail(preset.email);
        setSenderName(preset.sender);
        setProductDescription(preset.desc);
    };

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
            onResult({ status: 'success', result: "Email sent successfully via Resend API!" });
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

    if (draftMode && currentDraft) {
        return (
            <div className="form-container form-container-wide">
                <div className="agent-header">
                    <div className="agent-icon">✉️</div>
                    <div className="agent-header-text">
                        <h2>Review Generated Email Draft</h2>
                        <p className="agent-subtitle">Human-in-the-loop review before dispatch</p>
                    </div>
                </div>

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
                        className="submit-button draft-btn draft-btn-send"
                        disabled={loading}
                    >
                        🚀 {loading ? 'Sending...' : 'Approve & Send (Resend)'}
                    </button>

                    <button
                        onClick={() => {
                            const text = currentDraft.html_body.replace(/<[^>]*>?/gm, '');
                            navigator.clipboard.writeText(text);
                            alert("Text content copied to clipboard!");
                        }}
                        className="submit-button draft-btn draft-btn-copy"
                    >
                        📋 Copy Plaintext
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
                    <em>Tip: In production environments, emails are dispatched through authenticated SMTP/Resend with DKIM & SPF validation.</em>
                </p>
            </div>
        );
    }

    // Default Form View
    return (
        <>
            <div className="form-container">
                <div className="agent-header">
                    <div className="agent-icon">💼</div>
                    <div className="agent-header-text">
                        <h2>Sales Outreach Agent</h2>
                        <p className="agent-subtitle">Autonomous B2B personalized email generation & strategic drafting</p>
                    </div>
                </div>

                {/* 1-Click Demo Presets */}
                <div className="presets-section">
                    <div className="presets-label">⚡ 1-Click Quick Demos (Try instantly):</div>
                    <div className="presets-grid">
                        {PRESETS.map((preset, idx) => (
                            <button
                                key={idx}
                                type="button"
                                className="preset-chip"
                                onClick={() => applyPreset(preset)}
                                disabled={loading}
                            >
                                {preset.label}
                            </button>
                        ))}
                    </div>
                </div>

                <form onSubmit={handleGenerateDraft}>
                    <div className="form-group">
                        <label className="form-label">Contact Name</label>
                        <input
                            type="text"
                            value={contactName}
                            onChange={(e) => setContactName(e.target.value)}
                            className="form-input"
                            placeholder="e.g., John Smith"
                            disabled={loading}
                        />
                    </div>

                    <div className="form-group">
                        <label className="form-label">Company Name</label>
                        <input
                            type="text"
                            value={companyName}
                            onChange={(e) => setCompanyName(e.target.value)}
                            className="form-input"
                            placeholder="e.g., Nokia, Microsoft, Stripe"
                            disabled={loading}
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
                            disabled={loading}
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
                            disabled={loading}
                        />
                    </div>

                    <div className="form-group">
                        <label className="form-label">Product / Value Proposition</label>
                        <textarea
                            value={productDescription}
                            onChange={(e) => setProductDescription(e.target.value)}
                            className="form-input"
                            placeholder="What are you offering? (e.g. Multi-agent workflow platform, Enterprise cloud consulting...)"
                            rows="3"
                            required
                            disabled={loading}
                        ></textarea>
                    </div>

                    <button
                        type="submit"
                        className="submit-button"
                        disabled={loading}
                    >
                        {loading ? '⚡ Synthesizing Optimal Pitch...' : '🚀 Generate Draft'}
                    </button>
                </form>
            </div>

            {loading && <ProcessLog agentType="sales" />}
        </>
    );
}
