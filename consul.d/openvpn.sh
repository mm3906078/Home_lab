#!/bin/bash
# consul check for openvpn

CMD="ps auxww | grep openvpn | grep -v grep |grep -v ./openvpn.sh "
OUT=$(eval "$CMD")
if [ "$OUT" != "" ]
then
	echo"$OUT"
	exit 0
else
	echo"$OUT"
	exit 3
fi
