#!/bin/bash
# consul watches for all services
echo "$1";
PKILL="pkill $1";
CMD="systemctl restart $1";
POUT=$(eval "$PKILL");
OUT=$(eval "$CMD");
