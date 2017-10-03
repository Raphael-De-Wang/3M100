#!/usr/bin/env python

roman=["Comment s'etaient-ils rencontres ?", "Par hasard, comme tout le monde.", "Comment s’appelaient-ils ?", "Que vous importe ?", "D’ou venaient-ils ?", "Du lieu le plus prochain"]

print [lettre for phrase in roman for lettre in phrase]

for phrase in roman:
    print phrase

questions = [ q for q in roman[::2] ]
reponses  = [ q for q in roman[1::2] ]

for ( q, r ) in zip(questions, reponses) :
    print q + "  " + r 

