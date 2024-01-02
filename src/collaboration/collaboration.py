"""
This creates a colloborative effort between two agents that allow for an iterative development
of a response to a query.

Returns:
    _type_: _description_

"""


class CollaborationWrapper:
    def __init__(self):
        self.agent1 = CallAgent()
        self.agent2 = CallAgent()

    def navigate(self, input_text, max_iterations=8, termination='Final Response'):
        response = input_text
        iterations = 0
        while response != termination and iterations < max_iterations:
            response = self.agent1.generate_response(response)
            if response == termination:
                break
            response = self.agent2.generate_response(response)
            iterations += 1
        return response
