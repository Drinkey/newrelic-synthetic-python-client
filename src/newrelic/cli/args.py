from dataclasses import dataclass

from typing import Sequence, Optional, Dict
import argparse
import abc


class Arguments(abc.ABC):
    @abc.abstractmethod
    def to_dict(self) -> Dict:
        pass


@dataclass
class ScriptedBrowserArguments(Arguments):
    """
    Arguments class for the program.
    """

    name: str = ""
    status: Optional[str] = None
    locations: Optional[str] = None
    period: Optional[str] = None
    enable_screenshot: bool = True

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "status": self.status,
            "locations": self.locations.split(",") if self.locations else None,
            "period": self.period,
            "enable_screenshot": self.enable_screenshot
        }


def parse_scripted_browser_args(
    command: Sequence[str]
) -> ScriptedBrowserArguments:
    parser = argparse.ArgumentParser(
        description="newrelic client",
    )
    args = ScriptedBrowserArguments()
    parser.add_argument(
        "--name", type=str, required=True, help="The Synthetic monitor name"
    )
    parser.add_argument(
        "--status",
        type=str,
        default=args.status,
        choices=["enabled", "disabled", "muted"],
        help="Specify the monitor status",
    )
    parser.add_argument(
        "--locations",
        type=str,
        default=args.locations,
        help="Specify the monitor locations, comma separated for multi values",
    )
    parser.add_argument(
        "--period",
        type=str,
        default=args.period,
        help="Specify the monitor period",
    )
    parser.add_argument(
        "--enable-screenshot",
        action="store_true",
        default=args.enable_screenshot,
        help="Whether take screenshot when failure",
    )
    parser.parse_args(args=command, namespace=args)
    return _post_scripted_browser_args_hook(args)


def _post_scripted_browser_args_hook(
    args: ScriptedBrowserArguments
) -> ScriptedBrowserArguments:
    """
    Extra validations for the arguments.
    """
    return args


@dataclass
class SecureCredentialArguments(Arguments):
    key: str = ""
    value: str = ""
    description: str = "NR PYTHON CLIENT AUTO GENERATED"

    def to_dict(self) -> Dict:
        return {
            "key": self.key,
            "value": self.value,
            "description": self.description
        }


def parse_secure_credential_args(
    command: Sequence[str]
) -> SecureCredentialArguments:
    parser = argparse.ArgumentParser(
        description="newrelic client",
    )
    args = SecureCredentialArguments()
    parser.add_argument(
        "--key", type=str, required=True,
        help="The Synthetic secure credential key"
    )
    parser.add_argument(
        "--value", type=str, required=True,
        help="The Synthetic secure credential value"
    )
    parser.add_argument(
        "--description", type=str,
        default=args.description,
        help="The Synthetic secure credential description"
    )
    parser.parse_args(args=command, namespace=args)
    return _post_secure_credential_args_hook(args)


def _post_secure_credential_args_hook(
    args: SecureCredentialArguments
) -> SecureCredentialArguments:
    """
    Extra validations for the arguments.
    """
    return args
