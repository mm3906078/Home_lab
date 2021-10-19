#!/bin/sh
echo
echo '-----AUTHOR: https://dannyda.com-----'
echo
echo '---Existing locks---'
ls -l /run/lock/qemu-server
rm -f /run/lock/qemu-server/lock-$1.conf
qm unlock $1
echo
echo '---Remaining locks---'
ls -l /run/lock/qemu-server
