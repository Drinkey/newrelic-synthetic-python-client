import sys
import os
import pathlib
import json
from typing import Callable, Sequence, List

from newrelic.utils.log import log
from newrelic.nerdgraph.client import NerdGraphClient, NerdGraphConfig
from newrelic.synthetic import Synthetic
import newrelic.cli.args as newrelic_cli


modules = {
        "synthetic": Synthetic
    }


def do_action(func: Callable, args: newrelic_cli.Arguments = None):
    return func() if args is None else func(**args.to_dict())


def get_nr_config_path() -> pathlib.Path:
    """Search the NR configuration JSON file in some places.

    Search order
    1. $HOME/.newrelic-python-client.json
    2. $HOME/.config/newrelic-python-client.json
    3. $CWD/newrelic-python-client.json
    4. Specified by environment $NEWRELIC_PYTHON_CLIENT_JSON

    The higher number will take precedence. If both #1 and #2 exist, #2 will
    take effect. If all #1, #2, #3, #4 exist, #4 will take effect.

    :return: the configuration JSON file path
    :rtype: pathlib.Path
    """
    p = None
    fname = "newrelic-python-client.json"
    home_dir = pathlib.Path().home()
    env_path = os.getenv(
        "NEWRELIC_PYTHON_CLIENT_JSON",
        "NEWRELIC_PYTHON_CLIENT_JSON"  # make sure the value is not exist file
        )
    path_to_test: List[pathlib.Path] = [
        home_dir / f'.{fname}',
        home_dir / ".config" / fname,
        pathlib.Path().cwd() / fname,
        pathlib.Path(env_path),
    ]
    for _p in path_to_test:
        log.debug(f"Check if file exists: {_p}")
        if _p.exists():
            log.debug(f"File {_p} exist, overwrite the previous value {p}")
            p = _p
    assert p is not None, "Unable to find any configuration file"
    log.info(f"Using file {p} as configuration")
    return p


def main(cmd: Sequence[str] = sys.argv):
    assert len(cmd) >= 4, (
        "Command argument not sufficient.\n"
        "Command format:\n"
        "PROG MODULE SUBMODULE ACTION [ARGUMENTS]"
        )

    module_name = cmd[1]
    log.debug(f"{module_name=}")
    assert module_name in modules.keys(), f"{module_name} is not supported"

    module = modules[module_name](
        client=NerdGraphClient(
            config=NerdGraphConfig.from_json_file(
                filepath=get_nr_config_path()
                )
            )
        )
    log.debug(f"{module=}")

    submodule_name = cmd[2]
    log.debug(f"{submodule_name=}")
    submodule = getattr(module, submodule_name, None)
    assert submodule is not None, (
        f"{submodule_name} not supported in {module_name}"
    )
    log.debug(f"{submodule=}")

    action_name = cmd[3]
    log.debug(f"{action_name=}")
    action = getattr(submodule, action_name, None)
    assert action is not None, (
        f"{action_name} is not support in {module_name}:{submodule_name}"
    )
    log.debug(action)

    args_parser = getattr(newrelic_cli, f"parse_{submodule_name}_args", None)
    log.debug(f"{args_parser=}")

    action_args = cmd[4:]
    log.debug(action_args)

    args = args_parser(action_args) if action_args else None

    log.debug(args)

    result = do_action(action, args)
    print(json.dumps(result, indent=4))
