from pathlib import PurePath, Path
import pytest

from src.newrelic.cli.args import ScriptedBrowserArguments


def test_merge_content():
    script_browser = ScriptedBrowserArguments(
        account_file=str(PurePath(Path(__file__).parent, "data", "account.js"))
    )
    assert script_browser.merge_content() == (
        "const FULL_URL = $secure.STAG_URL\\n"
        "const USERNAME = $secure.WSOM_STAG_DEU_USER\\n"
        "const PASSWORD = $secure.WSOM_STAG_DEU_PASSWD\\n"
        "const SCRIPT_NAME"
    )


def test_exception_not_found_account_file():
    script_browser = ScriptedBrowserArguments(
        account_file=str(
            PurePath(Path(__file__).parent, "data", "accounts.js")
        )
    )

    with pytest.raises(FileNotFoundError) as err:
        script_browser.merge_content()
    assert "Not found" in str(err)


def test_exception_not_newline_account_file():
    script_browser = ScriptedBrowserArguments(
        account_file=str(
            PurePath(Path(__file__).parent, "data", "account_no_newline.js")
        )
    )
    with pytest.raises(ValueError) as err:
        script_browser.merge_content()
    assert "The account content must end in " in str(err)
