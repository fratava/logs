from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


def parser(nombre_archivo):
	f=open(nombre_archivo)
	Listaf=f.readlines()
	campos=["Fecha","Proceso","Descripcion"]
	LogParse=[]
	for Renglon in Listaf:
		Rsplit=Renglon.split(" ")
		fecha={'Mes':Rsplit[0],'Dia':Rsplit[1],"Hora":Rsplit[2]}
		proceso=Rsplit[4]
		descripcion =' '.join(map(str,Rsplit[5:]))
		Rparse=[fecha,proceso,descripcion]
		LogParse.append(dict(zip(campos,Rparse)))

	f.close()
	return LogParse


def parsermail(nombre_archivo):
    f=open(nombre_archivo)
    ListaF=f.readlines()
    Mailparse = []
    campos=["nProceso","Daemon","Fecha","Descripcion"]
    for Renglon in ListaF:
        Rsplit = Renglon.split(" ")
        aux1 = Rsplit[4].split("[")
        if len(aux1)>1:
            nproceso = aux1[1]
            daemon = aux1[0]
        else:
            nproceso = Rsplit[4]
            daemon = 0
        
        fecha = {'Mes':Rsplit[0],'Dia':Rsplit[1],"Hora":Rsplit[2]}
        descripcion =' '.join(map(str,Rsplit[5:]))
        Rparse = [nproceso[0:len(nproceso)-2],daemon,fecha,descripcion]
        Mailparse.append(dict(zip(campos,Rparse)))
    
    f.close()
    return Mailparse

def SFPIU_c(nombre):
    L=parsermail(nombre)
    Camposfp=['Mail']
    FPIU=[]
    for l in L:
        if l['Daemon'] == "postfix/smtp":
            Lfp = l['Descripcion'].split(' ')
            #print Lfp[1].split('to=<')
            if Lfp[1].find("to=<") == 0:
                Mail=Lfp[1]
                #print Mail[4:len(Mail)-2]
                FPIU.append(dict(zip(Camposfp,[Mail[4:len(Mail)-2]])))
    return FPIU


def SFPIU_l(nombre):
    L=parsermail(nombre)
    Camposfp=['Mail']
    FPIU=[]
    for l in L:
        if l['Daemon'] == "postfix/local":
            Lfp = l['Descripcion'].split(' ')
            #print Lfp[1].split('to=<')
            if Lfp[1].find("to=<") == 0:
                Mail=Lfp[1]
                #print Mail[4:len(Mail)-2]
                FPIU.append(dict(zip(Camposfp,[Mail[4:len(Mail)-2]])))
    return FPIU


def SFPIU_e(nombre):
    L=parsermail(nombre)
    Camposfp=['Mail','Fecha']
    FPIU=[]
    for l in L:
        if l['Daemon'] == "postfix/qmgr":
            Lfp = l['Descripcion'].split(' ')
            #print Lfp[1].split('from=<')
            if Lfp[1].find("from=<") == 0:
                Mail=Lfp[1]
                #print Mail[4:len(Mail)-2]
                FPIU.append(dict(zip(Camposfp,[Mail[4:len(Mail)-2]])))
    return FPIU

def SFPIU_s(nombre):
    L=parsermail(nombre)
    Camposfp=['Mail','Fecha']
    FPIU=[]
    for l in L:
        if l['Daemon'] == "spamd":
            Lfp = l['Descripcion'].split(' ')
            if Lfp[1].find("identified") == 0:
                Mail=Lfp[1]
                FPIU.append(dict(zip(Camposfp,[Mail[4:len(Mail)-2]])))
    return FPIU
