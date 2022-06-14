from scipy.stats import poisson
from scipy.stats import expon
from scipy.stats import norm

print("\nKlausur SS21\n")
print("\nAufgabe 5.1:\n")

print("a)\n")
print("P(Z = 1/7) = 0; weil stetig")

print("\nb)")
print("noch falsch (0,633) P(Z < 1/7)", expon.cdf(2, 0, 7))

print("\nc)")
print("P(X = 7) = ", poisson.pmf(7, 7))

print("\nAufgabe 5.2:\n")

print("\na)")
print("P(M >= 120) = ", norm.sf(120, 130, 15))

print("\nb)")
print("P(115 <= M <= 145) = ", norm.cdf(145, 130, 15) - norm.cdf(115, 130, 15))

print("\nc)")
print("P(M >= x) = 0.1; x = ", norm.isf(0.1, 130, 15))

print("\nd)")
print("P(M) = ", norm.interval(0.9, 130, 15))
