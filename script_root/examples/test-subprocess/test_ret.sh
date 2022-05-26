#!/bin/bash 

ls 
echo "ls return code is $?"

exit_code=$1
echo "exit code is $1"

exit $1

