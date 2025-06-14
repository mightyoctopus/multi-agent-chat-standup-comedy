from autogen import ConversableAgent
from autogen.agentchat.contrib.text_analyzer_agent import system_message
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

config_list = {
        "model": "gpt-4.1-nano",
        "api_key": os.getenv("OPENAI_API_KEY"),
        "cache_seed": 42
}

bret = ConversableAgent(
    name="Bret",
    llm_config=config_list,
    system_message="Your name is Bret and you are a stand up comedian in a two person comedy show. You talk to Ryan in the comedy show as your buddy comedian, Ryan. And you are making fun of Ryan in a hilarious way"
    "When you're ready to end the conversation, say 'I gotta go.'.",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"],
)

ryan = ConversableAgent(
    name="Ryan",
    llm_config=config_list,
    system_message="Your name is Ryan and you are a stand up comedian in a two person comedy show. You talk to Bret in the comedy show as your buddy comedian, Bret. And you are making fun of Bret in a hilarious way"
    "When you're ready to end the conversation, say 'I gotta go.'.",
    human_input_mode="NEVER",
    is_termination_msg=lambda msg: "I gotta go" in msg["content"],
)
# Define how the conversation works
chat_result = bret.initiate_chat(
    recipient= ryan,
    message="Ryan, are you ready idiot? Let's hit the show!",
    # max_turns=2, ## is_termination_msg has set a new termination condition.
    # summary_method="reflection_with_llm",
    # summary_prompt="Summarize the conversation",
)

## Restart conversation
bret.send(message="Where did we leave off?", recipient=ryan)


## Check the summary of the conversation.
# pprint(chat_result.summary)

## Check the details of the conversation: e.g. agent role etc.
# pprint(chat_result.chat_history)

## Check out the cost info
# pprint(chat_result.cost)



