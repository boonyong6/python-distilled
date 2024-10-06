import os

path = os.environ["PATH"]
user = os.environ.get("USER")
editor = os.environ.get("EDITOR")
val = os.environ.get("SOME_VAR")

os.environ["NAME"] = "VALUE"
name = os.environ["NAME"]

print(f"{path=}, {user=}, {editor=}, {val=}, {name=}")

# Usage:
#   env SOME_VAR=some_value python _9_5_environment_variables.py
