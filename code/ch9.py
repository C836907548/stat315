import numpy as np
from scipy import stats

# Data
regular = np.array([1903, 1935, 1910, 2496, 2108, 1961, 2060, 1444, 1612, 1316, 1511])
kiln_dried = np.array([2009, 1915, 2011, 2463, 2180, 1925, 2122, 1482, 1542, 1443, 1535])

# Differences
differences = regular - kiln_dried

# Mean and standard deviation of differences
mean_diff = np.mean(differences)
std_diff = np.std(differences, ddof=1)

# Number of samples
n = len(differences)

# Standard error
SE = std_diff / np.sqrt(n)

# Critical value for 99% confidence interval
t_critical = stats.t.ppf(0.995, df=n-1)

# Margin of error
margin_of_error = t_critical * SE

# Confidence interval
confidence_interval = (mean_diff - margin_of_error, mean_diff + margin_of_error)

mean_diff, std_diff, SE, t_critical, margin_of_error, confidence_interval
