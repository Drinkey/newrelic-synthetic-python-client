"""
Samples:
newrelic synthetic secure_credential put --key xxxx --value xxxx
newrelic synthetic scripted_browser put \
    --name "USA - Configure/Device Settings (Account Level)" \
    --status enabled \
    --script file://some_path_to_script \
    --locations US_WEST_2, AP_NORTHEAST_1

"""
from newrelic.cli.entrypoint import main

if __name__ == "__main__":
    main()
