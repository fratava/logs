from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


#def parser(nombre_archivo):
#    f=open(nombre_archivo)
#    Listaf=f.readlines()
#    campos=["Fecha","Descripcion","IP"]
#    LogParse=[]
#    for Renglon in Listaf:
#        Rsplit=Renglon.split(" ")
#        descripcion=Rsplit[0]
#        fecha=Rsplit[3]
#        ip =' '.join(map(str,Rsplit[5:]))
#        Rparse=[fecha,ip,descripcion]
#        LogParse.append(dict(zip(campos,Rparse)))
#
#    f.close()
#    return LogParse

def parser(nombre_archivo):
    f=open(nombre_archivo)
    Listaf=f.readlines()
    campos=["Fecha","Descripcion","IP","Navegador"]
    LogParse=[]
    for Renglon in Listaf:
        Rsplit=Renglon.split(" ")
        navegador=Rsplit[6]
        #print Rsplit[6]
        descripcion=Rsplit[0]
        fecha=Rsplit[3]
        ip =' '.join(map(str,Rsplit[5:]))
        Rparse=[fecha,ip,descripcion,navegador]
        LogParse.append(dict(zip(campos,Rparse)))

    f.close()
    return LogParse



#def SFPIU(nombre):
#	L=parser(nombre)
#	Camposfp=['Usuario','IP','Puerto']
#	FPIU=[]
#	for l in L:
#		if l['Descripcion'].find("Failed password for invalid user")!=-1:
#			Lfp = l['Descripcion'].split(' ')
#			FPIU.append(dict(zip(Camposfp,[Lfp[5],Lfp[7],Lfp[9]])))
#	return FPIU



def SFPIU(nombre):
    L=parser(nombre)
    Camposfp=['Usuario','IP','Puerto','Descripcion','Navegador']
    FPIU=[]
    for l in L:
        if l['Descripcion'].find("Failed password for invalid user")!=-1:
            Lfp = l['Descripcion'].split(' ')
            FPIU.append(dict(zip(Camposfp,[Lfp[5],Lfp[7],Lfp[9]])))
    return FPIU

