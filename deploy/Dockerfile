FROM alpine:3.20

RUN apk add --no-cache ca-certificates tzdata curl unzip

ARG XRAY_VERSION=1.8.13
RUN mkdir -p /usr/local/xray && \
    curl -L -o /tmp/xray.zip \
      "https://github.com/XTLS/Xray-core/releases/download/v${XRAY_VERSION}/Xray-linux-64.zip" && \
    unzip -o /tmp/xray.zip -d /usr/local/xray && \
    rm -f /tmp/xray.zip && \
    chmod +x /usr/local/xray/xray

RUN mkdir -p /etc/xray /var/log/xray

COPY deploy/config.json.tpl /etc/xray/config.json.tpl

EXPOSE 8080

COPY deploy/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
