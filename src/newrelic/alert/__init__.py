from newrelic.nerdgraph.client import NerdGraphClient
from newrelic.alert.policy import Policy
from newrelic.alert.condition import Condition


class Alert:
    def __init__(self, client: NerdGraphClient) -> None:
        self.client = client
        self._policy = None
        self._condition = None

    @property
    def policy(self):
        if self._policy is None:
            self._policy = Policy(client=self.client)
        return self._policy

    @property
    def condition(self):
        if self._condition is None:
            self._condition = Condition(client=self.client)
        return self._condition
