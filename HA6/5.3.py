from scipy.stats import poisson
print("Aufgabe 5.3:")

print("\na)")

print("P(X=3) =", round(poisson.pmf(3, 5), 4))

print("\nb)")
print("P(X>4) =", round(1 - poisson.cdf(4, 5), 4))
