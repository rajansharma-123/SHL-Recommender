import unittest

from app import llm


class LLMTests(unittest.TestCase):
    def test_generate_response_without_key_returns_fallback_message(self):
        result = llm.generate_response("system", "user")
        self.assertIn("configured", result.lower())


if __name__ == "__main__":
    unittest.main()
