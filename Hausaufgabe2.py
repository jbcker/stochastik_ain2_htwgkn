import numpy as np
import statistics
import math

from matplotlib import pyplot as plt
from scipy.stats import linregress
from sklearn.linear_model import LinearRegression
from csv import reader

print("Stochastik Hausaufgabe 2:")
print("Tobias Stöhr, Lukas Butscher, Jona Böcker")

print("\nAufgabe 1.5\n")

fahrzeug = [2, 4, 3, 1, 2, 4, 2, 2, 2, 3]
print("Fahrzeuge=", fahrzeug)

print("a) arithmetisches Mittel = ", np.mean(fahrzeug))
print("b) Median = ", np.quantile(fahrzeug, 0.5))
print("c) Modalwert(e): ", statistics.multimode(fahrzeug))
print("d) 10% Quantil = ", math.ceil(np.quantile(fahrzeug, 0.1)))
print("d) nach Tutorenlsg.: 10% Quantil = ", np.quantile(fahrzeug, 0.1, method="averaged_inverted_cdf"))
print("e) 25% Quantil = ", math.ceil(np.quantile(fahrzeug, 0.25)))
print("d) nach Tutorenlsg.: 25% Quantil = ", np.quantile(fahrzeug, 0.25, method="averaged_inverted_cdf"))
print("f) 75% Quantil = ", math.ceil(np.quantile(fahrzeug, 0.75)))
print("d) nach Tutorenlsg.: 75% Quantil = ", np.quantile(fahrzeug, 0.75, method="averaged_inverted_cdf"))
print("g) Interquartialabstand: ", np.percentile(fahrzeug, 75)-np.percentile(fahrzeug, 25))
print("h) Spannweite = ", max(fahrzeug)-min(fahrzeug))

print("\nAufgabe 1.6.1\n")

taschengeld = [25, 10, 30, 25, 35, 25]
print("Taschengeld=", taschengeld)

print("a) arithmetisches Mittel = ", np.mean(taschengeld))
print("b) Median = ", np.quantile(taschengeld, 0.5))
print("c) 75% Quantil = ", math.ceil(np.quantile(taschengeld, 0.75)))
print("c) nach Tutorenlsg. 75% Quantil = ", np.quantile(taschengeld, 0.75, method="averaged_inverted_cdf"))
print("d) empirische Standartabweichung = ", np.std(taschengeld))

print("\nAufgabe 1.6.2\n")

print("a) Die Spannweite mit R=5 ist falsch. Die Stichproben gehen von 10 - 35, damit ist die Spannweite R=25"
      "   Der Interquartialabstand kann nicht so groß sein wie die Spannweite, damit ist I=25 auch falsch.")
print("b) Das ist Zufall")
print("c) Das heißt, dass 75% der Werte kleiner sind, als das Ergebniss des 75% Quantils")
print("d) In Klasse 8b erhalten alle Schüler*innen den gleichen Monatlichen Betrag.")
print("e) Laut Franks Korrelationskoeffizienten stehen Schuhgröße und Taschengeld mit "
      "hoher Wahrscheinlichkeit in Korrelation. Mathenote und Taschengeld nicht.")
print("f) Grace sollte noch andere Werte berechnen, z.B. den Modalwert, "
      "da ein Schüler auch 900€ bekommen könnte und die anderen nichts")

print("\nAufgabe 1.9.1\n")

print("Bei C) liegen die Punkte für einen Korreleationskoeffizienten von 0,966 zu weit auseinander.")
print("Da der Korreleationskoeffizient negativ ist müssen die Punkte abschüssig sein. Daher passt nur noch B).")

print("\nAufgabe 1.9.2\n")
print("A = 0.00\n"
      "B = 0.33\n"
      "C = 0.98\n"
      "D = 1.00\n"
      "E = -0.08\n"
      "F = -0.20\n"
      "G = -0.64\n"
      "H = -1.00")

print("\nAufgabe 1.12\n")

ausbildungsdauer = [9, 13, 15, 18, 20]
jahresgehalt = [18, 37, 61, 125, 59]

print("Ausbildungsdauer = ", ausbildungsdauer)
print("Jahresgehalt [1000€] = ", jahresgehalt)

print("a) empirischer Korrelationskoeffizient = ", np.corrcoef(ausbildungsdauer, jahresgehalt)[0, 1])
print("-> korrelieren mit hoher Wahrscheinlichkeit.")
b, a, r, p, std = linregress(ausbildungsdauer, jahresgehalt)
print("b) lineare Regressionsgerade; Jahresgehalt = ", a, " + ", b, " * ausbildungsdauer")
print("   r = ", r)

f = plt.figure(1)
plt.scatter(ausbildungsdauer, jahresgehalt)
plt.plot([0, 25], [0, 130], c="red", alpha=0.5)
plt.plot()
plt.xlim(0, 25)
plt.ylim(0, 130)
plt.xlabel("Ausbildungsdauer")
plt.ylabel("Jahresgehalt [1000€]")
plt.grid(alpha=0.4)
plt.xticks([x for x in range(26) if x % 5 == 0])
plt.yticks([x for x in range(131) if x % 25 == 0])
plt.title("Plot A: ")
f.show()

abd = np.array(ausbildungsdauer)
abd = abd.reshape(-1, 1)
jgh = np.array(jahresgehalt)
lr = LinearRegression().fit(abd, jgh)
print("R² = ", lr.score(abd, jgh))

print("\nAufgabe 1.14\n")

with open('Einwohner_Deutsch_Ausländer_ab_1975_0.csv', 'r') as csv_file:
    csv_reader = reader(csv_file, delimiter=';')
    list_of_rows = list(csv_reader)
    index = 0
    jahr = [0]*(len(list_of_rows)-1)
    bevoelkerung_ges = [0]*(len(list_of_rows)-1)

    liste = [0]*6
    for x in range(1, len(list_of_rows)):
        liste = list_of_rows[x]
        for y in range(0, len(liste)):
            jahr[x-1] = int(liste[2])
            bevoelkerung_ges[x-1] = int(liste[3])

g = plt.figure(2)
plt.scatter(jahr, bevoelkerung_ges)
plt.plot()
plt.xlim([jahr[0], jahr[len(jahr)-1]])
plt.xlabel("Jahr")
plt.ylabel("Gesamtbevölkerung")
plt.grid(alpha=0.5)

print("Plot B zeigt die Bevölkerungsentwicklung in Konstanz für die Jahre 1975-2018.")
print("Bis 1984 war die entwicklung leicht rückläufig. Bis 2018 stiegen die Zahlen konstant.")
print("Erst im Jahre 1991 erreichte die Gesamtbevölkerung wieder den Stand von 1975.")

b, a, r, p, std = linregress(jahr, bevoelkerung_ges)
print("\nlineare Regressionsgerade für die Gesamtbevölkerung = ", a, " + ", b, " * Jahr")
print("r = ", r)
jahrn = np.array(jahr)
plt.plot(jahrn, b*jahrn + a, c="magenta")
plt.title("Plot B: Gesamtbevölkerung über Jahre")
g.show()

bvg = np.array(bevoelkerung_ges)
bvg = bvg.reshape(-1, 1)
lr = LinearRegression().fit(bvg, jahrn)

print("\nDie Magenta Regressionsgerade in Plot B bildet den Korrelationskoeffizienten ab.")
print("Die Bevölkerungszahl korreliert positiv mit der Jahreszahl.\n")
print("Ein R²-Wert von: ", lr.score(bvg, jahrn), "zeigt, dass die einzelnen Werte nicht weit von der Regressionsgerade abweichen.")

zuwachs = [0]*(len(bevoelkerung_ges)-1)

for x in range(1, len(bevoelkerung_ges)):
    zuwachs[x-1] = bevoelkerung_ges[x] - bevoelkerung_ges[x-1]

jahr.pop(0)
y = plt.figure(3)
plt.bar(jahr, zuwachs)
plt.xlim([jahr[0]-1, jahr[len(jahr)-1]+1])
plt.xlabel("Jahr")
plt.ylabel("Zuwachs der Gesamtbevölkerung")
plt.grid(alpha=0.5)
plt.title("Plot C: Zuwachs der Gesamtbevölkerung")
plt.show()

print("\nPlot C zeigt den Bevölkerungszuwachs über die Jahre 1975-2018 in Konstanz.")
