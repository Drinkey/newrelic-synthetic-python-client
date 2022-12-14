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
    - [Update scripted browser monitor with account](#update-scripted-browser-monitor-with-account)
  - [CRUD Alert Policy](#crud-alert-policy)
    - [Create Alert Policy](#create-alert-policy)
    - [List Alert Policy](#list-alert-policy)
    - [Update Alert Policy](#update-alert-policy)
    - [Delete Alert Policy](#delete-alert-policy)
  - [CRUD Alert condition](#crud-alert-condition)
    - [Create Alert Condition](#create-alert-condition)
    - [List Alert Condition](#list-alert-condition)
    - [Update Alert Condition](#update-alert-condition)
    - [Delete Alert Condition](#delete-alert-condition)
  - [CRUD Alert Destinations](#crud-alert-destinations)
    - [Create Alert Destinations](#create-alert-destinations)
    - [List Alert Destinations](#list-alert-destinations)
    - [Update Alert Destinations](#update-alert-destinations)
    - [Delete Alert Destinations](#delete-alert-destinations)
  - [CRUD Alert Channels](#crud-alert-channels)
    - [Create Alert Channels](#create-alert-channels)
    - [List Alert Channels](#list-alert-channels)
    - [Update Alert Channels](#update-alert-channels)
    - [Delete Alert Channels](#delete-alert-channels)
  - [CRUD Alert Workflows](#crud-alert-workflows)
    - [Create Alert Workflows](#create-alert-workflows)
    - [List Alert Workflows](#list-alert-workflows)
    - [Update Alert Workflows](#update-alert-workflows)
    - [Delete Alert Workflows](#delete-alert-workflows)
  - [Service Level](#service-level)
    - [Create Synthetic Service Level](#create-synthetic-service-level)
    - [List Synthetic Service Level](#list-synthetic-service-level)
    - [Update Synthetic Service Level](#update-synthetic-service-level)

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

### Update scripted browser monitor with account

```sh
python src/newrelic.py synthetic scripted_browser put --monitor-name "You Scripted Monitor Name"  --script-content "You Script Path" --script-content "You Script Path"
```


## CRUD Alert Policy

### Create Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert policy add --name 'policy name' --preference="PER_CONDITION"
```

### List Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert policy list
```

### Update Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert policy update --name "policy name" --preference "PER_POLICY" --policy-id "3715372"
```

### Delete Alert Policy
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert policy delete --policy-id "3715372"
```

## CRUD Alert condition

### Create Alert Condition
```sh
# Threshold Type Static
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition add  --name "auto_add_1" --policy-id "3719613"

# Threshold Type Baseline
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition add  --name "auto_add_baseline" --policy-id "3717302" --type "baseline" --operator "ABOVE" --threshold "1" --threshold-duration "120"
```

### List Alert Condition
```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition list
```

### Update Alert Condition
```sh
# Threshold Type Static 
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition update --condition-id "28613358" --name "auto_static_update"

# Threshold Type Baseline
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition update  --name "auto_add_baseline_update" --condition-id "28614376" --type "baseline" --operator "ABOVE" --threshold "1" --threshold-duration "120"
```

### Delete Alert Condition

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert condition delete --condition-id "28613141"
```

## CRUD Alert Destinations

### Create Alert Destinations

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert destinations add --name "auto_add_1" --email "test@example.com" 
```

### List Alert Destinations

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert destinations list
```

### Update Alert Destinations

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert destinations update --name "auto_add_update" --destinations-id "You-Destination-ID"
```

### Delete Alert Destinations

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert destinations delete --destinations-id "You-Destination-ID"
```

## CRUD Alert Channels

### Create Alert Channels

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert channels add --name "auto_channel_1" --destination-id "You-Destination-ID"
```

### List Alert Channels

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert channels list
```

### Update Alert Channels

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert channels update --name "auto_channel_update_1" --channel-id "You-Channel-ID"
```

### Delete Alert Channels

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert channels delete  --channel-id  "You-Channel-ID"
```

## CRUD Alert Workflows

### Create Alert Workflows

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert workflows add --name "auto_workflow_add_1" --policy-id "You-Policy-ID" --channel-id  "You-Channel-ID"
```

### List Alert Workflows

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert workflows list --type "EMAIL"
```

### Update Alert Workflows

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert workflows update --name "auto_workflow_update_1" --workflow-id "You-Workflow-ID"
```

### Delete Alert Workflows

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py alert workflows delete  --workflow-id  "You-Workflow-ID"
```

## Service Level

### Create Synthetic Service Level

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic service_level add --monitor-name "You-monitor-name" --name "You-service-level-name"
```

### List Synthetic Service Level

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic service_level list --monitor-name "You-monitor-name"
```

### Update Synthetic Service Level

```sh
NR_LOG_LEVEL="INFO" python src/newrelic.py synthetic service_level update --indicators-id "You-indicators-id" --count "1"
```
