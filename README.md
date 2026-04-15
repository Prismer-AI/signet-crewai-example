# Signet + CrewAI Example

Add cryptographic signing to every CrewAI tool call. Each action gets an Ed25519 signature in a hash-chained audit log.

## Install

```bash
pip install signet-auth crewai crewai-tools
```

## Quick Start

```python
from crewai import Agent, Task, Crew
from signet_auth import SigningAgent
from signet_auth.crewai import install_hooks, uninstall_hooks

# Create Signet identity
signer = SigningAgent.create("crewai-bot", owner="team")
install_hooks(signer)

researcher = Agent(
    role="Researcher",
    goal="Find latest AI news",
    tools=[...],
)

task = Task(description="Research AI agent security trends", agent=researcher)
crew = Crew(agents=[researcher], tasks=[task])
crew.kickoff()  # Every tool call is now signed

uninstall_hooks()
```

## What Happens

1. `install_hooks()` patches CrewAI's tool execution
2. Every tool call gets an Ed25519 signature
3. Receipts are appended to `~/.signet/audit/`
4. `uninstall_hooks()` restores original behavior

## Verify

```bash
signet audit --since 1h
signet audit --verify
```

## Links

- [Signet](https://github.com/Prismer-AI/signet) — Cryptographic action receipts for AI agents
- [PyPI: signet-auth](https://pypi.org/project/signet-auth/)
- [CrewAI](https://www.crewai.com/)
