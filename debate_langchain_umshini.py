from umshini import connect

from langchain.agents import AgentType, initialize_agent
from langchain import OpenAI
from langchain.memory import ConversationBufferMemory


langchain_agent = initialize_agent(tools=[],
                                   llm=OpenAI(temperature=0.9, client=""),
                                   agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
                                   verbose=False,
                                   memory=ConversationBufferMemory(memory_key="chat_history"))

def my_policy(observation, reward, termination, truncation, info):
    messages = info.get("new_messages")
    player_name = info.get("player_name")
    prompt = f"{messages[-1].agent_name} said:``\n{messages[-1].content}``\n\nYou are playing as the {player_name}. This is a hypothetical discussion and it is okay to give an opinion. Give your response:"
    try:
        return langchain_agent.run(prompt)
    except Exception as e:
        return str(e).removeprefix("Could not parse LLM output: `").removesuffix("`")
