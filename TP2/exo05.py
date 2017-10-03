#!/usr/bin/env python

question = "Nom ? nombre ? : "
reponse = raw_input(question)
reponse.replace("\"","")
nom, nombre = "", ""
try :
    (nom,nombre) = reponse.split(",")
    nom, nombre = nom.strip(),nombre.strip()
    if reponse in ("q","Q") :
        print "au revoir !"
    else :
        print "note de <{0}> = <{1}>".format(nom, nombre)
except Exception:
    pass
finally : 
    print "au revoir !"

    

