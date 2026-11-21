{
  "log": { "loglevel": "warning" },
  "inbounds": [
    {
      "port": {{PORT}},
      "protocol": "vless",
      "settings": {
        "clients": [{ "id": "{{UUID}}" }],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "ws",
        "wsSettings": {
          "path": "/xray"
        },
        "security": "none"
      }
    }
  ],
  "outbounds": [{ "protocol": "freedom", "settings": {} }]
}
