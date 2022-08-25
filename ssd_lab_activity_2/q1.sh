#!/bin/bash

N=$(cat $1 | wc -l)

if [ $(($N%2)) == 0 ]
then
	M=$(($N/2))
	head -$M $1 | tail -1
else
	M=$(($N/2+1))
	head -$M $1 | tail -1
fi
