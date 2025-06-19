"""
Code to run AI Prompts
"""

import sys, os
from typing import List, Dict
from anthropic import AnthropicBedrock

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from config.singleton import Singleton
from config.configuration_vars import ConfigVars


class ClaudeAIResponse:
    """
    A class to interact with the Claude AI model via Anthropic Bedrock
    and to parse XML-formatted responses.
    """

    @staticmethod
    def get_claude_sonnet35_response(system_prompt, user_prompt):
        """
        Sends a prompt to the Claude 3.5 Sonnet model via Anthropic Bedrock
        and returns the response.

        Args:
            system_prompt (str): The system prompt to guide the AI's behavior.
            user_prompt (str): The user's prompt or question.

        Returns:
            str: The text content of the AI's response.
        """
        anthropic_client = AnthropicBedrock(
            aws_secret_key=ConfigVars().aws_secret_key,
            aws_access_key=ConfigVars().aws_access_key,
            aws_region=ConfigVars().aws_region,
        )

        messages = []
        user = {"role": "user", "content": user_prompt}
        messages.append(user)

        assistant = {
            "role": "assistant",
            "content": "Here is the honest and hallucination free emails in XML as requested.",
        }
        messages.append(assistant)

        response = anthropic_client.messages.create(
            model="anthropic.claude-3-5-sonnet-20240620-v1:0",
            system=system_prompt,
            messages=messages,
            temperature=0,
            top_p=0.5,
            max_tokens=5000,
            timeout=180,
        )

        input_tokens = response.usage.input_tokens
        output_tokens = response.usage.output_tokens
        total_tokens = input_tokens + output_tokens

        # Calculate the cost
        input_cost = (input_tokens / 1_000_000) * 3
        output_cost = (output_tokens / 1_000_000) * 15
        total_cost = input_cost + output_cost
        total_cost = "$ " + str(round(total_cost, 5))

        print(
            {
                "completion_tokens": output_tokens,
                "prompt_tokens": input_tokens,
                "total_tokens": total_tokens,
                "total_cost": total_cost,
            }
        )

        output = response.content[0].text

        return output

    def extract_linkedin_message_details(self, message_content: str) -> Dict[str, str]:
        """
        Extracts specific details (body, logic) from an XML-like string
        representing a single LinkedIn message.

        Args:
            message_content (str): The string content of a single <messages> tag (for LinkedIn).

        Returns:
            Dict[str, str]: A dictionary containing the extracted LinkedIn message details.
        """
        # Extract the content of each nested tag within a LinkedIn message
        body = self.extract_between_tags("body", message_content, strip=True)
        logic = self.extract_between_tags("logic", message_content, strip=True)

        return {"body": body[0] if body else "", "logic": logic[0] if logic else ""}

    def extract_linkedin_messages(self, msg: str) -> List[Dict[str, str]]:
        """
        Extracts all LinkedIn message details from a larger XML-like string
        that contains a <linkedin_messages> block.

        Args:
            msg (str): The full string message, expected to contain a <linkedin_messages> tag,
                       which in turn contains multiple <messages> tags.
        Returns:
            List[Dict[str, str]]: A list of dictionaries, where each dictionary
            represents an extracted LinkedIn message.
        """
        # Extract the content within <linkedin_messages> tag
        linkedin_messages_content = self.extract_between_tags(
            "linkedin_messages", msg, strip=True
        )

        if not linkedin_messages_content:
            return []

        # Extract each <messages> tag within the <linkedin_messages> content
        message_contents = self.extract_between_tags(
            "messages", linkedin_messages_content[0], strip=True
        )

        # Extract the details of each LinkedIn message
        messages = [
            self.extract_linkedin_message_details(message_content)
            for message_content in message_contents
        ]

        return messages
