# spam.py 
eggs = "beans"


departements = { 
    'ain' : (1, 'Bourg-en-Bresse'), 
    'aisne' : (2, 'Laon'), 
    'allier' : (3, 'Moulins') 
    # etc.. 
}

n = 4 
u = None

if 10 in [1, 2, 3]: 
    print 'oui' if n-4 else 'non' 
else: 
    print 'oui' if not u else 'non'

print "--------"

if 'a' in 'spam': 
    if n - 4: 
        print 'oui' 
    else: 
        print 'non'
        
print "--------"

if 'a' in 'spam': 
    if n == 10: 
        print 'non' 
else: 
    print 'oui'

compteur = 0 
for temoin in [ [], True, {}, "", None, False ] +range(5): 
    if temoin: 
        compteur += 1 
print compteur
