# Automated Multi-Asset Volatility & Market Regime Feature Pipeline

An end-to-end Python and Bash feature engineering pipeline designed to ingest non-synchronous financial time series, resolve multi-exchange trading calendar mismatches, compute stationarity-preserving features, and model latent market regimes for machine learning models.

## Key Architecture & Features
- **Multi-Asset Ingestion:** Synchronizes Gold, Silver, S&P 500, USD Index, and VIX market data.
- **Stationarity Transformation:** Implements Fractional Differentiation to preserve price memory while achieving stationarity.
- **Regime Modeling:** Utilizes Hidden Markov Models (HMM) and Gaussian Mixture Models (GMM) to classify market volatility states.
- **Leakage Prevention:** Strict walk-forward transformation splits to ensure zero lookahead bias.
- **Production Pipeline:** Shell-script orchestration (`run_pipeline.sh`) with `pytest` suite validation and structured logging.

## Project Structure
```text
volatility-feature-pipeline/
│
├── data/
│   ├── raw/                  # Downloaded OHLCV raw data
│   └── processed/            # Scaled, regime-labeled parquet datasets
├── logs/                     # Pipeline execution logs
├── notebooks/                # Exploratory Data Analysis & visual verification
├── scripts/                  # Core Python modules and orchestration scripts
└── tests/                    # Unit and integration test suite