# -*- coding: utf-8 -*-
"""
Spyder Editor

Xasanov Ismoil
"""

son = int(input("Butun son kiriting: "))

login = []

for n in range(2,11):
    if not (son%n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")