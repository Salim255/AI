from agents.agent_core import run_agent
from llms.groq_llm import groq_llm_call

llm = groq_llm_call
if __name__ == "__main__":
    response = run_agent(llm, "Show me the profile of user 7")
    print(response)