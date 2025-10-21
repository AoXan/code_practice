#!/usr/bin/env bash
# Usage: ./scripts/new_competition.sh <slug> <title> <url>
set -e
if [ -z "$1" ]; then
  echo "Usage: $0 <slug> <title> <url>"
  exit 1
fi
SLUG="$1"; TITLE="${2:-<Title>}"; URL="${3:-<URL>}"
DEST="competitions/${SLUG}"
mkdir -p "${DEST}"
rsync -a templates/competition_template/ "${DEST}/"
sed -i.bak "s#<Competition Title>#${TITLE}#g; s#<Kaggle competition URL>#${URL}#g" "${DEST}/README.md"
rm -f "${DEST}/README.md.bak"
echo "Created ${DEST}"
