# 📉 Gaussian Risk Calculator

A professional, lightweight Python toolkit for calculating **parametric Value at Risk (VaR)** and **Expected Shortfall (ES)** to facilitate rapid portfolio risk assessment.

---

## Overview

This tool provides a command-line interface to estimate potential portfolio losses under a Gaussian distribution assumption. It is designed for financial analysts and researchers who need a quick, reliable method for sensitivity analysis and risk screening.

---

## Features

- **Parametric VaR** — Estimates maximum expected loss at a given confidence level
- **Expected Shortfall (ES)** — Computes the average loss in the tail beyond the VaR threshold
- **Configurable Inputs** — Mean return, volatility (σ), confidence level, and time horizon
- **Square-Root-of-Time Scaling** — Applies the standard σ_h = σ × √T rule for multi-day horizons
- **Zero Dependencies Beyond NumPy/SciPy** — Minimal, portable, and easy to integrate

---

## Prerequisites

Ensure you have Python 3.x installed, then install the required libraries:

```bash
pip install numpy scipy
```

---

## Usage

Run the calculator directly from your terminal:

```bash
python main.py
```

You will be prompted to enter the following inputs:

| Input | Description | Example |
|---|---|---|
| Mean Return | Expected daily return of the portfolio | `0.001` |
| Volatility (σ) | Daily standard deviation of returns | `0.02` |
| Confidence Level | Probability threshold (e.g. 95%, 99%) | `0.95` |
| Time Horizon | Holding period in days | `10` |

---

## Example Output

```
Results:
  Gaussian VaR:  2.45%
  Gaussian ES:   3.12%
```

---

## Mathematical Background

This tool uses the **Parametric (Gaussian) Method**, which models portfolio returns as normally distributed.

**Value at Risk (VaR)**

$$\text{VaR}_{\alpha, T} = -\left(\mu \cdot T - \sigma \cdot \sqrt{T} \cdot z_{\alpha}\right)$$

**Expected Shortfall (ES)**

$$\text{ES}_{\alpha, T} = -\mu \cdot T + \sigma \cdot \sqrt{T} \cdot \frac{\phi(z_{\alpha})}{1 - \alpha}$$

Where $z_{\alpha}$ is the quantile of the standard normal distribution at confidence level $\alpha$, and $\phi$ is the standard normal PDF.

---

## ⚠️ Limitations & Disclaimer

> This tool is intended for **exploratory analysis and preliminary risk screening only**. It is **not suitable** for regulatory capital reporting or high-stakes financial decision-making.

| Limitation | Detail |
|---|---|
| **Normality Assumption** | Returns are assumed normally distributed. Fat-tail risks and extreme market events may be underestimated. |
| **Volatility Scaling** | Applies the square-root-of-time rule, which assumes i.i.d. returns. Not valid under volatility clustering or autocorrelation. |
| **Static Parameters** | Mean and volatility are treated as constant over the horizon. |

---

## Project Structure

```
gaussian-risk-calculator/
│
├── main.py          # Entry point — CLI prompts and output
├── README.md        # Project documentation
└── requirements.txt # Python dependencies
```

---

## About

Developed by **Mateo Veltri** as part of the [Veltri Capital](https://github.com/) quantitative research toolkit.

This calculator bridges the gap between raw market data and actionable risk metrics, providing a foundational approach to assessing tail risk in portfolio analysis.

---

## License

This project is licensed under the [MIT License](LICENSE).
