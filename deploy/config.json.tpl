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
      "streamSettings": { "network": "tcp", "security": "none" }
    }
  ],
  "outbounds": [{ "protocol": "freedom", "settings": {} }]
}
