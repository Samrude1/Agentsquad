import { useState, useEffect } from 'react';

const SALES_LOGS = [
    "Initializing Sales Manager system protocol...",
    "> Loading prospect profile data",
    "> Analyzing company metrics",
    "Target identified. Initiating outreach sequence...",
    "> Drafting: Professional variant [DONE]",
    "> Drafting: Engaging variant [DONE]",
    "> Drafting: Concise variant [DONE]",
    "System: Evaluating optimal strategy...",
    "Selection confirmed. Formatting final output...",
    "> HTML conversion complete",
    "Sequence finished successfully."
];

const RESEARCH_LOGS = [
    "Initializing Deep Research module...",
    "> System: Parsing research topic",
    "> Planner: Generating search strategy",
    "Executing search protocols [Tavily API]...",
    "> Query 1: Validating sources [OK]",
    "> Query 2: Extracting data points [OK]",
    "> Query 3: Cross-referencing entities [OK]",
    "Analysis: 15 sources processed.",
    "Writer: Compiling technical report...",
    "> Synthesizing executive summary",
    "> Formatting markdown structure",
    "> Building section: Introduction",
    "> Building section: Key Findings",
    "> Building section: Analysis",
    "> Building section: Recommendations",
    "> Generating citations and references",
    "> Finalizing document structure",
    "Creating HTML export...",
    "Saving report to disk...",
    "Research task complete."
];

const MEETING_PREP_LOGS = [
    "Initializing Meeting Prep AI [CrewAI]...",
    "> Deploying 3-agent crew",
    "Agent 1: Company Intel Researcher online",
    "> Searching: Company overview",
    "> Searching: Key executives",
    "> Searching: Recent news [6 months]",
    "Intel gathered: 12 sources processed [OK]",
    "Agent 2: Meeting Strategy Analyst online",
    "> Analyzing: Talking points",
    "> Analyzing: Potential opportunities",
    "> Generating: Smart questions",
    "Strategy complete [OK]",
    "Agent 3: Briefing Coordinator online",
    "> Building section: Company Snapshot",
    "> Building section: Key People",
    "> Building section: Recent Developments",
    "> Building section: Talking Points",
    "> Building section: Questions",
    "Finalizing executive briefing...",
    "Saving to Reports folder...",
    "Briefing ready."
];

export default function ProcessLog({ agentType = 'sales' }) {
    const [logs, setLogs] = useState([]);
    const [isBuilding, setIsBuilding] = useState(false);

    const getLogsForType = (type) => {
        switch (type) {
            case 'sales': return SALES_LOGS;
            case 'research': return RESEARCH_LOGS;
            case 'meeting-prep': return MEETING_PREP_LOGS;
            default: return SALES_LOGS;
        }
    };

    const fullLogs = getLogsForType(agentType);

    useEffect(() => {
        let currentIndex = 0;
        const showSpinnerAfter = 5; // Show spinner after this many logs

        const interval = setInterval(() => {
            if (currentIndex < fullLogs.length && currentIndex < showSpinnerAfter) {
                setLogs(prev => [...prev, fullLogs[currentIndex]]);
                currentIndex++;
            } else if (!isBuilding) {
                // Switch to building indicator after a few logs
                setIsBuilding(true);
            }
        }, 600); // Faster log display

        return () => clearInterval(interval);
    }, [agentType]);

    return (
        <div className="process-log-container">
            <div className="process-log-header">
                <span className="terminal-title">AGENT_PROCESS.EXE</span>
                <span className="terminal-status">
                    <span className="status-dot"></span>
                    RUNNING
                </span>
            </div>
            <div className="process-log-content">
                {logs.map((log, index) => (
                    <div key={index} className="log-line">
                        <span className="log-timestamp">[{new Date().toLocaleTimeString('en-US', { hour12: false, hour: '2-digit', minute: '2-digit', second: '2-digit' })}]</span> {log}
                    </div>
                ))}
                {!isBuilding && <div className="log-line blinking-cursor">_</div>}
            </div>

            {isBuilding && (
                <div className="ai-building-indicator">
                    <div className="ai-spinner"></div>
                    <div className="ai-building-text">
                        <span className="loading-dots">AI is building your report</span>
                    </div>
                    <div className="ai-building-subtext">This may take 30-60 seconds</div>
                    <div className="ai-progress-bar">
                        <div className="ai-progress-fill"></div>
                    </div>
                </div>
            )}
        </div>
    );
}

