#!/bin/sh
set -e

UUID="${UUID:-0c41b6ff-2a96-4f3b-b4b5-4c713fb1505b}"
PORT="${PORT:-8080}"

sed -e "s|{{UUID}}|$UUID|g" -e "s|{{PORT}}|$PORT|g" \
  /etc/xray/config.json.tpl > /etc/xray/config.json

echo "== xray config =="
cat /etc/xray/config.json

exec /usr/local/xray/xray run -config /etc/xray/config.json
