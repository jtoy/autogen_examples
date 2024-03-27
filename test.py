from autogen import UserProxyAgent, ConversableAgent #, config_list_from_json

#import autogen #start importing the autogen lib


def main():
    # Load LLM inference endpoints from an env variable or a file
    # See https://microsoft.github.io/autogen/docs/FAQ#set-your-api-endpoints
    # and OAI_CONFIG_LIST_sample.
    # For example, if you have created a OAI_CONFIG_LIST file in the current working directory, that file will be used.
    config_list = [
        {
            "model": "mistral", #the name of your running model
            "base_url": "http://127.0.0.1:11434/v1", #the local address of the api
            "api_key": "sk-111111111111111111111111111111111111111111111111", # just a placeholder
        }
    ]

    # Create the agent that uses the LLM.
    assistant = ConversableAgent("agent", llm_config={"config_list": config_list})

    # Create the agent that represents the user in the conversation.
    user_proxy = UserProxyAgent("user", code_execution_config=False)

    # Let the assistant start the conversation.  It will end when the user types exit.
    assistant.initiate_chat(user_proxy, message="How can I help you today?")


if __name__ == "__main__":
    main()
