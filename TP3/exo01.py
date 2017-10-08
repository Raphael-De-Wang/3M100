#!/usr/bin/env python

import abc

class Suite(object) :
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        self.suite_lst = []

    @abc.abstractmethod
    def next(self,Un_1,Un_2): # how to make the list of vars extenable ? 
        return
        
    @abc.abstractmethod        
    def u_ext(self, n) :
        pass

    def show(self) :
        print self.suite_lst

    def get(self,n) :
        if n >= len(self.suite_lst) :
            self.u_ext(n)
        return self.suite_lst[n]
    
############################
##  ##   question 1   ##  ##

class Un(Suite) :
    def __init__(self):
        self.u0 = 0
        self.u1 = 1
        self.suite_lst = [self.u0, self.u1]

    def next(self,Un_1,Un_2) :
        return Un_1 + Un_2

    def u_ext(self, n) :
        if type(n) is int and n > 1 :
            # for i in range(len(self.suite_lst),n+1) :
            while len(self.suite_lst) <= n :
                un_tmp = self.next(self.suite_lst[-2],self.suite_lst[-1])
                self.suite_lst.append(un_tmp)

                
# test
# un = Un()
# print un.get(10)
# un.show()

############################
##  ##   question 2   ##  ##

class UV(Suite) :
    def __init__(self):
        self.u0 = 1
        self.v0 = 1
        self.suite_lst = [(self.u0,self.v0)]
    
    def next(self,Un,Vn) :
        return (Un+Vn, 2*Un-Vn)

    def u_ext(self,n) :
        if type(n) is int and n > 1 :
            # for i in range(len(self.suite_lst),n+1) :
            while len(self.suite_lst) <= n :
                un_tmp = self.next(self.suite_lst[-1][0],self.suite_lst[-1][1])
                self.suite_lst.append(un_tmp)

                
# test
# uv = UV()
# print uv.get(100)
# uv.show()

        
