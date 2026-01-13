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

export default function ProcessLog({ agentType = 'sales' }) {
    const [logs, setLogs] = useState([]);
    const fullLogs = agentType === 'sales' ? SALES_LOGS : RESEARCH_LOGS;

    useEffect(() => {
        let currentIndex = 0;
        const interval = setInterval(() => {
            if (currentIndex < fullLogs.length) {
                setLogs(prev => [...prev, fullLogs[currentIndex]]);
                currentIndex++;
            } else {
                // After logs finish, keep showing "Creating report..." to indicate work is ongoing
                setLogs(prev => [...prev, "> Processing data..."]);
            }
        }, 800);

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
                <div className="log-line blinking-cursor">_</div>
            </div>
        </div>
    );
}
