import numpy as np
from scipy.stats import norm

def risk_calculation ():
    print ("--- Gaussian VaR & ER Calculator ---")
    mean = float (input ("Mean return (μ): "))
    sigma = float (input ("Standard deviation (σ): "))
    confidence = float (input ("Confidence level: "))
    horizon = int (input ("Time horizon (days): "))

    mean_h = mean * horizon
    sigma_h = sigma * horizon
    z = norm.ppf(1 - confidence)
    var = -(mean_h + z * sigma_h)
    es = -(mean_h - sigma_h * (norm.pdf(z) / (1 - confidence)))

    return var, es

var, es = risk_calculation()

print (f"\nResults:")
print (f"Gaussian VaR: {var:.2%}")
print (f"Gaussian ES: {es:.2%}")