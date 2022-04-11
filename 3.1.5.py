import numpy as np

wohnung = [4, 3, 5, 1, 5, 2, 1, 3, 1, 3]
print("Wohnung=", wohnung)

print("a) arithmetisches Mittel = ", np.mean(wohnung))
# numpy.mean() berechnet Arithmetisches Mittel(Mittelwert)
print("a) durchschnitt = ", np.average(wohnung))
# alternative zu np.mean()

print("b) Median = ", np.quantile(wohnung, 0.5))
# percentile(array, prozentzahl)berechnet Quantil bei Prozentzahl. Median = 0.5

modalarray = np.unique(wohnung, return_counts=True)
print("c) Modalwert(e): ", np.unique(wohnung, return_counts=True))
# am häufigsten auftretender Wert -> jewl. erster der Arrays

print("d) 25% Quantil = ", np.quantile(wohnung, 0.25))
print("e) 30% Quantil = ", np.quantile(wohnung, 0.3))
print("f) 66% Quantil = ", np.quantile(wohnung, 0.66))

print("g) Varianz = ", np.var(wohnung))
# variance = (Summe der Quadrate aus allen Zahlen und Mitteln)/n

print("h) Standardabweichung =", np.std(wohnung))
# StandardDeviation = Wurzel(variance) -> wie Weit weichen Daten von Mittelwert ab?
