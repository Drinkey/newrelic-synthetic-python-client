from typing import Dict

from newrelic.nerdgraph.client import NewRelicModule
from newrelic.nerdgraph.synthetic import alert


class AlertPolicy(NewRelicModule):
    def list(self) -> Dict:
        graphql = alert.Policy.list(self.client.account_id)
        return self.client.request(ql=graphql).json()

    def add(
        self,
        preference: str,
        name: str,
        **kwargs,
    ) -> Dict:
        graphql = alert.Policy.add(self.client.account_id, preference, name)
        return self.client.request(ql=graphql).json()

    def delete(
        self,
        policy_id: str,
        **kwargs,
    ) -> Dict:
        graphql = alert.Policy.delete(self.client.account_id, policy_id)
        return self.client.request(ql=graphql).json()

    def update(
        self,
        policy_id: str,
        name: str,
        preference: str,
        **kwargs,
    ) -> Dict:
        graphql = alert.Policy.update(self.client.account_id, policy_id, name, preference)
        return self.client.request(ql=graphql).json()
