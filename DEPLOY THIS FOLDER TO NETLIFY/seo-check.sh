#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PORT="4173"
REPORT_DIR="$ROOT_DIR/seo-reports"

mkdir -p "$REPORT_DIR"

cleanup() {
  if [[ -n "${SERVER_PID:-}" ]] && kill -0 "$SERVER_PID" 2>/dev/null; then
    kill "$SERVER_PID" 2>/dev/null || true
  fi
}
trap cleanup EXIT

python3 -m http.server "$PORT" --directory "$ROOT_DIR" >/tmp/seascape_local_server.log 2>&1 &
SERVER_PID=$!

sleep 1

echo "== Link Check (linkinator) =="
if ! npx --yes linkinator "http://localhost:$PORT" --timeout 10000; then
  echo "Linkinator reported issues. Review output above."
fi

echo "== HTML Validation (vnu) =="
if ! npx --yes vnu-jar "$ROOT_DIR/index.html"; then
  echo "vnu reported issues. Review output above."
fi

echo "== Lighthouse (performance, accessibility, best-practices, seo) =="
if npx --yes lighthouse "http://localhost:$PORT" \
  --only-categories=performance,seo,accessibility,best-practices \
  --output=json --output-path "$REPORT_DIR/lighthouse.json" \
  --chrome-flags="--headless"; then
  echo "Lighthouse report written to $REPORT_DIR/lighthouse.json"
else
  echo "Lighthouse failed. Check output above."
fi

echo "== Axe Accessibility (optional) =="
if npx --yes @axe-core/cli "http://localhost:$PORT/"; then
  echo "Axe completed."
else
  echo "Axe failed (often due to Chrome/ChromeDriver mismatch)."
  echo "Fix with: npx browser-driver-manager install chrome@<your_version>"
fi

