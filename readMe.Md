### Setup

1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r requirements.txt


### Documentation

## Yfinance calls and responses that are used in the repository
[Relevant YFinance documentation](/documentation/yfinance.md)

We are using Yfinance python module in this repo. In order to understand what calls are being made and the response that are given back, we document it here. Integration tests against YFinance module should be based on what calls we would like our repo to call.

### Linting and Formating
In order to ensure quality of code, it's important to also have a codebase that throughout the project always ensures that all files follow the same coding practices and standards. In this specific project, we are following the PEP8 practices, and utilizes PYLINTT and AUTOPEP in combination with a bash script to reinforce clean code. By default, everytime the main.py script is ran, pylint will run to notify you about possible PEP8 code violations.

You can use the commands:
- sh scripts/format.sh runPylint #Reports PEP8 violations
- sh scripts/format.sh runAutoPep #Fixes PEP8 violations
- sh scripts/format.sh runReportAndFix #Runs the two functions above