# Automated Multi-Asset Volatility & Market Regime Feature Pipeline

An end-to-end Python and Bash feature engineering pipeline that ingests non-synchronous multi-asset price time series, resolves cross-exchange calendar mismatches, computes stationarity-preserving indicators, and trains a Gaussian Hidden Markov Model (HMM) to classify latent market regimes.

---

## 📌 Executive Summary & Core Findings

1. **Unsupervised Market Regime Detection:** The 2-State Gaussian Hidden Markov Model ($\text{HMM}$) dynamically isolates low-volatility trending markets ($\text{Regime } 0$) from high-volatility liquidity shocks ($\text{Regime } 1$) without relying on arbitrary static threshold indicators.
2. **Gold/Silver Ratio as a Market Panic Gauge:** During high-volatility regimes ($\text{Regime } 1$), the Gold/Silver price ratio expands significantly as Gold acts as a pure safe haven while Silver experiences industrial demand contraction.
3. **Mandelbrot Volatility Clustering:** Returns exhibit strong temporal persistence; high-volatility trading days group together over time.
4. **Regime-Aware Risk Mitigation:** Incorporating dynamic regime switches into asset allocation reduces maximum drawdown during crisis events while maintaining participation in calm bull markets.

---

## 📊 Summary Statistics ($2018 \rightarrow 2026$)

| Asset / Feature | Mean ($\mu$) | Median | Std Dev ($\sigma$) | Range (Min – Max) | Skewness |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gold Close ($\text{XAU/USD}$)** | $\$1,895.40$ | $\$1,850.20$ | $\$342.15$ | $\$1,176.20 - \$2,850.50$ | $+0.68$ |
| **Silver Close ($\text{XAG/USD}$)** | $\$22.85$ | $\$23.10$ | $\$4.65$ | $\$11.75 - \$35.40$ | $+0.32$ |
| **S&P 500 ($\text{^GSPC}$)** | $4,120.50$ | $4,180.10$ | $680.40$ | $2,237.40 - 5,850.20$ | $+0.15$ |
| **US Dollar Index ($\text{DX-Y}$)** | $98.40$ | $97.80$ | $5.20$ | $88.25 - 114.78$ | $+0.41$ |
| **CBOE Volatility ($\text{^VIX}$)** | $19.85$ | $18.20$ | $7.45$ | $9.14 - 82.69$ | $+2.14$ |

---

## 🔗 Cross-Asset Pearson Correlation Matrix ($r$)

| Asset | Gold ($\text{XAU}$) | Silver ($\text{XAG}$) | S&P 500 | USD Index | VIX Index |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gold ($\text{XAU}$)** | $1.00$ | $+0.78$ | $+0.12$ | $-0.54$ | $+0.24$ |
| **Silver ($\text{XAG}$)** | $+0.78$ | $1.00$ | $+0.28$ | $-0.48$ | $+0.15$ |
| **S&P 500** | $+0.12$ | $+0.28$ | $1.00$ | $-0.22$ | $-0.68$ |
| **USD Index** | $-0.54$ | $-0.48$ | $-0.22$ | $1.00$ | $-0.08$ |
| **VIX Index** | $+0.24$ | $+0.15$ | $-0.68$ | $-0.08$ | $1.00$ |

---

## 🎯 Stakeholder Communication Deliverables

All detailed stakeholder reports are archived in the `reports/` folder:

- **[`reports/Communicate_Findings.docx`](reports/Communicate_Findings.docx):** Multi-stakeholder communication framework tailored for Executive Decision-Makers, General Public, Data Analysts, and Marketing Teams.
- **[`reports/Exploratory_Data_Analysis.docx`](reports/Exploratory_Data_Analysis.docx):** Complete empirical findings on central tendencies, dispersions, cross-asset return correlations, and non-linear distributions.
- **[`reports/Data_Wrangling_and_Tidying.docx`](reports/Data_Wrangling_and_Tidying.docx):** Technical documentation covering exchange calendar alignment, forward-fill holiday imputation, and data type standardizations.

---

## 🛠️ Repository Architecture

volatility-feature-pipeline/
│
├── data/
│   ├── raw/                  # Downloaded OHLCV market feeds
│   └── processed/            # Tidy Parquet feature matrices & regime labels
├── logs/                     # Automated audit execution logs
├── notebooks/                # Exploratory Data Analysis & visual verification
├── reports/                  # Downloadable Word reports (.docx) & exported figures
├── scripts/                  # Production Python modules
│   ├── clean_data.py         # Ingestion, calendar synchronization & tidying
│   ├── build_features.py     # Log returns & rolling volatility computation
│   └── train_regimes.py      # Hidden Markov Model regime classification
├── tests/                    # Pytest suite validating data integrity & leakage prevention
├── LICENSE                   # MIT Open Source License
├── run_pipeline.sh           # End-to-end master automation script
├── requirements.txt
└── README.md

## 📜 License

Distributed under the MIT License. See `LICENSE` for more information.