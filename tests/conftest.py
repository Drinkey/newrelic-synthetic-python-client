import pathlib
import json

import pytest

from newrelic.nerdgraph.client import NerdGraphClient, NerdGraphConfig


@pytest.fixture(scope="session")
def nerd_client():
    c = json.loads(pathlib.Path("./nerd.json").read_text())
    config = NerdGraphConfig(
        endpoint=c["endpoint"],
        api_key=c["api_key"],
        account_id=c["account_id"],
    )
    yield NerdGraphClient(config=config)
