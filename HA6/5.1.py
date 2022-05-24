import math
from scipy.stats import binom

print("Aufgabe 5.1\na)")
print("Ereignisraum: (1,1,1,1,1), (1,1,1,1,2), (1,1,1,1,3), ... (10,10,10,10,9), (10,10,10,10,10)")
print("Wertebereich: [0,1,2,3,4,5]")
print("\nb)\nx\t\t", "0\t\t\t", "1\t\t\t", "2\t\t\t", "3\t\t\t", "4\t\t\t", "5\t\t\t")
print("P(X=x)\t", round(math.pow(9 / 10, 5), 6), "\t", round(math.pow(9 / 10, 4) * 1 / 10, 6), "\t",
      round(math.pow(9 / 10, 3) * math.pow(1 / 10, 2), 6),
      "\t", round(math.pow(9 / 10, 2) * math.pow(1 / 10, 3), 6), "\t", round(9 / 10 * math.pow(1 / 10, 4), 6), "\t",
      round(math.pow(1 / 10, 5), 6))
print("\nc)")
n, p = 5, 1 / 10
print("P(X<=2: ", binom.cdf(2, n, p))
print("P(X>=3) = 1-P(X<=2): ", round(1 - binom.cdf(2, n, p), 4))
print("\nd)\nErwartungswert = ", 0.1 * 5)
