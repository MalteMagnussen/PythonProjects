import re

txt = """A Henning Gamborg Møller
Klostergade 28
6760 Ribe
61 69 03 76

A K Møller
Bregnerødvej 75, st. 0002
3460 Birkerød
75 50 75 14

A Møller
Violvej 3
Ø. Bjerregrav
8920 Randers NV
86 45 44 36

A Møller
Hyrdevej 16A
7000 Fredericia
76 42 00 81

A Møller
Brammersgade 45
8000 Aarhus C
86 13 22 99

A Møller
Dalstræde 11
Heltborg
7760 Hurup Thy
97 95 20 01

A Møller
Jørgensgaardvej 13
6240 Løgumkloster
74 74 36 62

A Møller Andersen
Gammel Holtevej 60
Gl Holte
2840 Holte
45 80 47 14

A Møller Jensen
Viborgvej 115, 1. TV
Hasle
8210 Aarhus V
60 94 39 04

A Møller Sørensen
Korsørgade 4, 6. tv
2100 København Ø
35 38 97 81

A Porse Møller
Røddikvej 60
8464 Galten
86 94 66 60

Aage Beck Møller
Rødding Nørregade 8
6630 Rødding
20 44 00 35

Aage Bojsen-Møller
Noret 3
4780 Stege
55 81 46 76

Aage Christian Møller Andersen
Jordemodervej 7
Bislev
9240 Nibe
20 83 70 65

Aage Hansen Møller
Filippavej 38
Hundstrup
5762 Vester Skerninge
62 24 10 81

Aage Jan Møller
Næsborgvej 50, st. th
2650 Hvidovre
20 83 88 62

Aage Karl Møller
Dyrevænget 21
Tibirke Sand
3300 Frederiksværk
51 15 15 66

Aage Majbom Møller
Pilelunden 23
5550 Langeskov
28 59 06 93

Aage Martin Møller
Almind Østergade 15A, 1. tv
6051 Almind
21 48 73 79

Aage Møller
Ørritslev Gade 7
Ørritslev
5450 Otterup
64 82 11 54

Aage Møller
Knudsvej 1
8586 Ørum Djurs
40 10 80 76

Aage Møller
Fruevej 4
7900 Nykøbing M
21 79 64 18

Aage Møller
Dybdevej 30
Bolbro
5200 Odense V
23 66 57 00

Aage Møller
Hammelmosevej 12
9700 Brønderslev
60 45 79 69

Aage Møller
Birkevej 6
8370 Hadsten
29 68 03 25
"""

nameReg = re.compile(r"\n\n(.+)")

items = nameReg.findall(txt)

print(items)
