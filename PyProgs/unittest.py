#!/bin/usr/python3

import sys
# List-Comprehension/Funktionale Ausdrücke schreiben
# Schreiben Sie zwei Funktionen, die jeweils nur aus zwei Zeilen bestehen, 
# den Funktionskopf mit def und der Rückgabe als eine List-Comprehension oder ein funktionaler Ausdruck. 
# Leerzeilen sind erlaubt. Beide Funktionen filtern ihr Argument, 
# geben also von einer Liste als Argument nur Elemente zurück, die eine gewisse Eigenschaft haben.

# Die Funktion vonvornewievonhinten(lis) gibt aus einer Liste von Strings lis nur die Strings als Liste zurück, 
# die von vorne wie von hinten gelesen das gleiche Wort ergeben. So werden die Worte abba und abcba 
# durchgelassen, aber die Wort bla, abc, abcda nicht.

# Die Funktion gleichebuchstaben(lis, words) gibt aus einer Liste von Strings lis nur die Strings als 
# Liste zurück, wenn in einer anderen Liste von Strings words ein Wort auftaucht, 
# dass genau die gleichen Buchstaben hat, nur in einer anderen Reihenfolge. 
# Dazu darf das Wort selbst aber nicht in words auftauchen. Wenn words = ["abc", "defg", "aaabb"], 
# dann wird zum Beispiel cba und bac durchgelassen, aber abc nicht; 
# es wird auch edfg und degf durchgelassen, aber gdefg nicht; 
# es wird auch ababa durchgelassen, aber babab nicht.
def main():
    print(list(filter(lambda x: x[::-1] == x, words)))
    pass

if __name__ == "__main__":
    main()