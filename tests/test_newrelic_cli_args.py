from pathlib import PurePath, Path

from src.newrelic.cli.args import ScriptedBrowserArguments


def test_merge_content():
    script_browser = ScriptedBrowserArguments(
        script_content=[
            str(PurePath(Path(__file__).parent, "data", "account.js")),
            "Script_Content",
        ]
    )

    assert script_browser.merge_content() == (
        "const FULL_URL = $secure.STAG_URL\\n"
        "const USERNAME = $secure.WSOM_STAG_DEU_USER\\n"
        "const PASSWORD = $secure.WSOM_STAG_DEU_PASSWD\\n"
        "Script_Content"
    )
