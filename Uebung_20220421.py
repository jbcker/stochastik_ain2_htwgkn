import math

print("\nAufgabe 2.10.1\n")

print("a) Typ 1: 26!/(26-2)! =", math.factorial(26)/math.factorial(26-2))
print("b) Typ 2: 26^3 =", 26**3)
print("c) Typ 3: 26!/(26-4)! + 26!/(26-5)! =",
      math.factorial(26)/math.factorial(26-4) + math.factorial(26)/math.factorial(26-5))

print("\nAufgabe 2.10.2\n")

print("a) 1-(25/26*24/25) =", 1-(25/26*24/25))
print("b) (25/26)^3 =", (25/26)**3)
print("c) 0%, da ein Buchstabe sich nicht wiederholen darf.")
print("d) 2/(26!/(26-4)! + 26!/(26-5)!) =",
      2/(math.factorial(26)/math.factorial(26-4) + math.factorial(26)/math.factorial(26-5)))

print("\nAufgabe 2.5\n")
print("a) (8/32*8/31*8/30*8/29)*24 =", (8/32*8/31*8/30*8/29)*24)
print("b) 8/32*7/31*6/30*5/29 =", 8/32*7/31*6/30*5/29)
print("c) 16/32*15/31*14/30*13/29 =", 16/32*15/31*14/30*13/29)
print("d) 1-(24/32*23/31*22/30*21/29) =", 1-(24/32*23/31*22/30*21/29))

