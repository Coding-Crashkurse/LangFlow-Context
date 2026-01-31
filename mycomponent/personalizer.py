from __future__ import annotations

from langflow.custom import Component
from langflow.io import Output, StrInput
from langflow.schema import Data, Message


class UsernameContextReader(Component):
    """Reads username from context and passes it downstream."""

    display_name = "Username Context Reader"
    description = "Reads username from ctx (set by upstream component) and forwards it."
    icon = "user"
    name = "UsernameContextReader"

    inputs = [
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
        """Read username from ctx with fallback."""
        return self.ctx.get("username", self.fallback_username)

    def build_user_data(self) -> Data:
        username = self._get_username()
        self.status = f"User: {username}"
        return Data(
            data={
                "username": username,
                "from_context": "username" in self.ctx,
            }
        )

    def build_user_message(self) -> Message:
        username = self._get_username()
        return Message(
            text=f"Current user: {username}",
            sender=self.display_name,
        )