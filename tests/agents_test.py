import unittest
from unittest.mock import patch
from src.agents.agents import prompt_node, summary_memory, agent_basic

class TestAgents(unittest.TestCase):
    @patch('os.getenv')
    def test_prompt_node(self, mock_getenv):
        mock_getenv.return_value = 'test_api_key'
        self.assertIsNotNone(prompt_node)

    def test_summary_memory(self):
        self.assertIsNotNone(summary_memory)

    def test_agent_basic(self):
        self.assertIsNotNone(agent_basic)

if __name__ == '__main__':
    unittest.main()