import autogen
from autogen import UserProxyAgent, ConversableAgent #, config_list_from_json

config_list = [
    {
        "model": "mistral", #the name of your running model
        "base_url": "http://127.0.0.1:11434/v1", #the local address of the api
        "api_key": "sk-111111111111111111111111111111111111111111111111", # just a placeholder
    }
]
llm_config = {"config_list": config_list, "cache_seed": 42}
user_proxy = autogen.UserProxyAgent(
    name="User_proxy",
    system_message="A human admin.",
    code_execution_config={
        "last_n_messages": 2,
        "work_dir": "groupchat",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    human_input_mode="TERMINATE",
    llm_config=llm_config,
)
coder = autogen.AssistantAgent(
    name="Coder",
    llm_config=llm_config,
)
pm = autogen.AssistantAgent(
    name="Product_manager",
    system_message="Creative in software product ideas.",
)
groupchat = autogen.GroupChat(agents=[user_proxy, coder, pm], messages=[], max_round=12)
manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config)
user_proxy.initiate_chat(
    manager, message="Find a latest paper about gpt-4 on arxiv and find its potential applications in software."
)
