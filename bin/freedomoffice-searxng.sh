#!/usr/bin/env bash
# FreedomOffice SearXNG Meta-Search Engine Docker Controller
# Launches or stops a pre-configured SearXNG meta-search engine instance.

ACTION="${1:-status}"
CONTAINER_NAME="freedomoffice-searxng"
PORT="8080"

case "$ACTION" in
    enable|start)
        echo "Spinning up FreedomOffice SearXNG Search Engine Container..."
        if docker ps -a --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
            docker start "${CONTAINER_NAME}"
        else
            docker run -d \
                --name "${CONTAINER_NAME}" \
                -p "${PORT}:8080" \
                -e "SEARXNG_BASE_URL=http://localhost:${PORT}/" \
                -e "INSTANCE_NAME=FreedomOffice Search Engine" \
                --restart unless-stopped \
                searxng/searxng:latest
        fi
        echo "FreedomOffice SearXNG running at http://localhost:${PORT}/"
        ;;
    disable|stop)
        echo "Stopping FreedomOffice SearXNG Search Engine Container..."
        docker stop "${CONTAINER_NAME}" 2>/dev/null || true
        ;;
    status)
        if docker ps --format '{{.Names}}' | grep -q "^${CONTAINER_NAME}$"; then
            echo "SearXNG status: RUNNING (http://localhost:${PORT}/)"
        else
            echo "SearXNG status: STOPPED"
        fi
        ;;
    *)
        echo "Usage: $0 {enable|disable|status}"
        exit 1
        ;;
esac
