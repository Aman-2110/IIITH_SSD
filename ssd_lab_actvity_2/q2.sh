#!/bin/bash

cat /etc/shells | awk -F "/" '{ if ($2 == "usr") print $NF}'
