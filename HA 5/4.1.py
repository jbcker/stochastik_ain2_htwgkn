import numpy as np
import matplotlib.pyplot as plt

print("4.1.1")

x = [1, 2, 3]
px1 = [round(4/8, 4), round(1/8, 4), round(3/8, 4)]
px2 = [round(3/8, 4), round(3/8, 4), round(2/8, 4)]
fx1 = [px1[0], px1[0] + px1[1], px1[0] + px1[1] + px1[2]]
fx2 = [px2[0], px2[0] + px2[1], px2[0] + px2[1] + px2[2]]

print("a)")
print("x1\t\t", "1\t\t", "2\t\t", "3\t\t")
print("P(X=x1)\t", round(4/8, 4), "\t", round(1/8, 4), "\t", round(3/8, 4))
print("")
print("x2\t\t", "1\t\t", "2\t\t", "3\t\t")
print("P(X=x1)\t", round(3/8, 4), "\t", round(3/8, 4), "\t", round(2/8, 4))
print("\n")
print("x\t\t", "1\t\t", "2\t\t", "3\t\t")
print("F(x1)\t", fx1[0], "\t", fx1[1], "\t", fx1[2], "\t")
print("")
print("x\t\t", "1\t\t", "2\t\t", "3\t\t")
print("F(x2)\t", fx2[0], "\t", fx2[1], "\t", fx2[2], "\t")


print("4.1.1 b)")

# set width of bar
barWidth = 0.25
fig = plt.subplots()
x2 = [x + barWidth for x in x]

plt.bar(x, px1, color='r', width=barWidth,
        edgecolor='grey', label='P(x=x1)')
plt.bar(x2, px2, color ='g', width=barWidth,
        edgecolor ='grey', label ='P(x=x2)')
# Adding Xticks
plt.ylim(0, 1)
plt.xlim(0.5, 3.5)
plt.xlabel('x', fontweight ='bold', fontsize = 15)
plt.ylabel('P(X=x)', fontweight ='bold', fontsize = 15)
plt.xticks([r + barWidth for r in range(4)],
           ['0', '1', '2', '3'])
plt.title("4.1.1 b)")

plt.legend()
plt.show()

print("4.1.1 c)")
typ1 = [1, 1, 1, 1, 2, 3, 3, 3]
typ2 = [1, 1, 1, 2, 2, 2, 3, 3]

b = plt.figure(2)
plt.hist(typ1, bins=9, density=True, cumulative=True, label='CDF', histtype='step')
plt.hist(typ2, bins=9, density=True, cumulative=True, label='CDF', histtype='step')
plt.xlabel("X")
plt.ylabel("F(x)")
plt.xticks(np.arange(1, 4))
plt.title("4.1.1 c)")
b.show()

print("4.1.2")
erwartungswert = 0
for i in range(3):
    erwartungswert = erwartungswert + (x[i] * px1[i])
print("a) Erwartungswert = ", erwartungswert)

erwartungswert = 0
for i in range(3):
    erwartungswert = erwartungswert + (x[i] * px2[i])
print("a) Erwartungswert = ", erwartungswert)

print("b) Varianz x1 = ", np.var(typ1))
print("b) Varianz x2 = ", np.var(typ2))

print("c) Standardabweichung x1=", np.std(typ1))
print("c) Standardabweichung x2=", np.std(typ2))
