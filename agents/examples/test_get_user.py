from agents.agent_core import run_agent
from llms.groq_llm_tools import groq_llm_tools

if __name__ == "__main__":
    response = run_agent(groq_llm_tools, "Show me the profile of user 7")
    print("🧠🧠",response)