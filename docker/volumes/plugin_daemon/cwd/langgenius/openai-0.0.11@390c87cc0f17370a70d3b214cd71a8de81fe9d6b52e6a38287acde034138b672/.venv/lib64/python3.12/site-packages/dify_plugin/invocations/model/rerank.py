from dify_plugin.core.entities.invocation import InvokeType
from dify_plugin.core.runtime import BackwardsInvocation
from dify_plugin.entities.model.rerank import RerankModelConfig, RerankResult


class RerankInvocation(BackwardsInvocation[RerankResult]):
    def invoke(self, model_config: RerankModelConfig, docs: list[str], query: str) -> RerankResult:
        """
        Invoke rerank
        """
        for data in self._backwards_invoke(
            InvokeType.Rerank,
            RerankResult,
            {
                **model_config.model_dump(),
                "docs": docs,
                "query": query,
            },
        ):
            return data

        raise Exception("No response from rerank")
