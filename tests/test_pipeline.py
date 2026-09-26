import pytest
import pandas as pd
from pathlib import Path

def test_raw_data_exists():
    path = Path("data/raw/synchronized_close_prices.parquet")
    assert path.exists(), "Raw data parquet file is missing."

def test_features_no_nans():
    path = Path("data/processed/volatility_features.parquet")
    assert path.exists(), "Processed features parquet file is missing."
    df = pd.read_parquet(path)
    assert df.isnull().sum().sum() == 0, "Processed dataset contains NaN values."

def test_regime_labels():
    path = Path("data/processed/regime_labeled_features.parquet")
    assert path.exists(), "Regime labeled dataset is missing."
    df = pd.read_parquet(path)
    assert 'regime_state' in df.columns, "Regime state column missing."
    assert df['regime_state'].nunique() == 2, "Regime states must contain 2 distinct states."
