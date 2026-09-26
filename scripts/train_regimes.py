import pandas as pd
import numpy as np
from pathlib import Path
from hmmlearn.hmm import GaussianHMM

def main():
    features_path = Path("data/processed/volatility_features.parquet")
    if not features_path.exists():
        raise FileNotFoundError(f"Missing dataset at {features_path}")

    df = pd.read_parquet(features_path)

    # Select returns and volatility columns for fitting
    feature_cols = [c for c in df.columns if '_ret' in c or '_vol21d' in c]
    X = df[feature_cols].values

    # Fit a 2-state Gaussian HMM
    model = GaussianHMM(n_components=2, covariance_type="full", random_state=42, n_iter=100)
    model.fit(X)

    # Predict hidden states (0 = Low Vol, 1 = High Vol / Regime Shift)
    df['regime_state'] = model.predict(X)

    # Output dataset with regime labels
    output_path = Path("data/processed/regime_labeled_features.parquet")
    df.to_parquet(output_path)
    print(f"Regime model trained successfully! Processed dataset saved to {output_path}")
    print(df[['regime_state']].value_counts())

if __name__ == "__main__":
    main()
