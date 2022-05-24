import statistics
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import tkinter as tk
import sys

import numpy as np
from numpy import double

import time


def ausgabe(dataAsString):
    ergebnis = ''
    data = [0.0] * (len(dataAsString))
    for x in range(0, len(dataAsString)):
        try:
            data[x] = float(dataAsString[x])
        except ValueError:
            showerror(
                title='Du Seggl',
                message='Deine Eingabe ist keine Zahl')

    ergebnis = ergebnis + "Als Float-Array: " + str(data)
    n = len(data)
    ergebnis = ergebnis + "\nAnzahl Elemente (n): " + str(n)

    ergebnis = ergebnis + "\nArithmetisches Mittel = " + str(np.mean(data))
    # numpy.mean() berechnet Arithmetisches Mittel(Mittelwert)

    ergebnis = ergebnis + "\nDurchschnitt = " + str(np.average(data))
    # alternative zu np.mean()

    ergebnis = ergebnis + "\nMedian = " + str(np.quantile(data, 0.5))
    # percentile(array, prozentzahl)berechnet Quantil bei Prozentzahl. Median = 0.5

    ergebnis = ergebnis + "\nModalwert(e): " + str(statistics.multimode(data))
    # am häufigsten auftretender Wert -> jewl. erster der Arrays

    ergebnis = ergebnis + "\nVarianz = " + str(np.var(data))
    # variance = (Summe der Quadrate aus allen Zahlen und Mitteln)/n

    ergebnis = ergebnis + "\nempirische Standardabweichung = " + str(np.std(data))
    # StandardDeviation = Wurzel(variance) -> wie Weit weichen Daten von Mittelwert ab?

    ergebnis = ergebnis + "\nInterquartialabstand: " + str(np.percentile(data, 75) - np.percentile(data, 25))

    ergebnis = ergebnis + "\nSpannweite (Range) = " + str(max(data) - min(data))

    text['state'] = 'normal'
    text.delete(1.0, "end")
    text.insert(tk.END, ergebnis)
    text['state'] = 'disabled'


def quantile(event=None):
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

        qnt_txt = ''
        # print("25% Quartil = ", np.quantile(data, 0.25, method="averaged_inverted_cdf"))
        qnt_txt = qnt_txt + "25.0% Quartil = " + str(np.quantile(data, 0.25, method="averaged_inverted_cdf"))
        # print("50% Quartil = ", np.quantile(data, 0.50, method="averaged_inverted_cdf"))
        qnt_txt = qnt_txt + "\n50.0% Quartil = " + str(np.quantile(data, 0.50, method="averaged_inverted_cdf"))
        # print("75% Quartil = ", np.quantile(data, 0.75, method="averaged_inverted_cdf"))
        qnt_txt = qnt_txt + "\n75.0% Quartil = " + str(np.quantile(data, 0.75, method="averaged_inverted_cdf"))

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
                qnt_txt = qnt_txt + "\n" + str(quantilvalue) + "% Quantil = " + str(
                    np.quantile(data, quantilvalue / 100, method="averaged_inverted_cdf"))
    else:
        print("\nKeine Daten eingegeben!\n")

    text['state'] = 'normal'
    text.delete(1.0, "end")
    text.insert(tk.END, qnt_txt)
    text['state'] = 'disabled'


def callback(event=None):
    # print (e.get()) # This is the text you may want to use later
    if e.get() != '':
        data = e.get().split()
        print("\nDeine Ausgangsdaten sind: ", data)
        ausgabe(data)
    else:
        print("\nKeine Daten eingegeben!\n")


def close(event):
    sys.exit()  # if you want to exit the entire thing


def sleep():
    time.sleep(5)
    text['state'] = 'normal'
    text.insert(tk.END, "\n Jetzt mal ehrlich, was machst du denn so lange?")
    text['state'] = 'disabled'


root = tk.Tk()
root.geometry("500x375")
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
    message='Hast du während deiner Klausur nichts besseres zu tun?')).grid(column=0, row=6)
ttk.Button(frm, text="Exit", command=root.destroy).grid(column=1, row=6)

frm2 = ttk.Frame(root, padding=25)
frm2.grid()
text = tk.Text(root, height=10, width=50)
text.grid(column=0, row=7)

text.insert(tk.END, "Jetzt gib mal Werte ein!!!")
text['state'] = 'disabled'

e.bind('<Return>', callback)
i.bind('<Return>', quantile)
root.bind('<Escape>', close)

#sleep()

root.mainloop()
