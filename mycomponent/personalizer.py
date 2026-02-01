from __future__ import annotations

from langflow.custom import Component
from langflow.io import MessageInput, Output, StrInput
from langflow.schema import Data, Message


class UsernameContextReader(Component):
    """Reads username from context and combines it with incoming message."""

    display_name = "Username Context Reader"
    description = "Reads username from ctx and combines it with the incoming message."
    icon = "user"
    name = "UsernameContextReader"

    inputs = [
        MessageInput(
            name="input_message",
            display_name="Input Message",
            info="Incoming message to personalize.",
        ),
        StrInput(
            name="fallback_username",
            display_name="Fallback Username",
            info="Used if no username is found in context.",
            value="unknown",
        ),
    ]

    outputs = [
        Output(
            name="user_data",
            display_name="User Data",
            method="build_user_data",
        ),
        Output(
            name="user_message",
            display_name="User Message",
            method="build_user_message",
        ),
    ]

    def _get_username(self) -> str:
        return self.ctx.get("username", self.fallback_username)

    def build_user_data(self) -> Data:
        username = self._get_username()
        msg_text = self.input_message.text if self.input_message else ""
        self.status = f"User: {username}"
        return Data(
            data={
                "username": username,
                "message": msg_text,
                "from_context": "username" in self.ctx,
            }
        )

    def build_user_message(self) -> Message:
        username = self._get_username()
        msg_text = self.input_message.text if self.input_message else ""
        return Message(
            text=f"[{username}]: {msg_text}",
            sender=username,
        )