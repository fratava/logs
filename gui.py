#Importamos el modulo para manejar la GUI
# https://wiki.python.org/moin/TkInter
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure
from collections import Counter
import numpy as np
from maillog import *
#from maillog_local import *
from logs import *
import tkFileDialog
import tkMessageBox

import Tkinter as tk
#Definimos tipo de letra
LARGE_FONT = ("Verdana",12)

#Importamos matplotlib 

#Clase principal para el manejo de la Interfaz
#Debe heredar de la clase Tkinter

class AnalizadorLogs(tk.Tk):

#El metodo  __init__ se ejecuta siempre que se utilice un
#objeto de la clase AnalizadorLogs

	def __init__(self,*args,**kargs):
		tk.Tk.__init__(self,*args,**kargs)

		#Definimos un contenedor donde vamnos a mostrar los distintos
		#Frames de nuestra Interfaz (tambien es un Frame).		
		contenedor = tk.Frame(self)
		contenedor.pack(side="top",fill="both",expand=True)
		contenedor.grid_rowconfigure(0,weight=1)
		contenedor.grid_columnconfigure(0,weight=1)
		
		#Diccionario de Frames inicialmete vacio
		self.frames={}
		
		#Almacenamos los frames en el diccionario
		for L in (Inicio,Correo,Conexion,Web,Fecha,Local,Saliente,Request,Spam):
			frame = L(contenedor,self)
			self.frames[L] = frame
			frame.grid(row=0,column=0,sticky="nsew")

		#Usamos el metodo show_frame definido mas abajo 
		#para mostrar el frame
                self.initUI()
		self.show_frame(Inicio)


                #self.parent = parent
                #self.initUI()
                self.aboutUs()
                self.hello()

	#Metodo que muestra un frame
	def show_frame(self,frameshow):
		#Elegimos el frame para mostrar del diccionario frame
		frame=self.frames[frameshow]
		#tkraise() trae el frame  al frente del contenedor
		frame.tkraise()

        ###########################################################
        def initUI(self):
      
                self.title("Analizador de Logs")
        
                menubar = tk.Menu(self)
                self.config(menu=menubar)

                fileHelp= tk.Menu(menubar)
                
                #top = Tkinter.Tk()
                
                fileMenu = tk.Menu(menubar)       
                #fileMenu.add_command(label="Abrir", command=self.onOpen)

                #fileHelp.add_command(label="Acerca de", command=self.onOpen)
                fileHelp.add_command(label="Acerca de", command=self.hello)
                
                #fileMenu.add_separator()
                
                fileMenu.add_command(label="Salir", underline=0, command=self.onExit)
                menubar.add_cascade(label="Archivo", underline=0, menu=fileMenu)
                menubar.add_cascade(label="Ayuda", underline=0, menu=fileHelp) 

                #self.txt = tk.Text(self)
                #self.txt.pack(fill=tk.BOTH, expand=1)

        def hello(self):
            tkMessageBox.showinfo("Acerca de Analizador de Logs", "Desarrollado por: \n Francisco Tapia")



        def onExit(self):
                self.quit()


        def onOpen(self):
        
            ftypes = [('All files', '*')]
            dlg = tkFileDialog.Open(self, filetypes = ftypes)
            fl = dlg.show()
        
            if fl != '':
                    text = self.readFile(fl)
                    self.txt.insert(tk.END, text)

        def aboutUs(self):
            print " "

        def nombre(filename):
            return filename

        def readFile(self, filename):

            f = open(filename, "r")
            text = f.read()
            return text
            

#Clase para el frame de inicio 
#debe heredar de la clase tk.Frame
class Inicio(tk.Frame):
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)


                
		#Creamos una etiqueta con tk.Label
		#label =  tk.Label(self,text="Analizador de Logs",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		#label.pack(pady=10,padx=10)
		
		#Anadimos botones
		boton = tk.Button(self,text="Analizar Conexiones IP",command=lambda:controller.show_frame(Conexion))		
		boton.pack()
		
		boton2 = tk.Button(self,text="Analizar Correos",command=lambda:controller.show_frame(Correo))		
		boton2.pack()
		boton3 = tk.Button(self,text="Analizar Procesos Web",command=lambda:controller.show_frame(Web))		
		boton3.pack()
                boton4 = tk.Button(self,text="Analizar Fechas Web",command=lambda:controller.show_frame(Fecha))		
		boton4.pack()
                boton5 = tk.Button(self,text="Analizar Correo Local",command=lambda:controller.show_frame(Local))		
		boton5.pack()
                boton6 = tk.Button(self,text="Analizar Correo en Espera",command=lambda:controller.show_frame(Saliente))		
		boton6.pack()
                boton7 = tk.Button(self,text="Analizar Requisiciones",command=lambda:controller.show_frame(Request))		
		boton7.pack()
                boton8 = tk.Button(self,text="Analizar Spam",command=lambda:controller.show_frame(Spam))		
		boton8.pack()
                boton9 = tk.Button(self,text="Analizar Fechas5",command=lambda:controller.show_frame(Fecha))		
		boton9.pack()
               
class Conexion(tk.Frame):
        mas_comunes=20
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Conexiones IP",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)

                #
                #self.myentrybox = tk.Entry()
                #self.myentrybox.pack()
                #self.myentrybox.insert(0,"Mas comunes")
                #self.myentrybox.focus()
                #self.myentrybox.bind("<Return>",self.Enter)
		#self.myentrybox.insert(0,"some default value")
                #Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()
                
                nombre_archivo="./access_log"
                categoria="IP"
                #mas_comunes_1= str(self.myentrybox.get())
                #print mas_comunes_1
                mas_comunes=20 
                #mas_com=self.Enter
                #print self.Enter
                #print mas_com

                data_file = parser(nombre_archivo)
                counter = Counter(item[categoria] for item in data_file)
                labels = tuple(counter.keys())
                values = tuple(counter.values())
                most_common=tuple(counter.most_common(mas_comunes))
                value_ip=[]
                #
                for i in range(0,len(most_common)):
                    value_ip.append(most_common[i][1])
                 
                xlocations = np.arange(len(most_common)) + 0.5
                width = 0.5

		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.rand(200000)
    		#a.hist(nm)
                #xlocations, value_ip, width =grafica_conex()
                
                a.bar(xlocations, value_ip, width=width)
                a.set_xticks(xlocations + width / 2)
                a.set_xticklabels(labels, rotation=90)
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
	

       #def Enter(self, event):
       #    """ Someone Pressed Enter """
       #    #print "You entered >> %s" % (self.myentrybox.get())
       #    #return self.myentrybox.get()
       #    #value = int(myentrybox.get())
       #    #mas_comunes.set(int(self.myentrybox.get()))
       #    value=int(self.myentrybox.get())
       #    print value+20
       #    return value

class Correo(tk.Frame):
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Correos",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo_c="maillog"
                categoria_c="Mail"
                mas_comunes_c=20
                
                data_file_c = SFPIU_c(nombre_archivo_c)
                #print data_file_c
                counter_c = Counter(item[categoria_c] for item in data_file_c)
                labels_c = tuple(counter_c.keys())
                values_c = tuple(counter_c.values())
                most_common_c=tuple(counter_c.most_common(mas_comunes_c))
                value_ip_c=[]
                #print most_common_c
                for i in range(0,len(most_common_c)):
                    value_ip_c.append(most_common_c[i][1])
    
                xlocations_c = np.arange(len(most_common_c)) + 0.5
                width_c = 0.5
                
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(200000)
    		#a.hist(nm)
                a.bar(xlocations_c, value_ip_c, width=width_c)
                a.set_xticks(xlocations_c + width_c / 2)
                a.set_xticklabels(labels_c, rotation=90)
                #print xlocations_c
                #print value_ip_c
                #a.xticks(xlocations + width / 2, labels, rotation=90)
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Spam(tk.Frame):
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Spam",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo_c="maillog"
                categoria_c="Mail"
                mas_comunes_c=20
                
                data_file_c = SFPIU_s(nombre_archivo_c)
                #print data_file_c
                counter_c = Counter(item[categoria_c] for item in data_file_c)
                labels_c = tuple(counter_c.keys())
                values_c = tuple(counter_c.values())
                most_common_c=tuple(counter_c.most_common(mas_comunes_c))
                value_ip_c=[]
                #print most_common_c
                for i in range(0,len(most_common_c)):
                    value_ip_c.append(most_common_c[i][1])
    
                xlocations_c = np.arange(len(most_common_c)) + 0.5
                width_c = 0.5
                
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(200000)
    		#a.hist(nm)
                a.bar(xlocations_c, value_ip_c, width=width_c)
                a.set_title('Spam Identificado')
                a.set_ylabel('Numero de Correos Spam')
                #a.text(2, 6, r'an equation: $E=mc^2$')
                #a.set_xticks(labels)
                a.get_xaxis().set_visible(False)
                
                #a.set_xticks(xlocations_c + width_c / 2)
                #a.set_xticklabels(labels_c, rotation=90)
                #print xlocations_c
                #print value_ip_c
                #a.xticks(xlocations + width / 2, labels, rotation=90)
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Web(tk.Frame):
		#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Servidor Web",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo="./access_log"
                categoria="Descripcion"
                mas_comunes=20
                
                data_file = parser(nombre_archivo)
                counter = Counter(item[categoria] for item in data_file)
                labels = tuple(counter.keys())
                values = tuple(counter.values())
                most_common=tuple(counter.most_common(mas_comunes))
                value_ip=[]
                
                for i in range(0,len(most_common)):
                    value_ip.append(most_common[i][1])
                
                xlocations = np.arange(len(most_common)) + 0.5
                width = 0.5
		
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(2000)
    		#a.hist(nm)

                a.bar(xlocations, value_ip, width=width)
                a.set_xticks(xlocations + width / 2)
                a.set_xticklabels(labels, rotation=90)
                #a.set_title('Numero de peticiones web')
                #a.set_ylabel('Numero de peticiones web')
                #a.text(2, 6, r'an equation: $E=mc^2$')
                #a.set_xticks(labels)
                #a.set_ylabel('Y label')
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		#f = Figure(figsize=(5,5	), dpi=100)
    		#a = f.add_subplot(111)
    		#a.bar([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    		#canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
    		#canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Request(tk.Frame):
		#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Peticiones",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo="./access_log"
                categoria="Navegador"
                mas_comunes=20
                
                data_file = parser(nombre_archivo)
                counter = Counter(item[categoria] for item in data_file)
                labels = tuple(counter.keys())
                values = tuple(counter.values())
                most_common=tuple(counter.most_common(mas_comunes))
                value_ip=[]
                
                for i in range(0,len(most_common)):
                    value_ip.append(most_common[i][1])
                
                xlocations = np.arange(len(most_common)) + 0.5
                width = 0.5
		
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(2000)
    		#a.hist(nm)

                a.bar(xlocations, value_ip, width=width)
                a.set_xticks(xlocations + width / 2)
                a.set_xticklabels(labels, rotation=90)
                #a.set_title('Numero de peticiones web')
                #a.set_ylabel('Numero de peticiones web')
                #a.text(2, 6, r'an equation: $E=mc^2$')
                #a.set_xticks(labels)
                #a.set_ylabel('Y label')
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		#f = Figure(figsize=(5,5	), dpi=100)
    		#a = f.add_subplot(111)
    		#a.bar([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    		#canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
    		#canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

                
class Fecha(tk.Frame):
		#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Fechas de Uso del Servidor",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo="./access_log"
                categoria="Fecha"
                mas_comunes=20
                
                data_file = parser(nombre_archivo)
                counter = Counter(item[categoria] for item in data_file)
                labels = tuple(counter.keys())
                values = tuple(counter.values())
                most_common=tuple(counter.most_common(mas_comunes))
                value_ip=[]
                
                for i in range(0,len(most_common)):
                    value_ip.append(most_common[i][1])
                
                xlocations = np.arange(len(most_common)) + 0.5
                width = 0.5
		
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(2000)
    		#a.hist(nm)

                a.bar(xlocations, value_ip, width=width)
                a.set_xticks(xlocations + width / 2)
                a.set_xticklabels(labels, rotation=90)
                #a.set_title('Numero de peticiones web')
                #a.set_ylabel('Numero de peticiones web')
                #a.text(2, 6, r'an equation: $E=mc^2$')
                #a.set_xticks(labels)
                #a.set_ylabel('Y label')
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
		#f = Figure(figsize=(5,5	), dpi=100)
    		#a = f.add_subplot(111)
    		#a.bar([1,2,3,4,5,6,7,8],[5,6,1,3,8,9,3,5])
    		#canvas = FigureCanvasTkAgg(f, self)
		#canvas.show()
    		#canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		#canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Local(tk.Frame):
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Correos Local",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo_c="maillog"
                categoria_c="Mail"
                mas_comunes_c=20
                
                data_file_c = SFPIU_l(nombre_archivo_c)
                #print data_file_c
                counter_c = Counter(item[categoria_c] for item in data_file_c)
                labels_c = tuple(counter_c.keys())
                values_c = tuple(counter_c.values())
                most_common_c=tuple(counter_c.most_common(mas_comunes_c))
                value_ip_c=[]
                #print most_common_c
                for i in range(0,len(most_common_c)):
                    value_ip_c.append(most_common_c[i][1])
    
                xlocations_c = np.arange(len(most_common_c)) + 0.5
                width_c = 0.5
                
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(200000)
    		#a.hist(nm)
                a.bar(xlocations_c, value_ip_c, width=width_c)
                a.set_xticks(xlocations_c + width_c / 2)
                a.set_xticklabels(labels_c, rotation=90)
                #print xlocations_c
                #print value_ip_c
                #a.xticks(xlocations + width / 2, labels, rotation=90)
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

class Saliente(tk.Frame):
	#Metodo __init__ que se ejecuta cuando de crea un objeto Inicio
	def __init__(self,parent,controller):
		tk.Frame.__init__(self,parent)
		#Creamos una etiqueta con tk.Label
		label =  tk.Label(self,text="Analizador de Correos en Espera",font="LARGE_FONT")
		#La anadimos al frame con .pack()
		label.pack(pady=10,padx=10)
		#Anadimos botones
		boton = tk.Button(self,text="Inicio",command=lambda:controller.show_frame(Inicio))		
		boton.pack()

                nombre_archivo_c="maillog"
                categoria_c="Mail"
                mas_comunes_c=20
                
                data_file_c = SFPIU_e(nombre_archivo_c)
                #print data_file_c
                counter_c = Counter(item[categoria_c] for item in data_file_c)
                labels_c = tuple(counter_c.keys())
                values_c = tuple(counter_c.values())
                most_common_c=tuple(counter_c.most_common(mas_comunes_c))
                value_ip_c=[]
                #print most_common_c
                for i in range(0,len(most_common_c)):
                    value_ip_c.append(most_common_c[i][1])
    
                xlocations_c = np.arange(len(most_common_c)) + 0.5
                width_c = 0.5
                
		f = Figure(figsize=(5,5), dpi=100)
    		a = f.add_subplot(111)
		#nm=np.random.randn(200000)
    		#a.hist(nm)
                a.bar(xlocations_c, value_ip_c, width=width_c)
                a.set_xticks(xlocations_c + width_c / 2)
                a.set_xticklabels(labels_c, rotation=90)
                #print xlocations_c
                #print value_ip_c
                #a.xticks(xlocations + width / 2, labels, rotation=90)
    		canvas = FigureCanvasTkAgg(f, self)
		canvas.show()
    		canvas.get_tk_widget().pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
		canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)



#Creamos una instancial Analizador de Logs
root=AnalizadorLogs()
#Loop de la Interfaz
root.mainloop() 
