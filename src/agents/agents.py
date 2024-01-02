
"""
This module defines an agent for conversational AI using the Haystack library.

The Agent function creates a ConversationalAgent object that utilizes a PromptNode and ConversationSummaryMemory
to generate responses to user queries. The agent can be initialized with a pre-trained model specified by the
`model_uri` parameter and an optional API key specified by the `model_api_key` parameter.

Example usage:
    agent = Agent(model_uri="path/to/model", model_api_key="your_api_key")

Args:
    model_uri (str): The URI or path to the pre-trained model. Defaults to None.
    model_api_key (str): The API key for accessing the pre-trained model. Defaults to None.
    memory (ConversationSummaryMemory): The memory component for storing conversation summaries. Defaults to None.

Returns:
    ConversationalAgent: An instance of the ConversationalAgent class.

Note:
    The `memory` parameter can be customized by passing a ConversationSummaryMemory object. If not provided,
    a default ConversationSummaryMemory object will be created using the prompt node.

"""

from haystack.nodes import PromptNode
from haystack.agents.memory import ConversationSummaryMemory
from haystack.agents.conversational import ConversationalAgent

def call_agent(model_uri, model_api_key, **model_kwargs):

    prompt_node = PromptNode(
        model_name_or_path  = model_uri,
        api_key             = model_api_key,
        max_length          = 256,
        stop_words          = ["Human"],
        model_kwargs        = {}
    )

    summary_memory  = ConversationSummaryMemory(prompt_node)
    #full_memory     = ConversationMemory(prompt_node)
    
    return ConversationalAgent(prompt_node=prompt_node, memory=summary_memory)