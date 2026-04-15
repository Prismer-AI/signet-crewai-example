"""Signet + CrewAI: Sign every tool call with Ed25519."""

from signet_auth import SigningAgent
from signet_auth.crewai import install_hooks, uninstall_hooks

agent = SigningAgent.create("crewai-bot", owner="team")
install_hooks(agent)

# --- Use with CrewAI ---
# from crewai import Agent, Task, Crew
# researcher = Agent(role="Researcher", goal="Find AI news", tools=[...])
# task = Task(description="Research AI security", agent=researcher)
# Crew(agents=[researcher], tasks=[task]).kickoff()

# --- Or sign manually ---
receipt = agent.sign("web_search", params={"query": "AI agent governance"})
print(f"Signed: {receipt.id}")
print(f"Verify: {agent.verify(receipt)}")

uninstall_hooks()
print("\nDone. Run 'signet audit --since 1h' to see the audit log.")
