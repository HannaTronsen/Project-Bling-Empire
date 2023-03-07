#!/usr/bin/env bash

runPylint() {
    echo "Running pylint on all tracked files..."
    pylint $(git ls-files '*.py');  
}

runAutopep() {
    echo
    """
    ----------------Running Auto PEP------------------
    """
    find . -name '*.py' -exec autopep8 --in-place '{}' \;
    echo
    """
    ----------------Auto PEP finished------------------
    """
}

runReportAndFix() {
    runPylint
    runAutopep
}


# Check if the function exists (bash specific)
if declare -f "$1" > /dev/null
then
  # call arguments verbatim
  "$@"
else
  # Show a helpful error
  echo "'$1' is not a known function name" >&2
  exit 1
fi


