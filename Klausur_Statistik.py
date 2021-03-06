import statistics
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import tkinter as tk
import tkinter.font as tkFont
import sys

import numpy as np
from numpy import double


def ausgabe(dataAsString):
    if len(dataAsString) <= 1:  # abfangen, wenn nur eine Zahl vorhanden
        showerror(
            title='So geht das nicht',
            message='Ohne genug Daten wird´s selbst für mich schwierig.')
        return
    ergebnis = ''
    data = [0.0] * (len(dataAsString))
    for x in range(0, len(dataAsString)):
        try:  # abfangen, wenn ein Wert keine Zahl ist
            data[x] = float(dataAsString[x])
        except ValueError:
            showerror(
                title='Du Seggl',
                message='Der ' + str(x + 1) + '. Wert aus deiner Eingabe ist keine Zahl')
            return

    ergebnis = ergebnis + "Als Float-Array: " + str(data)
    n = len(data)
    ergebnis = ergebnis + "\nAnzahl Elemente (n): " + str(n)

    mittelwert = str(np.mean(data))
    ergebnis = ergebnis + "\nArithmetisches Mittel = " + mittelwert
    # numpy.mean() berechnet Arithmetisches Mittel(Mittelwert)

    ergebnis = ergebnis + "\nDurchschnitt = " + str(np.average(data))
    # alternative zu np.mean()

    ergebnis = ergebnis + "\nMedian = " + str(np.quantile(data, 0.5))
    # percentile(array, prozentzahl)berechnet Quantil bei Prozentzahl. Median = 0.5

    ergebnis = ergebnis + "\nModalwert(e): " + str(statistics.multimode(data))
    # am häufigsten auftretender Wert -> jewl. erster der Arrays

    ergebnis = ergebnis + "\nVarianz = " + str(np.var(data, ddof=1))
    # variance = (Summe der Quadrate aus allen Zahlen und Mitteln)/n

    standardabweichung = np.std(data, ddof=1)
    ergebnis = ergebnis + "\nempirische Standardabweichung = " + str(standardabweichung)
    # StandardDeviation = Wurzel(variance) -> wie Weit weichen Daten von Mittelwert ab?

    ergebnis = ergebnis + "\nInterquartilsabstand: " + str(np.percentile(data, 75) - np.percentile(data, 25))

    ergebnis = ergebnis + "\nSpannweite (Range) = " + str(max(data) - min(data))

    ergebnis = ergebnis + "\nWahrer Erwartungswert = " + mittelwert

    ergebnis = ergebnis + "\nWahre Varianz (Std^2) = " + str(standardabweichung ** 2)

    loesung(ergebnis)


def quantile(event=None):
    if e.get() == '':
        showerror(
            title='Also ein bisschen könntest du auch noch nachdenken!',
            message='Ohne genug Daten wird´s selbst für mich schwierig.')
        return
    dataAsString = e.get().split()
    data = [0.0] * (len(dataAsString))
    for x in range(0, len(dataAsString)):
        try:
            data[x] = float(dataAsString[x])
        except ValueError:
            showerror(
                title='Du Käpsale',
                message='Der ' + str(x + 1) + '. Wert aus deiner Eingabe ist keine Zahl')
            return

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
            qnt_txt = qnt_txt + "\n" + str(quantilvalue) + "% Quantil = " + \
                      str(np.quantile(data, quantilvalue / 100, method="averaged_inverted_cdf"))

    qnt = tk.Tk()
    qnt.geometry("500x100")
    qnt.wm_title("Quantile und so")
    # frm_qnt = ttk.Frame(qnt, padding=25)
    # frm_qnt.grid()

    text = tk.Text(qnt, height=5, width=50)
    scroll = ttk.Scrollbar(qnt)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=tk.LEFT)

    scroll.config(command=text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    text.insert(tk.END, qnt_txt)
    text['state'] = 'disabled'
    # text.grid(column=0, row=0)

    b1 = Button(qnt, text="Exit", command=qnt.destroy)
    # b1.grid(column=1, row=0)
    b1.pack()


def callback(event=None):
    # print (e.get()) # This is the text you may want to use later
    if e.get() != '':
        data = e.get().split()
        print("\nDeine Ausgangsdaten sind: ", data)
        ausgabe(data)
    else:
        showerror(
            title='So geht das nicht',
            message='Ohne Daten wird´s selbst für mich schwierig.')


def loesung(data):
    lsg = tk.Tk()
    lsg.geometry("500x200")
    lsg.wm_title("Des han i schnell im Kopf gmacht!")

    text = tk.Text(lsg, height=13, width=50)
    scroll = ttk.Scrollbar(lsg)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=tk.LEFT)

    scroll.config(command=text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    n = len(data)

    text.insert(tk.END, data)
    text['state'] = 'disabled'

    b1 = Button(lsg, text="Exit", command=lsg.destroy)
    b1.pack()


def close(event):
    sys.exit()  # if you want to exit the entire thing


root = tk.Tk()
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
ttk.Label(frm, text="").grid(column=0, row=6)
fontStyle = tkFont.Font(family="Lucida Grande", size=7)
ttk.Label(frm, text="engineered by J. Böcker, L. Butscher, T. Stöhr, W. Prinz", font=fontStyle).grid(column=0, row=7)
e.bind('<Return>', callback)
i.bind('<Return>', quantile)
root.bind('<Escape>', close)

root.mainloop()
