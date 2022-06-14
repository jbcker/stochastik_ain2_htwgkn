from scipy.stats import geom

print("\nAufgabe 5.9.1:\n")

print("a) X ~ geom(0.25)"
      "   Y ~ Bin(10,0.25)")

print("b) P(Y>=2) = ", )

print("c) ", geom.pmf(5, 0.25))     #einzelwert
             #geom.cdf(5, 0.25)      #kumuliert

print("d) ", geom.ppf(0.9, 0.25))   #invers of cdf / 0.9 = 90% / Wie oft muss ich ... bis mit einer wahrscheinlichkeit von 90% ...
