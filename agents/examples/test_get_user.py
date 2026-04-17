from agents.agent_core import run_agent
from llms.groq_llm_call import groq_llm_call  # your real LLM

llm = groq_llm_call

response = run_agent(llm, "Show me the profile of user 7")
print(response)
