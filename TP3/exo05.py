#!/usr/bin/env python

import numpy as np

class Premiers(object):
    def __init__(self, N):
        self.N = N
        self.pri_lst = []
        # [2,3,4,5,.....]
        self.num_lst = [ i + 2 for i in range(N-1) ]
        self.crible_eratosthene(self.num_lst)

    def pri2ind(self,pri):
        # [2,3,4,5,.....]        
        return pri - 2
        
    def crible_eratosthene(self, lst):
        for p in lst :
            if p == 0 :
                continue
            pc = p**2
            if pc >= self.N:
                break
            l = len(lst[self.pri2ind(p**2)::p])
            lst[self.pri2ind(pc)::p] = [0 for i in xrange(l)]
        self.num_lst = lst
        lst = np.array(lst)
        self.pri_lst = lst[lst!=0]

    def show(self) :
        return self.pri_lst



# p = Premiers(100)
# print p.show()
