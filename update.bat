python fetch_data_for_today.py

:: https://stackoverflow.com/a/72000317/376454
chcp 65001>nul

git add data/promotion_data.json
git commit -m "🗃️ Update JSON data snapshot"

git add docs/by_*.md
git commit -m "📄 Update Markdown docs"

git push
