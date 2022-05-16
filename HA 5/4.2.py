import numpy as np
from matplotlib import pyplot as plt

print("4.2 a)")

x = [1, 2, 3, 4, 5]
p = [0.1, 0.25, 0.35, 0.2, 0.1]

a = plt.figure(1)
plt.bar(x, p)
plt.xlim(0, 6)
plt.ylim(0,1)
plt.xlabel("x")
plt.ylabel("P(X=x)")
plt.grid(alpha=0.5)
plt.title("4.2 a)")
a.show()

print("4.2 b)")

data = [1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5]
# plt.hist(data, bins=9, density=True)
b = plt.figure(2)
plt.hist(data,bins=9, density=True, cumulative=True, label='CDF', histtype='step')
plt.xlabel("X")
plt.ylabel("P(X=x)")
plt.xticks(np.arange(1,6))
plt.title("4.2 b)")
b.show()

erwartungswert = 0
for i in range(5):
    erwartungswert = erwartungswert + (x[i] * p[i])

print("4.2 c) Erwartungswert = ", erwartungswert)
print("4.2 d) Varianz = ", np.var(data))
