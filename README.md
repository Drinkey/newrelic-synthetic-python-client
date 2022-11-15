# newrelic-synthetic-python-client
Python lib to interact with New Relic Synthetic Monitors API using NerdGraph

- [newrelic-synthetic-python-client](#newrelic-synthetic-python-client)
- [Installation](#installation)
  - [Requirements](#requirements)
  - [Install with pip](#install-with-pip)
  - [Development](#development)
- [Usage Example](#usage-example)
  - [Configuration file](#configuration-file)
    - [Configuration file places](#configuration-file-places)
  - [Log level](#log-level)
  - [Secure Credential](#secure-credential)
    - [List secure credentials](#list-secure-credentials)
    - [Update or Create secure credentials](#update-or-create-secure-credentials)
  - [Scripted Browser Monitors](#scripted-browser-monitors)
    - [List scripted browser monitors](#list-scripted-browser-monitors)
    - [Update or Create scripted browser monitor](#update-or-create-scripted-browser-monitor)
  - [CRUD Alert Policy](#crud-alert-policy)
    - [Create Alert Policy](#create-alert-policy)
    - [List Alert Policy](#list-alert-policy)
    - [Update Alert Policy](#update-alert-policy)
    - [Delete Alert Policy](#delete-alert-policy)

# Installation

## Requirements
- Python 3.8 +
- Poetry

## Install with pip


```
pip install newrelic-synthetic-python-client
```


## Development

```
python3 -m venv .venv
source ./venv/bin/activate
```

Verify the poetry is using the virutalenv
```
poetry env info

Virtualenv
Python:         3.8.13
Implementation: CPython
Path:           /Users/the/path/of/newrelic-synthetic-python-client/.venv
Valid:          True

System
Platform: darwin
OS:       posix
Python:   /opt/homebrew/opt/python@3.8/bin/../Frameworks/Python.framework/Versions/3.8
```

Install the dependencies

```
poetry install
```

This will install all the dev/non-dev dependencies.

# Usage Example

## Configuration file

The configuration file contains the information to interact with NewRelic API endpoint, either via RESTFul API or Graphql.

Create a JSON file contains the API Key, the example is like the following
```json
{
    "endpoint": "https://api.newrelic.com/graphql",
    "api_key": "<user_api_key>",
    "account_id": "<numeric_account_id>"
}
```
Let's say the file is located at `$HOME/my-account.json`. To use this file, you need to specify it in the environment variable `NEWRELIC_PYTHON_CLIENT_JSON`
```
export NEWRELIC_PYTHON_CLIENT_JSON=.config/wats-ng-dev.json 
```

### Configuration file places

Search order
1. `$HOME/.newrelic-python-client.json`
2. `$HOME/.config/newrelic-python-client.json`
3. `$CWD/newrelic-python-client.json`
4. Specified by environment `$NEWRELIC_PYTHON_CLIENT_JSON`

The one with larger number will overwrite the one with smaller number.

1. You can put the JSON configuration file to `$HOME/.newrelic-python-client.json` and the configuration will take effect.
2. And then you add a new file in `$HOME/.config/newrelic-python-client.json`, and this one will take effect, `$HOME/.newrelic-python-client.json` will no longer take effect.
3. Then you add a new file in `$CWD/newrelic-python-client.json`, then only this one will take effect.
4. And finally, if you specify the file by environment variable, the environment variable become the only one that take effect.

## Log level

The default log level is set to "INFO". You can change it by updating the environment variable `NR_LOG_LEVEL`.

The possible log levels are
- TRACE
- DEBUG
- INFO
- WARNING
- ERROR

The full list can be found in [loguru document](https://loguru.readthedocs.io/en/stable/api/logger.html) the "The severity levels" section.

The following command set the log level to TRACE and run the script.
```
NR_LOG_LEVEL="TRACE" python src/newrelic.py synthetic secure_credential put --key SPS_ID_TOKEN --value 123  
```


## Secure Credential
### List secure credentials
```
python src/newrelic.py synthetic secure_credential list
```

### Update or Create secure credentials

```
python src/newrelic.py synthetic secure_credential put --key SPS_ID_TOKEN --value 123
```
If the key `SPS_ID_TOKEN` already exist in your secure credentials storage, this command will update the existing credential. If the key does not exist, this command will create a new credential.

## Scripted Browser Monitors

### List scripted browser monitors

```
NR_LOG_LEVEL="TRACE" python src/newrelic.py synthetic scripted_browser list
```

### Update or Create scripted browser monitor

```
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic scripted_browser put --monitor-name "AUTO CREATE" 
```

## CRUD Alert Policy

### Create Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic alert_policy list
```

### List Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic alert_policy add --name 'policy name' --preference="PER_CONDITION"
```

### Update Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic alert_policy update --name "policy name" --preference "PER_POLICY" --policy-id "3715372"
```

### Delete Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic alert_policy delete --policy-id "3715372"
```