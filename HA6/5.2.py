from scipy.stats import binom

print("a)")
print("R ~ Bin(1, %.4f)" % round(8 / 31, 4))
print("A ~ Bin(31, %.4f)" % round(8 / 31, 4))
print("W ~ Geom(%.4f)" % round(8 / 31, 4))

print("\nb)")

print("P(X > 3) =", round(1 - binom.cdf(3, 31, 8 / 31), 4))

print("\nc)")

print("P(X = 1) =", round(1 / (8 / 31), 4))
