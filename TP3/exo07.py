#!/usr/bin/env python

class PolyN(object) :
    def __init__(self, poly):
        self.poly     = poly
        self.poly_dri = self.derive(poly)
        self.poly_pri = self.primitive_const_nul(poly)
    
    def derive(self, poly):
        p = poly + [0]
        for ind in range(1,len(p)) :
            p[ind-1] = p[ind] * ind
        return p[:-1]

    def primitive_const_nul(self, poly):
        p = [0] + poly
        for ind in range(1,len(p)) :
            p[ind] = p[ind] / (ind * 1.)
        return p

    def show(self, poly):
        # BUG : coef negative
        expr = []
        for ind in range(len(poly)) :
            if poly[ind] == 0 :
                continue
            elif poly[ind] == 1 :
                expr = expr + ["X^"+str(ind)]
            else :
                expr = expr + [str(poly[ind]) + "X^"+str(ind)]
        print "+".join(expr)


        
po = PolyN([2,-1,0,1])
print po.poly
print po.poly_dri
print po.poly_pri
po.show(po.poly_dri)
po.show(po.poly_pri)

