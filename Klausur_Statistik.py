from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

import numpy as np
from numpy import double


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

    print("Median = ", np.quantile(data, 0.5))
    # percentile(array, prozentzahl)berechnet Quantil bei Prozentzahl. Median = 0.5

    ergebnis = ergebnis + "\nModalwert(e): " + str(statistics.multimode(data))
    # am häufigsten auftretender Wert -> jewl. erster der Arrays

    ergebnis = ergebnis + "\nVarianz = " + str(np.var(data))
    # variance = (Summe der Quadrate aus allen Zahlen und Mitteln)/n

    ergebnis = ergebnis + "\nempirische Standardabweichung =" + str(np.std(data))
    # StandardDeviation = Wurzel(variance) -> wie Weit weichen Daten von Mittelwert ab?

    ergebnis = ergebnis + "\nInterquartialabstand: " + str(np.percentile(data, 75) - np.percentile(data, 25))

    ergebnis = ergebnis + "\nSpannweite (Range) = " + str(max(data) - min(data))

    loesung(ergebnis)


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

        quantiletxt = ''
        # print("25% Quartil = ", np.quantile(data, 0.25, method="averaged_inverted_cdf"))
        quantiletxt = quantiletxt + "25.0% Quartil = " + str(np.quantile(data, 0.25, method="averaged_inverted_cdf"))
        # print("50% Quartil = ", np.quantile(data, 0.50, method="averaged_inverted_cdf"))
        quantiletxt = quantiletxt + "\n50.0% Quartil = " + str(np.quantile(data, 0.50, method="averaged_inverted_cdf"))
        # print("75% Quartil = ", np.quantile(data, 0.75, method="averaged_inverted_cdf"))
        quantiletxt = quantiletxt + "\n75.0% Quartil = " + str(np.quantile(data, 0.75, method="averaged_inverted_cdf"))

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
                quantiletxt = quantiletxt + "\n" + str(quantilvalue) + "% Quantil = " + str(
                    np.quantile(data, quantilvalue / 100, method="averaged_inverted_cdf"))
    else:
        print("\nKeine Daten eingegeben!\n")

    qnt = tk.Tk()
    qnt.geometry("500x100")
    qnt.wm_title("Quantile und so")
    #frm_qnt = ttk.Frame(qnt, padding=25)
    #frm_qnt.grid()

    text = tk.Text(qnt, height=5, width=50)
    scroll = ttk.Scrollbar(qnt)
    text.configure(yscrollcommand=scroll.set)
    text.pack(side=tk.LEFT)

    scroll.config(command=text.yview)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    text.insert(tk.END, quantiletxt)
    text['state'] = 'disabled'
    #text.grid(column=0, row=0)

    b1 = Button(qnt, text="Exit", command=qnt.destroy)
    #b1.grid(column=1, row=0)
    b1.pack()


def callback(event=None):
    # print (e.get()) # This is the text you may want to use later
    if e.get() != '':
        data = e.get().split()
        print("\nDeine Ausgangsdaten sind: ", data)
        ausgabe(data)
    else:
        print("\nKeine Daten eingegeben!\n")


def loesung(data):
    lsg = tk.Tk()
    lsg.geometry("500x200")
    lsg.wm_title("Des han i schnell im Kopf gmacht!")

    text = tk.Text(lsg, height=10, width=50)
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
e.bind('<Return>', callback)
i.bind('<Return>', quantile)
root.bind('<Escape>', close)
root.mainloop()
