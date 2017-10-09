#!/usr/bin/env python

from time import ctime

num_1to60 = ["un","deux","trois","quatre","cinq","six","sept","huit","neuf","dix","onze","douze","treize","quatorze","quinze","seize","dix-sept","dix-huit","dix-neuf","vingt","vingt et un","vingt-deux","vingt-trois","vingt-quatre","vingt-cinq","vingt-six","vingt-sept","vingt-huit","vingt-neuf","trente","trente et un","trente-deux","trente-trois","trente-quatre","trente-cinq","trente-six","trente-sept","trente-huit","trente-neuf","quarante","quarante et un","quarante-deux","quarante-trois","quarante-quatre","quarante-cinq","quarante-six","quarante-sept","quarante-huit","quarante-neuf","cinquante","cinquante et un","cinquante-deux","cinquante-trois","cinquante-quatre","cinquante-cinq","cinquante-six","cinquante-sept","cinquante-huit""cinquante-neuf","soixante"]

class Heure(object):
    def __init__(self):
        self.ct = ctime()
        (wkday, month, day, time, year) = self.digital(self.ct)
        self.ct_dt = {"wkday": wkday, "day":day, "month":month, "time":time, "year":year}
        self.num_dict = {str(ind+1) : num_1to60[ind] for ind in range(len(num_1to60))}

    def digital(self, ct) :
        (wkday, month, day, time, year) = ct.split()
        return (wkday, month, day, time, year)

    def tm_digi2let(self, tm):
        (h,m,s) = tm.split(":")
        return "il est {0} heures, {1} minutes et {2} secondes".format(self.num_dict[h],\
                                                                       self.num_dict[m],\
                                                                       self.num_dict[s])

heure = Heure()
print heure.tm_digi2let(heure.ct_dt["time"])



