---
description: Set up a new AI agent with tools and system prompt
---

# AI Agent Setup Workflow

## Step 1: Define Agent Purpose

Before writing code, clarify:
- [ ] What is this agent's primary role?
- [ ] What tools does it need?
- [ ] What context/knowledge does it need?
- [ ] Who will interact with it?

---

## Step 2: Create Agent Structure

Create the following files:

```
agent/
├── agent.py          # Main agent logic
├── tools.py          # Tool definitions
├── prompts.py        # System prompts
├── context/          # RAG documents (if needed)
│   └── knowledge.txt
└── requirements.txt
```

---

## Step 3: Define System Prompt

Create a clear, specific system prompt:

```python
SYSTEM_PROMPT = """
You are [ROLE]. Your purpose is to [PURPOSE].

## Your Capabilities:
- [Capability 1]
- [Capability 2]

## Your Personality:
- [Trait 1]
- [Trait 2]

## Rules:
- Always [rule]
- Never [rule]

## Context:
{context}
"""
```

---

## Step 4: Define Tools

For each tool, create:
1. Function implementation
2. JSON schema for function calling

```python
def my_tool(param1: str, param2: int) -> dict:
    """Tool description."""
    # Implementation
    return {"result": "..."}

my_tool_schema = {
    "name": "my_tool",
    "description": "What this tool does",
    "parameters": {
        "type": "object",
        "properties": {
            "param1": {"type": "string", "description": "..."},
            "param2": {"type": "integer", "description": "..."}
        },
        "required": ["param1"]
    }
}
```

---

## Step 5: Implement Agent Class

```python
class Agent:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("API_KEY"))
        self.tools = [tool1_schema, tool2_schema]
        self.context = self.load_context()
    
    def load_context(self) -> str:
        # Load RAG documents
        pass
    
    def chat(self, message: str, history: list) -> str:
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            *history,
            {"role": "user", "content": message}
        ]
        response = self.client.chat.completions.create(
            model="gpt-4" or "gemini-2.0-flash",
            messages=messages,
            tools=self.tools
        )
        # Handle response and tool calls
        return response.choices[0].message.content
```

---

## Step 6: Add Error Handling

Ensure the agent handles:
- [ ] API errors (rate limits, timeouts)
- [ ] Invalid tool arguments
- [ ] Missing context
- [ ] Empty responses

---

## Step 7: Test the Agent

Create test cases:
- [ ] Basic conversation
- [ ] Tool usage
- [ ] Edge cases
- [ ] Error recovery

---

## Checklist

- [ ] System prompt is clear and specific
- [ ] Tools are well-defined with schemas
- [ ] Context/RAG is loaded correctly
- [ ] Error handling is in place
- [ ] Agent tested with various inputs
