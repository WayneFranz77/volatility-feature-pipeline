import pandas as pd
import numpy as np
from pathlib import Path

def main():
    # Load raw data
    raw_path = Path("data/raw/synchronized_close_prices.parquet")
    if not raw_path.exists():
        raise FileNotFoundError(f"Raw data file missing at {raw_path}")

    df = pd.read_parquet(raw_path)

    # Calculate Daily Log Returns
    log_returns = np.log(df / df.shift(1)).add_suffix('_ret')

    # Calculate 21-Day Annualized Rolling Volatility
    rolling_vol = (log_returns.rolling(window=21).std() * np.sqrt(252)).add_suffix('_vol21d')

    # Combine features
    features = pd.concat([df.add_suffix('_close'), log_returns, rolling_vol], axis=1).dropna()

    # Save features to data/processed
    out_dir = Path("data/processed")
    out_dir.mkdir(parents=True, exist_ok=True)
    out_path = out_dir / "volatility_features.parquet"
    
    features.to_parquet(out_path)
    print(f"Features saved successfully to {out_path}")
    print(f"Shape: {features.shape}")
    print(features.tail())

if __name__ == "__main__":
    main()
