# Case Studies in Financial Risk Modeling and Stock Price Simulation

This repository presents two case studies demonstrating how we can use Monte Carlo simulations, portfolio optimization, and Geometric Brownian Motion (GBM) to model and manage financial risk, specifically through Value at Risk (VaR), and to forecast stock price behavior.

## Overview
These case studies aim to:

1. Assess investment risk using different VaR methods (Monte Carlo, Parametric, Historical)
2. Simulate stock price evolution using GBM
3. Compare and visualize outcomes using both statistical and financial metrics
4. Explore portfolio optimization, specifically the Global Minimum Variance portfolio (GMV, it's in my Side-Quests folder)

## Case Study 1: Value at Risk (VaR) using Monte Carlo Simulation

### Objective
Simulate the future value of a stock investment (MSFT) using GBM, and compute the Value at Risk (VaR) using:
- Monte Carlo simulation (empirical percentile)
- Parametric method (mean ± z × standard deviation)

### Tools and Concepts
- GBM Simulation:  
  \[ S_t = S_0 \cdot e^{(\mu - 0.5\sigma^2)t + \sigma Z_t} \]
- Simulate log returns and convert to dollar returns
- Calculate VaR at 95% and 99% confidence
- Visualize return distribution with histogram and VaR cutoffs

### Outputs
- Histogram of simulated returns
- Parametric and Monte Carlo VaR values
- Overlay plot with mean return and VaR lines

### Why it Matters
Monte Carlo VaR captures fat tails and asymmetries that parametric methods may miss, providing more realistic risk estimates.

## Case Study 2: Stock Price Simulation using GBM

### Objective
Forecast the potential future paths of a stock (e.g., MSFT) over a 1-month horizon using GBM.

### Tools and Concepts
- Simulate 10,000 price paths using GBM
- Use exponential form of GBM for multi-step simulations
- Visualize a sample of simulated price paths

### Outputs
- Plot of GBM-simulated stock price paths
- Final price distribution histogram
- Confidence intervals and expected price range

### Why it Matters
This technique is useful in option pricing, scenario analysis, and understanding price variability over time.

## Bonus Module: Portfolio Optimization using Convex Programming

### Focus
- Construct a Global Minimum Variance (GMV) Portfolio
- Solve the quadratic optimization problem using `scipy.optimize` (SLSQP)
- Compare unconstrained vs. long-only solutions

### Skills Demonstrated
- Covariance matrix manipulation
- Application of convex optimization to minimize risk
- Practical understanding of GMV vs. maximum Sharpe portfolios

## Requirements
- Python 3.8+
- Libraries: `numpy`, `pandas`, `matplotlib`, `scipy`, `yfinance`

## Key Takeaways
- VaR provides a threshold for potential loss; CVaR estimates expected loss beyond that threshold
- Monte Carlo methods are valuable when returns are not normally distributed
- GBM is foundational in financial modeling
- Optimization techniques allow for effective portfolio construction under constraints

## Extensions
- Implement Conditional VaR (CVaR)
- Stress test under different volatility assumptions
- Extend to multi-asset portfolios with correlation
- Compare to historical VaR from real data

