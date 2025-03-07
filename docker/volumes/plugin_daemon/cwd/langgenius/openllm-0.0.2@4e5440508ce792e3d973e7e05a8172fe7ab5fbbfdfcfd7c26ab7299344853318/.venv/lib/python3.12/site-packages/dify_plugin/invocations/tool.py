from collections.abc import Generator
from typing import Any

from dify_plugin.core.entities.invocation import InvokeType
from dify_plugin.core.runtime import BackwardsInvocation
from dify_plugin.entities.tool import ToolInvokeMessage, ToolProviderType


class ToolInvocation(BackwardsInvocation[ToolInvokeMessage]):
    def invoke_builtin_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke builtin tool
        """
        return self.invoke(ToolProviderType.BUILT_IN, provider, tool_name, parameters)

    def invoke_workflow_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke workflow tool
        """
        return self.invoke(ToolProviderType.WORKFLOW, provider, tool_name, parameters)

    def invoke_api_tool(
        self, provider: str, tool_name: str, parameters: dict[str, Any]
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke api tool
        """
        return self.invoke(ToolProviderType.API, provider, tool_name, parameters)

    def invoke(
        self,
        provider_type: ToolProviderType,
        provider: str,
        tool_name: str,
        parameters: dict[str, Any],
    ) -> Generator[ToolInvokeMessage, None, None]:
        """
        Invoke tool
        """
        return self._backwards_invoke(
            InvokeType.Tool,
            ToolInvokeMessage,
            {
                "tool_type": provider_type.value,
                "provider": provider,
                "tool": tool_name,
                "tool_parameters": parameters,
            },
        )
