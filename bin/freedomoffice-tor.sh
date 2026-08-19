#!/usr/bin/env bash
# FreedomOffice Tor Privacy Proxy Docker Controller
# Launches or stops a pre-configured Tor SOCKS5 proxy & SearXNG Onion integration.

ACTION="${1:-status}"
TOR_CONTAINER="freedomoffice-tor-proxy"
SEARXNG_CONTAINER="freedomoffice-searxng"
SOCKS_PORT="9050"

case "$ACTION" in
    enable|start)
        echo "Enabling Tor Privacy Search Plugin..."
        if docker ps -a --format '{{.Names}}' | grep -q "^${TOR_CONTAINER}$"; then
            docker start "${TOR_CONTAINER}"
        else
            docker run -d \
                --name "${TOR_CONTAINER}" \
                -p "127.0.0.1:${SOCKS_PORT}:9050" \
                --restart unless-stopped \
                peterdavehello/tor-socks-proxy:latest
        fi
        echo "Tor SOCKS5 proxy running at socks5h://127.0.0.1:${SOCKS_PORT}"
        ;;
    disable|stop)
        echo "Disabling Tor Privacy Search Plugin..."
        docker stop "${TOR_CONTAINER}" 2>/dev/null || true
        ;;
    status)
        if docker ps --format '{{.Names}}' | grep -q "^${TOR_CONTAINER}$"; then
            echo "Tor Search Plugin status: ENABLED (socks5h://127.0.0.1:${SOCKS_PORT})"
        else
            echo "Tor Search Plugin status: DISABLED (Requires user to enable)"
        fi
        ;;
    *)
        echo "Usage: $0 {enable|disable|status}"
        exit 1
        ;;
esac
