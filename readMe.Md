# Project Bling Empire 
[Read more about the project](/documentation/vision.md)

## Setup

1. python3 -m venv env
2. source env/bin/activate
3. pip3 install -r requirements.txt


## Documentation

### YahooQuery calls and responses that are used in the repository
[Relevant YahooQuery documentation](/documentation/yquery.md)

We are using YahooQuery python module in this repo. In order to understand what calls are being made and the response that are given back, we document it here. Integration tests against YahooQuery module should be based on what calls we would like our repo to call.

### Linting and Formating
In order to ensure quality of code, it's important to also have a codebase that throughout the project always ensures that all files follow the same coding practices and standards. In this specific project, we are following the PEP8 practices, and currently only utilizes AUTOPEP in combination with a bash script to reinforce clean code. If the source code will be publically available in the future, a more rigid process of ensuring PEP8 code syntax should be put in place.

You can use the commands:
- sh scripts/format.sh runAutoPep #Fixes PEP8 violations