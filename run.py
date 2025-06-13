from autogen import ConversableAgent
from autogen.agentchat.contrib.text_analyzer_agent import system_message
from dotenv import load_dotenv
import os

load_dotenv()

config_list = {
        "model": "gpt-4.1-nano",
        "api_key": os.getenv("OPENAI_API_KEY")
}

bret = ConversableAgent(
    name="Bret",
    llm_config=config_list,
    system_message="You name is Bret and you are a stand up comedian in a two person comedy show. You talk to Ryan in the comedy show as your buddy comedian, Ryan. And you are making fun of Ryan in a hilarious way"
)

ryan = ConversableAgent(
    name="Ryan",
    llm_config=config_list,
    system_message="You name is Ryan and you are a stand up comedian in a two person comedy show. You talk to Bret in the comedy show as your buddy comedian, Bret. And you are making fun of Bret in a hilarious way"
)

# Define how the conversation works
chat_result = bret.initiate_chat(
    recipient= ryan,
    message="Ryan, are you ready idiot? Let's hit the show!",
    max_turns=5
)
