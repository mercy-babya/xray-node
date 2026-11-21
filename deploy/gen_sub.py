#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse, base64, urllib.parse, qrcode, os

def build_vless_link(uuid, domain, port=443, remark="muapi-node"):
    params = {
        "encryption": "none", "flow": "", "security": "none",
        "type": "tcp", "headerType": "none", "sni": domain, "fp": "chrome",
    }
    query = urllib.parse.urlencode(params)
    return f"vless://{uuid}@{domain}:{port}?{query}#{urllib.parse.quote(remark)}"

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--uuid", required=True)
    ap.add_argument("--domain", required=True)
    ap.add_argument("--port", type=int, default=443)
    ap.add_argument("--remark", default="muapi-node")
    args = ap.parse_args()

    link = build_vless_link(args.uuid, args.domain, args.port, args.remark)
    os.makedirs("runs", exist_ok=True)
    with open("runs/subscription.txt", "w", encoding="utf-8") as f:
        f.write(link + "\n")
    b64 = base64.b64encode(link.encode("utf-8")).decode("utf-8")
    with open("runs/subscription-b64", "w", encoding="utf-8") as f:
        f.write(b64 + "\n")
    img = qrcode.make(link)
    img.save("runs/qrcode.png")
    print("=== VLESS 链接 ===\n" + link + "\n")
    print("=== 订阅 base64 ===\n" + b64)

if __name__ == "__main__":
    main()
