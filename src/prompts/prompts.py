"""
This module maintains a modular format for using prompts.

Prompts for the various Agent roles as defined by the developer will be called down from a database.
This was designed intentionally for maintainability and scalability. Instead of pushing new code when
a new prompt is defined or modified, instead the database will be updated for quicker reference.

** Will this cause latency issues and additional costs? Because we're updating prompts too often?
** Look into ways to cache or intermittently store prompts.

"""

from haystack.nodes import PromptTemplate

title_generator = PromptTemplate(
    prompt="Provide a short, descriptive title for the given piece of news. News: {documents}; Title:"
)
