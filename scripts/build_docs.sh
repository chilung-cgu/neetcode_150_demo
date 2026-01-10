#!/bin/bash
set -e

echo "🚀 Starting MkDocs Build Process..."

# Base directory
BASE_DIR=$(pwd)
DOCS_DIR="$BASE_DIR/docs"

# Clean generated directories
echo "🧹 Cleaning previous build artifacts..."
rm -rf "$DOCS_DIR/by-category" "$DOCS_DIR/by-difficulty"
# Note: we don't clean solutions here because the loop below handles overwrite

echo "📂 Syncing solution files to docs/ (Build-time only)..."
# Find all numbered directories (e.g., 01_Arrays..., 18_Bit_...) and copy them to docs/
# We use rsync to avoid re-copying if correct, but cp is fine.
# Note: We must ensure destination exists.
for dir in [0-9][0-9]_*/; do
    if [ -d "$dir" ]; then
        dirname=$(basename "$dir")
        echo "   -> Copying $dirname"
        # Remove existing symlink or dir in docs to ensure clean state
        rm -rf "$DOCS_DIR/$dirname"
        cp -r "$dir" "$DOCS_DIR/"
    fi
done

echo "🔢 Generating Difficulty Index..."
python3 scripts/generate_difficulty_index.py

echo "🏗️ Building Static Site..."
mkdocs build --strict

echo "✅ Build Complete! (Output: site/)"
