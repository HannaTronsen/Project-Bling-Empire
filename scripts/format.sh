#!/usr/bin/env bash

runAutoPep() {
   echo "----------------Running Auto PEP------------------"
    find . -name '*.py' ! -path '*/env/*' -exec autopep8 -v --in-place --aggressive --aggressive '{}' \;
    echo "----------------Auto PEP finished------------------"
}

runReportAndFix() {
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


