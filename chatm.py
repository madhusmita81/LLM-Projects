class PromptEditor:
    def __init__(self):
        guidelines= """Respond with at most two sentences at a time"""
        background_context= """You are a product manager, who is expert in writing product description"""
        persona= """Act a professional writer"""

        self.system_message= f"""{guidelines}
        {background_context}
        {persona}"""

    def add_sys_msg(self):
        messages = [
            {"role": "system", "content": self.system_message}
        ]
        return messages




