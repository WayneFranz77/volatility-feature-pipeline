#!/bin/bash
set -e

echo "=== 1. Ingesting & Synchronizing Data ==="
python scripts/fetch_data.py

echo "=== 2. Building Technical & Volatility Features ==="
python scripts/build_features.py

echo "=== 3. Training Market Regime Model ==="
python scripts/train_regimes.py

echo "=== 4. Running Validation Tests ==="
pytest tests/

echo "=== Pipeline Executed Successfully ==="
