#!/usr/bin/env python

import math

class AI (object) :
    "Find a nature number between 0 and 100. "
    def __init__(self): 
        self.scale_up   = 100
        self.scale_down = 0
        self.num = 0

    def ask(self):
        self.userInput = raw_input("Is it bigger than {0} (Yes/No) ? ".format(str(self.num)))

    def update(self):
        if self.userInput[0] in ('Y','y') :
            self.num = self.num + 1
            self.scale_down = self.num
        elif self.userInput[0] in ('N','n') :
            self.scale_up  = self.num
        else :
            print "Your input is invalid ! \n"
            
    def dichotomie(self):
        self.num = math.trunc(( self.scale_up + self.scale_down ) / 2 )

    def is_success(self):
        if self.scale_up == self.scale_down :
            return True
        else :
            return False
            
    def win(self):
        print "It is {0}. ".format(str(self.num))
        
    def talk(self):
        while not self.is_success() :
            self.dichotomie()
            self.ask()
            self.update()
        self.win()

# test 
a = AI()
a.talk()
