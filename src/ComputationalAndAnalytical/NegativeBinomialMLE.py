import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb
from scipy.optimize import minimize_scalar



def negative_binomial_log_likelihood(p, x, k):
    """
    Log-likelihood for Negative Binomial (trials until k successes)
    p : success probability
    x : array of observations
    k : fixed number of successes
    """
    if p <= 0 or p >= 1:
        return -np.inf

    return np.sum(
        np.log(comb(x - 1, k - 1))
        + k * np.log(p)
        + (x - k) * np.log(1 - p)
    )

np.random.seed(123)  # Set random seed to ensure reproducibility of the simulation
n = 50  # Define sample size (number of observations)
k = 3  # Fix the number of required successes in the negative binomial model
p_true = 0.4  # Set the true success probability used to generate synthetic data

# Generate data from a negative binomial distribution
# numpy.random.negative_binomial returns the number of failures
# before k successes, so we add k to obtain the total number of trials
x = np.random.negative_binomial(k, p_true, size=n) + k

# Compute the analytical MLE derived in Section 2.2: p_hat = k / mean(x)
p_hat_analytical = k / np.mean(x)
print("Analytical MLE:", p_hat_analytical)

# Numerically maximize the log-likelihood by minimizing its negative
# The bounds enforce that p remains in the valid interval (0, 1)
result = minimize_scalar(
    lambda p: -negative_binomial_log_likelihood(p, x, k),
    bounds=(1e-6, 1 - 1e-6),
    method="bounded"
)

p_hat_numerical = result.x  # Extract the numerical maximum likelihood estimate from the optimizer
print("Numerical MLE:", p_hat_numerical)

# Create a fine grid of p values to evaluate the log-likelihood function
p_grid = np.linspace(0.01, 0.99, 1000)

# Evaluate the log-likelihood at each grid point
loglik_values = [
    negative_binomial_log_likelihood(p, x, k)
    for p in p_grid
]

# Create a new figure for the log-likelihood plot
plt.figure()
plt.plot(p_grid, loglik_values)  # Plot the log-likelihood function as a function of p

# Add a vertical lines at the analytical and numerical MLEs
plt.axvline(p_hat_analytical, linestyle="--", label="Analytical MLE")
plt.axvline(p_hat_numerical, linestyle=":", label="Numerical MLE")
plt.xlabel("p")  # Label the x-axis
plt.ylabel("Log-likelihood")  # Label the y-axis
plt.title("Log-likelihood of Negative Binomial Distribution")  # Add a title to the plot

plt.legend()  # Display a legend identifying the MLE lines
plt.show()  # Display the plot
