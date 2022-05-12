from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

import numpy as np
from numpy import double


def ausgabe(dataAsString):
    data = [0.0] * (len(dataAsString))
    for x in range(0, len(dataAsString)):
        try:
            data[x] = float(dataAsString[x])
        except ValueError:
            showerror(
                title='Du Seggl',
                message='Deine Eingabe ist keine Zahl')

    print("Als Float-Array: ", data)
    n = len(data)
    print("Anzahl Elemente (n): ", n, "\n")

    print("Arithmetisches Mittel = ", np.mean(data))
    # numpy.mean() berechnet Arithmetisches Mittel(Mittelwert)
    print("Durchschnitt = ", np.average(data))
    # alternative zu np.mean()

    print("Median = ", np.quantile(data, 0.5))
    # percentile(array, prozentzahl)berechnet Quantil bei Prozentzahl. Median = 0.5

    # modalarray = np.unique(data, return_counts=True)
    print("Modalwert(e): ", np.unique(data, return_counts=True))
    # am häufigsten auftretender Wert -> jewl. erster der Arrays

    print("Varianz = ", np.var(data))
    # variance = (Summe der Quadrate aus allen Zahlen und Mitteln)/n

    print("empirische Standardabweichung =", np.std(data))
    # StandardDeviation = Wurzel(variance) -> wie Weit weichen Daten von Mittelwert ab?

    print("Interquartialabstand: ", np.percentile(data, 75) - np.percentile(data, 25))

    print("Spannweite (Range) = ", max(data) - min(data))

    print("")


def quantile():
    if e.get() != '':
        dataAsString = e.get().split()
        data = [0.0] * (len(dataAsString))
        for x in range(0, len(dataAsString)):
            try:
                data[x] = float(dataAsString[x])
            except ValueError:
                showerror(
                    title='Du Käpsale',
                    message='Deine Eingabe ist keine Zahl')

        print("25% Quartil = ", np.quantile(data, 0.25, method="averaged_inverted_cdf"))
        print("50% Quartil = ", np.quantile(data, 0.50, method="averaged_inverted_cdf"))
        print("75% Quartil = ", np.quantile(data, 0.75, method="averaged_inverted_cdf"))

        if i.get() != '':
            quantilvalue = i.get()
            quantilvalue = double(quantilvalue)

            if quantilvalue < 0 or quantilvalue > 100:
                showerror(
                    title='Bisch du bled?',
                    message='Quantile < 0 oder > 100 können nicht berechnet werden!')
            else:
                print(quantilvalue, "% Quantil = ",
                      np.quantile(data, quantilvalue / 100, method="averaged_inverted_cdf"))
    else:
        print("\nKeine Daten eingegeben!\n")


def callback():
    # print (e.get()) # This is the text you may want to use later
    if e.get() != '':
        data = e.get().split()
        print("\nDeine Ausgangsdaten sind: ", data)
        ausgabe(data)
    else:
        print("\nKeine Daten eingegeben!\n")


root = Tk()
root.wm_title("Kannsch des nich im Kopf rechna?!")
frm = ttk.Frame(root, padding=25)
frm.grid()
ttk.Label(frm, text="Gebe deine Eingangswerte mit Leerzeichen getrennt ein").grid(column=0, row=0)
e = ttk.Entry(frm, width=48)

e.grid(column=0, row=1)
e.focus_set()

ttk.Button(frm, text="Standardwerte berechnen", command=callback).grid(column=1, row=1)
ttk.Label(frm, text="Gebe einen Wert für ein bestimmtes Quantil ein").grid(column=0, row=2)
i = ttk.Entry(frm, width=48)
i.grid(column=0, row=3)
ttk.Button(frm, text="Quantile berechnen", command=quantile).grid(column=1, row=3)
ttk.Label(frm, text="").grid(column=0, row=4)
ttk.Button(frm, text="Drück mi", command=lambda: showinfo(
        title='HaHa',
        message='Hast du während deiner Klausur nichts besseres zu tun?')).grid(column=0, row=5)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=5)
root.mainloop()
