#!/usr/bin/env bash

runPylint() {
    echo "Running pylint on all tracked files..."
    pylint $(git ls-files '*.py');  
}

runAutoPep() {
   echo "----------------Running Auto PEP------------------"
    find . -name '*.py' ! -path '*/env/*' -exec autopep8 -v --in-place --aggressive --aggressive '{}' \;
    echo "----------------Auto PEP finished------------------"
}

runReportAndFix() {
    runPylint
    runAutoPep
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


