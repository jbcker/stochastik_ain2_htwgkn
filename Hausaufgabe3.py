import statistics

import numpy as np

print("Autoren: Jona Böcker, Lukas Butscher, Wiebke Prinz, Tobias Stöhr")

print("\nAufgabe 1.11.1:\n")

att = [7, 4, 10, 10, 9, 3, 9, 6]

print("a) Modalwert(e): ", statistics.multimode(att))
print("b) arithmetisches Mittel = ", np.mean(att))
print("c) Standartabweichung = ", np.std(att, ddof=1))
print("d) 25% Quantil =", np.quantile(att, 0.25, method="averaged_inverted_cdf"))
print("   50% Quantil =", np.quantile(att, 0.5, method="averaged_inverted_cdf"))
print("   75% Quantil =", np.quantile(att, 0.75, method="averaged_inverted_cdf"))
print("e) 60% Quantil =", np.quantile(att, 0.6, method="averaged_inverted_cdf"))

print("\nAufgabe 1.11.2:\n")

print("a) Wir würden uns für Job 3 entscheiden, da uns eine interessante Tätigkeit und\n"
      "   ein attraktives Umfeld wichtiger sind als ein hohes Gehalt.\n")
print("b) Bei Bob sind alle Städte mit dem Wert 5 bewertet, um eine Standardabweichung\n"
      "   von 5 zu erreichen muss die mittlere Differenz zum Mittelwert 5 betragen.\n"
      "   Dies ist bei Alice nur möglich, wenn sie alle Städte sehr gut oder sehr schlecht\n"
      "   bewertet und dann ihre Standardabweichung gerundet hat.\n")
print("c) 1.) d, Es gibt für eine Attraktivität von 10 sowohl das höchste, als auch das niedrigste Gehalt.\n"
      "          Das gleiche lässt sich auch bei anderen Werten beobachten.\n"
      "   2.) b, Bei Städten, die eine hohe Attraktivität haben sind die Jobs meistens uninteressant.\n"
      "          Bei unattraktiven Städten hingegen scheint der Job interessant zu sein. \n"
      "   3.) c, Die uninteressanteren Jobs sind teilweise besser bezahlt.\n"
      "          d.h. mit steigendem interesse an den Tätigkeiten sinkt das Gehalt tendenziell.\n")

print("\nAufgabe 2.1.1:\n")

print("a) Omega = {1,2,3,4,5,6,7,8,9,10}\n")
print("b) Nein, da die 2 nicht ungerade ist und somit nicht in A enthalten ist.\n")
print("c) Ja, da die 2 in beiden Mengen enthalten ist.\n")
print("d) !A = gerade Augenzahl, !B = Omega\\{2}, !C = Omega\\{2,3} ")

print("\nAufgabe 2.1.2:\n")

print("a) 1/10 = 10%")
print("b) 5/10 = 50%")
print("c) 8/10 = 80%")
print("d) 2/10 = 20%")

print("\nAufgabe 2.1.3:\n")

print("a) 1/10 * 1/10 = 1/100 = 1%")
print("b) 1/10 + 1/10 = 2/10 = 20%")
print("c) ((1,3), (2,2), (3,1), (2,2)) = 4/100 = 4%")
print("d) ((10,9), (10,10), (9,10), (10,10)) = 4/100 = 4%")

print("\nAufgabe 2.3.1:\n")

print("a) Es gibt 10^4 = ", 10 ** 4, "mögliche PINs")
print("b) Es gibt 9 * 10^3 = ", 9 * 10 ** 3, "mögliche PINs")

print("\nAufgabe 2.3.2:\n")

print("a) 3/10^4 = ", 3 / 10 ** 4)
print("b) 3/(9 * 10^3) = ", 3 / (9 * 10 ** 3))

print("\nAufgabe 2.4:\n")

print("a) zwei Rote: 6/14 * 5/13 = ", 6 / 14 * 5 / 13)
print("b) zwei Blaue: 8/14 * 7/13 = ", 8 / 14 * 7 / 13)
print("c) zwei Verschiedene: 1-((6/14 * 5/13) + (8/14 * 7/13)) = ", 1 - ((6 / 14 * 5 / 13) + (8 / 14 * 7 / 13)))
print("d) zwei Gleiche:(6/14 * 5/13) + (8/14 * 7/13) = ", (6 / 14 * 5 / 13) + (8 / 14 * 7 / 13))

print("\nAufgabe 2.7:\n")

print("Vierfeldertafel:")
print("\t", "A\t\t", "!A\t", "\t")
print(" B\t", "0.2\t", "0.3\t", "0.5\t")
print("!B\t", "0.4\t", "0.1\t", "0.5\t")
print("\t", "0.6\t", "0.4\t", "1.0\t")

print("a) Die Wahrscheinlichkeit, dass ein Einwohner beide Lokalblätter liest liegt bei 0.2. P(A∩B)")
print("b) Die Wahrscheinlichkeit, dass ein Einwohner keines der Lokalblätter liest liegt bei 0.1. P(!A∩!B)")
print("c) Die Wahrscheinlichkeit, dass ein Einwohner eines der Lokalblätter liest liegt bei 0.7. P((!A∩B)∪(A∩!B))")
