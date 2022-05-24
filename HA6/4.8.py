import terminaltables
from matplotlib import pyplot as plt
import numpy as np

print("Autoren: Jona Böcker, Lukas Butscher, Wiebke Prinz, Tobias Stöhr")

print("\nAufgabe 4.8.1:\n")

print("a)")

data = [
    ["x", "1", "2", "3", "4", "5", "6"],
    ["P(X1=x)", round(2 / 6, 4), round(2 / 6, 4), round(2 / 6, 4), 0, 0, 0],
    ["P(X3=x)", 0, round(2 / 6 * 2 / 6, 4), round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4),
     round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4),
     round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4), round(2 / 6 * 2 / 6, 4)]
]

table = terminaltables.AsciiTable(data)
print(table.table)

print("\nb) PLot")

x1 = [round(2 / 6, 4), round(2 / 6, 4), round(2 / 6, 4), 0, 0, 0]
x2 = [0, round(2 / 6 * 2 / 6, 4), round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4),
      round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4),
      round(2 / 6 * 2 / 6 + 2 / 6 * 2 / 6, 4), round(2 / 6 * 2 / 6, 4)]
y = [1, 2, 3, 4, 5, 6]

# set width of bar
barWidth = 0.25
fig = plt.subplots()
y2 = [y + barWidth for y in y]

plt.bar(y, x1, color='r', width=barWidth,
        edgecolor='grey', label='P(x=x1)')
plt.bar(y2, x2, color='b', width=barWidth,
        edgecolor='grey', label='P(x=x2)')
# Adding Xticks
plt.ylim(0, 1)
plt.xlim(0.5, 6.5)
plt.xlabel('x', fontweight='bold', fontsize=15)
plt.ylabel('P(X=x)', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(4)],
           ['0', '1', '2', '3'])
plt.title("4.8.1 b)")

plt.legend()
plt.show()

print("\nc)")

print("P(A) = ", round(1 - 2 / 6 * 2 / 6, 4))

print("P(B) = ", round(2 / 6 * 2 / 6 * 6, 4))

print("\nDas Spiel ist nicht fair.")

print("\nAufgabe 4.8.2:\n")
x = [1, 1, 2, 2, 3, 3]
p = [1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6, 1 / 6]
erwartungswert = 0
for i in range(6):
    erwartungswert = erwartungswert + (x[i] * p[i])
print("a) Erwartungswert X1 =", erwartungswert)

print("b) Varianz X1 = ", np.var(x))

print("c) Standardabweichung x1 =", np.std(x))

print("d) Erwartungswert:", erwartungswert * 21/6)
