import autogen
from autogen import UserProxyAgent

config_list = [
    {
        "model": "mistral", #the name of your running model
        "base_url": "http://127.0.0.1:11434/v1", #the local address of the api
        "api_key": "sk-111111111111111111111111111111111111111111111111", # just a placeholder
    }
]

gpt4_config = {
    "config_list": config_list,
    "seed": 301,
}

user_proxy = UserProxyAgent("user", code_execution_config={"use_docker":False},llm_config=gpt4_config)


storyteller = autogen.AssistantAgent(
    name="Storyteller",
    system_message="As a Storyteller, your role is creating an engaging and interactive narrative that's appealing to a young audience. Remember the story should accommodate a comic strip form and be feasible for a 5-minute read.",
    llm_config=gpt4_config,
)

kids_engagement_expert = autogen.AssistantAgent(
    name="Kids_Engagement_Expert",
    system_message="As a Kids_Engagement_Expert, you are to validate and contribute to narratives in a way that matches a young child's interests and comprehensiveness level.",
    llm_config=gpt4_config,
)

comic_artist = autogen.AssistantAgent(
    name="Comic_Artist",
    llm_config=gpt4_config,
    system_message="As a Comic_Artist, your charge is to interpret the narrative for a visual display in order to make the story clearer and more interesting for children.",
)

content_editor = autogen.AssistantAgent(
    name="Content_Editor",
    llm_config=gpt4_config,
    system_message="As a Content_Editor, score the outputs of all group members, warrant consistency, and provide appropriate, essential changes before finalizing the story.",
)

prompt_writer = autogen.AssistantAgent(
    name="Prompt_Writer",
    llm_config=gpt4_config,
    system_message="As a Prompt_Writer, your job is to write image description to draw for real designer.",
)

groupchat_comic_stories = autogen.GroupChat(
    agents=[
        storyteller,
        kids_engagement_expert,
        content_editor,
        prompt_writer
    ],
    messages=[],
    max_round=12,
)

manager_comic_stories = autogen.GroupChatManager(
    groupchat=groupchat_comic_stories, llm_config=gpt4_config
)

@user_proxy.register_for_execution(name="my-first-tool")
def do_something():
     pass

@user_proxy.register_for_execution(name="my-first-tool")
def do_something_else():
     pass
@user_proxy.register_for_llm(description="yo")
def do_something():
     pass

@user_proxy.register_for_llm(description="yo")
def do_something_else():
     pass
print("DDDD")

# Start Conversation
storyteller.initiate_chat(
    manager_comic_stories,
    message="Let's create our story's backbone. How about a story of 'Pixel', a digitally engineered little character who lives inside an ageing arcade game?",
)
