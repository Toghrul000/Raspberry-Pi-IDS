#!/bin/bash

if [ $# -lt 1 ]; then
    echo "Usage: $0 <command>"
    exit 1
fi

#echo "Timestamp START: $(date)"
echo "Timestamp START: $(date '+%m/%d-%H:%M:%S.%N')"

# Run the command with arguments
"$@"


#echo "Timestamp END: $(date)"
echo "Timestamp END: $(date '+%m/%d-%H:%M:%S.%N')"
