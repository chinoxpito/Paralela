#!/usr/bin/env python
import sys
import gobject
import pango
# Dirty path adjustment to look for pygtk 2.9 instead of pygtk 2.8
# This needs pygtk 2.9 installed.
sys.path[:0] = ['/usr/local/lib/python2.4/site-packages/gtk-2.0']
import pygtk
pygtk.require('2.0')
import gtk
import os
from gtk import gdk
import ImageFilter
import numpy as np
import time
from numpy import array, shape, reshape, zeros, transpose
from PIL import Image, ImageChops, ImageOps

# DECLARACION DE SUFIJOS PARA VARIABLES RECURRENTES (SOBRENOMBRES)
win = gtk.Window()
wi = gtk.Window()
image = gtk.Image()
im = gtk.Image()
vbox0=gtk.VBox(False,0)
scrolled_window = gtk.ScrolledWindow()
scrolled_window.set_border_width(10)
scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)
global fac
fac = 0
global Paralelo
Paralelo = 100

# FUNCION PARA AGREGAR UNA IMAGEN
def Agregar(event):
    vbox0.remove(image)

    dialog = gtk.FileChooserDialog("Elija la imagen", None, gtk.FILE_CHOOSER_ACTION_OPEN,
                                   (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                    gtk.STOCK_OPEN, gtk.RESPONSE_OK))
    dialog.set_default_response(gtk.RESPONSE_OK)
    filter = gtk.FileFilter()
    filter.set_name("Imagen")
    filter.add_mime_type("image/png")
    filter.add_mime_type("image/jpeg")
    filter.add_mime_type("*.png")
    filter.add_mime_type("*.jpg")
    filter.add_mime_type("*.jpeg")
    dialog.add_filter(filter)
    response = dialog.run()
    if response == gtk.RESPONSE_OK:
        image.set_from_file(dialog.get_filename())
        ima = Image.open(dialog.get_filename())
        ima.save("aux.jpg")
        ima.save("vol.jpg")
        ima.save("Dim.jpg")
        vbox0.pack_start(image)

    elif response == gtk.RESPONSE_CANCEL:
        print "Archivo no seleccionado"
        print  "Saliendo . . ."
        em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR,
                               gtk.BUTTONS_CLOSE, "Error al cargar imagen")
        em.run()
        em.destroy()
        raise SystemExit

    dialog.destroy()

def AgregarMas(event):
    global fac
    print fac
    #vbox0.remove(image)
    if fac < 3:
        dialog = gtk.FileChooserDialog("Elija la imagen", None, gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        filter = gtk.FileFilter()
        filter.set_name("Imagen")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_mime_type("*.png")
        filter.add_mime_type("*.jpg")
        filter.add_mime_type("*.jpeg")
        dialog.add_filter(filter)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            image.set_from_file(dialog.get_filename())
            ima = Image.open(dialog.get_filename())
            name = "mascara"
            fac = fac + 1
            print fac
            name = name + name[fac]
            ima.save(name + ".jpg")
            print name
            #vbox0.pack_start(image)

        elif response == gtk.RESPONSE_CANCEL:
            print "Archivo no seleccionado"
            print  "Saliendo . . ."
            em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR,
                                   gtk.BUTTONS_CLOSE, "Error al cargar imagen")
            em.run()
            em.destroy()
            raise SystemExit

        dialog.destroy()
    if fac == 3:
        fac = 10


def AgregarMasGif(event):
    global fac
    print fac
    # vbox0.remove(image)
    if fac < 5:
        dialog = gtk.FileChooserDialog("Elija la imagen", None, gtk.FILE_CHOOSER_ACTION_OPEN,
                                       (gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL,
                                        gtk.STOCK_OPEN, gtk.RESPONSE_OK))
        dialog.set_default_response(gtk.RESPONSE_OK)
        filter = gtk.FileFilter()
        filter.set_name("Imagen")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpeg")
        filter.add_mime_type("*.png")
        filter.add_mime_type("*.jpg")
        filter.add_mime_type("*.jpeg")
        dialog.add_filter(filter)
        response = dialog.run()
        if response == gtk.RESPONSE_OK:
            image.set_from_file(dialog.get_filename())
            ima = Image.open(dialog.get_filename())
            name = "asdfghj"
            fac = fac + 1
            print fac
            name = name + name[fac]
            ima.save(name + ".jpg")
            print name
            # vbox0.pack_start(image)

        elif response == gtk.RESPONSE_CANCEL:
            print "Archivo no seleccionado"
            print  "Saliendo . . ."
            em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR,
                                   gtk.BUTTONS_CLOSE, "Error al cargar imagen")
            em.run()
            em.destroy()
            raise SystemExit

        dialog.destroy()
    if fac == 5:
        fac = 10


# VENTANA DE ACERCA DE ...
def about_win(widget):
    about = gtk.AboutDialog()
    about.set_program_name("Procesamiento de imagenes")
    about.set_copyright("Laboratorio 1 Computacion Paralela ")
    about.set_comments("Desarrolladores: Acuna - Cerro - Saez - Vasquez.\n Profesor Oscar Magna V. ")
    about.set_website("http://www.utem.cl/")
    about.set_logo(gtk.gdk.pixbuf_new_from_file("utem.jpg"))
    about.run()
    about.destroy()

# FUNCION QUE LLAMA AL CODIGO ROTAR
def Rotar(event):
    import commands
    result=commands.getoutput('/usr/bin/python Rotar.py')
    image.set_from_file('aux.jpg')
    image.show()

def Infrarojo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Infrarojo.py')
    image.set_from_file('aux.jpg')
    image.show()

def Dianoche(event):

    import commands
    result = commands.getoutput('/usr/bin/python Dianoche.py')
    image.set_from_file('aux.jpg')
    image.show()


def Brillo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Brillo.py')
    image.set_from_file('aux.jpg')
    image.show()

def Sepia(event):
    import commands
    result = commands.getoutput('/usr/bin/python Sepia.py')
    image.set_from_file('aux.png')
    image.show()

def Reflejo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Reflejo.py')
    image.set_from_file('aux.jpg')
    image.show()

def RGB(event):
    import commands
    result = commands.getoutput('/usr/bin/python Rgb.py')
    image.set_from_file('aux.jpg')
    image.show()

def Redimensionar(event):
    import commands
    result = commands.getoutput('/usr/bin/python Redimencionar.py')
    image.set_from_file('aux.jpg')
    image.show()

def Agrandar(event):
    import commands
    result = commands.getoutput('/usr/bin/python Agrandar.py')
    image.show()

def Bordes(event):
    import commands
    result = commands.getoutput('/usr/bin/python Bordes.py')
    image.set_from_file('aux.jpg')
    image.show()

def Negativo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Negativo.py')
    image.set_from_file('aux.jpg')
    image.show()

def EscalaGrises(event):
    import commands
    result = commands.getoutput('/usr/bin/python EscalaGrises.py')
    image.set_from_file('aux.jpg')
    image.show()

def Nolineal(event):
    import commands
    result = commands.getoutput('/usr/bin/python Nolineal.py')
    image.set_from_file('aux.jpg')
    image.show()

def Polar(event):
    import commands
    result = commands.getoutput('/usr/bin/python Polar.py')
    image.set_from_file('aux.jpg')
    image.show()

def SumaFoto(event,f):
    global fac
    if fac == 10:
        import commands
        result = commands.getoutput('/usr/bin/python sumaFotosToGIF.py')
        image.set_from_file('Imagenes2/sumaAnimacion.gif')
        fac = 0
        image.show()


def SumaFotoVentana(event):
    global fac
    fac = fac + 1
    wi.set_title("... Suma de fotos a GIF ...")
    wi.set_position(gtk.WIN_POS_CENTER)
    wi.set_size_request(400, 70)

    vboxSu = gtk.VBox(False, 0)
    hboxBot = gtk.HBox(False, 0)
    hboxIma1 = gtk.HBox(False, 0)
    hboxIma2 = gtk.HBox(False, 0)
    hboxIma3 = gtk.HBox(False, 0)

    Dato = gtk.Label()
    Dato.set_text("Agrege 2 imagenes ")

    btnAgrSu = gtk.Button("Agregar")
    btnAgrSu.connect("clicked", AgregarMas)
    btnOk = gtk.Button("Sumar")
    btnOk.connect("clicked", SumaFoto, fac)

    vboxSu.pack_start(Dato, True, False, 1)
    hboxBot.pack_start(btnAgrSu, True, True, 1)
    hboxBot.pack_start(btnOk, True, True, 1)
    vboxSu.pack_start(hboxBot, True, False, 1)

    wi.add(vboxSu)
    wi.show_all()

def Convolucion(event):
    import commands
    result = commands.getoutput('/usr/bin/python convolucion.py')
    image.set_from_file('aux.jpg')
    image.show()

def Mascara(event,f):
    global fac
    if fac == 10:
        import commands
        result = commands.getoutput('/usr/bin/python Mascara.py')
        image.set_from_file('aux.jpg')
        fac = 0
        image.show()

def MascaraVentana(event):
    global fac
    wi.set_title("... Mascara ...")
    wi.set_position(gtk.WIN_POS_CENTER)
    wi.set_size_request(400, 70)

    vboxMa = gtk.VBox(False, 0)
    hboxBot = gtk.HBox(False, 0)
    hboxIma1 = gtk.HBox(False, 0)
    hboxIma2 = gtk.HBox(False, 0)
    hboxIma3 = gtk.HBox(False, 0)

    Dato = gtk.Label()
    Dato.set_text("Agrege 3 imagenes ")

    btnAgrMa = gtk.Button("Agregar")
    btnAgrMa.connect("clicked", AgregarMas)
    btnOk = gtk.Button("Combinar")
    btnOk.connect("clicked", Mascara, fac)

    vboxMa.pack_start(Dato, True, False, 1)
    hboxBot.pack_start(btnAgrMa, True, True, 1)
    hboxBot.pack_start(btnOk, True, True, 1)
    vboxMa.pack_start(hboxBot, True, False, 1)

    wi.add(vboxMa)
    wi.show_all()

def Efectocolor(event):
    import commands
    result = commands.getoutput('/usr/bin/python Efectocolor.py')
    image.set_from_file('aux.jpg')
    image.show()

def ConvAgif(event,f):
    global fac
    im = Image.open("asdfghjd.jpg")
    im.save('Imagenes/asdfghjd.png')
    im = Image.open("asdfghjf.jpg")
    im.save('Imagenes/asdfghjf.png')
    im = Image.open("asdfghjg.jpg")
    im.save('Imagenes/asdfghjg.png')
    im = Image.open("asdfghjh.jpg")
    im.save('Imagenes/asdfghjh.png')
    im = Image.open("asdfghjs.jpg")
    im.save('Imagenes/asdfghjs.png')
    if fac == 10:
        import commands
        result = commands.getoutput('/usr/bin/python toGIF.py')
        image.set_from_file('animacion.gif')
        fac = 0
        image.show()


def GIFventana(event):
    global fac
    wi.set_title("... GIF ...")
    wi.set_position(gtk.WIN_POS_CENTER)
    wi.set_size_request(400, 70)

    vboxGi = gtk.VBox(False, 0)
    hboxBot = gtk.HBox(False, 0)
    hboxIma1 = gtk.HBox(False, 0)
    hboxIma2 = gtk.HBox(False, 0)
    hboxIma3 = gtk.HBox(False, 0)

    Dato = gtk.Label()
    Dato.set_text("Agrege 5 imagenes ")

    btnAgrGi = gtk.Button("Agregar")
    btnAgrGi.connect("clicked", AgregarMasGif)
    btnOk = gtk.Button("Convertir")
    btnOk.connect("clicked", ConvAgif, fac)

    vboxGi.pack_start(Dato, True, False, 1)
    hboxBot.pack_start(btnAgrGi, True, True, 1)
    hboxBot.pack_start(btnOk, True, True, 1)
    vboxGi.pack_start(hboxBot, True, False, 1)

    wi.add(vboxGi)
    wi.show_all()

def Ajustar(even):
    imagenAnchuraMaxima=600
    imagenAlturaMaxima=600
    img = Image.open("aux.jpg")
    width, height = img.size
    img.thumbnail((imagenAnchuraMaxima, imagenAlturaMaxima), Image.ANTIALIAS)
    img.save("Dim.jpg")
    image.set_from_file("Dim.jpg")
    image.show()

def Volver(event):
    image.set_from_file("vol.jpg")
    image.show()
    ima = Image.open("vol.jpg")
    ima.save("aux.jpg")


def activate_cb(button, active):
    # if the button (i.e. the switch) is active, set the title
    # of the window to "Switch Example"
    if button.get_active():
        self.set_title("Switch Example")
    # else, set it to "" (empty string)
    else:
        self.set_title("")


def on_button_toggled(button, name):
    if button.get_active():
        state = "on"
        global Paralelo
        Paralelo = 101
        print Paralelo
    else:
        state = "off"
        Paralelo = 100
        print Paralelo

def main(args):

    win.set_title("... Procesador de Imagenes ...")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(900, 650)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy",gtk.main_quit)
    image.set_from_file("utem.jpg")
    image.show()


    # BOTONES
    btnAgr = gtk.Button("Agregar")
    btnAgr.connect("clicked", Agregar)
    btnAju = gtk.Button("Ajustar")
    btnAju.connect("clicked", Ajustar)
    btnRot = gtk.Button("Rotar")
    btnRot.connect("clicked", Rotar)
    btnVol = gtk.Button("Original")
    btnVol.connect("clicked", Volver)
    btnInf = gtk.Button("Infrarojo")
    btnInf.connect("clicked", Infrarojo)
    btnBri = gtk.Button("Brillo")
    btnBri.connect("clicked", Brillo)
    btnSep = gtk.Button("Sepia")
    btnSep.connect("clicked", Sepia)
    btnDia = gtk.Button("Dia-Noche")
    btnDia.connect("clicked", Dianoche)
    btnRef = gtk.Button("Reflejo")
    btnRef.connect("clicked", Reflejo)
    btnRed = gtk.Button("Redimensionar")
    btnRed.connect("clicked", Redimensionar)
    btnRgb = gtk.Button("RGB")
    btnRgb.connect("clicked", RGB)
    btnAgran = gtk.Button("Agrandar")
    btnAgran.connect("clicked", Agrandar)
    btnBor = gtk.Button("Bordes")
    btnBor.connect("clicked", Bordes)
    btnGris = gtk.Button("Escala Grises")
    btnGris.connect("clicked", EscalaGrises)
    btnNeg = gtk.Button("Negativo")
    btnNeg.connect("clicked", Negativo)
    btnCon = gtk.Button("Convolucion")
    btnCon.connect("clicked", Convolucion)
    btnNol = gtk.Button("No Lineal")
    btnNol.connect("clicked", Nolineal)
    btnEfe = gtk.Button("Efecto color")
    btnEfe.connect("clicked", Efectocolor)
    btnPol = gtk.Button("Polar")
    btnPol.connect("clicked", Polar)
    btnMas = gtk.Button("Mascara")
    btnMas.connect("clicked", MascaraVentana)
    btnSum = gtk.Button("Suma Fotos")
    btnSum.connect("clicked", SumaFotoVentana)
    btnGi = gtk.Button("Convertir a GIF")
    btnGi.connect("clicked", GIFventana)
    btnAce = gtk.Button("Acerca de")
    btnAce.connect("clicked", about_win)
    btnSal = gtk.Button(" Salir")
    btnSal.connect("clicked",gtk.main_quit)
    #btnPara = gtk.ToggleButton("Paralelo")
    #btnPara.connect("toggled", on_button_toggled, 1)


    # ACA SE AGREGAN LOS BOTONES A LA CAJA hbox1
    hbox1 = gtk.HBox(False, 0) # declaracion de hbox1
    hbox2 = gtk.HBox(False,0)
    hbox1.pack_start(btnAgr, False, False, 1)
    hbox1.pack_start(btnEfe, False, False, 1)
    hbox1.pack_start(btnGris, False, False, 1)
    hbox1.pack_start(btnRot, False, False, 1)
    hbox1.pack_start(btnInf, False, False, 1)
    hbox1.pack_start(btnBri, False, False, 1)
    hbox1.pack_start(btnSep, False, False, 1)
    hbox1.pack_start(btnDia, False, False, 1)
    hbox1.pack_start(btnRef, False, False, 1)
    hbox1.pack_start(btnRgb, False, False, 1)
    hbox1.pack_start(btnRed, False, False, 1)
    hbox1.pack_start(btnCon, False, False, 1)
    hbox2.pack_start(btnPol, False, False, 1)
    hbox2.pack_start(btnNol, False, False, 1)
    hbox2.pack_start(btnBor, False, False, 1)
    hbox2.pack_start(btnNeg, False, False, 1)
    hbox2.pack_start(btnMas, False, False, 1)
    hbox2.pack_start(btnSum, False, False, 1)
    hbox2.pack_start(btnGi, False, False, 1)
    hbox2.pack_start(btnAju, False, False, 1)
    hbox2.pack_start(btnVol, False, False, 1)
    hbox2.pack_start(btnAgran, False, False, 1)
    hbox2.pack_start(btnAce, False, False, 1)
    hbox2.pack_start(btnSal, False, False, 1)
    #hbox2.pack_start(btnPara, False, False, 1)


    vbox0.pack_start(hbox1,False,False,1) # SE GENERA UN ESPACIO Y SE LE INCLUYEN LOS BOTONES
    vbox0.pack_start(hbox2, False, False, 1)
    vbox0.pack_start(image)

    win.add(vbox0)
    win.show_all()
    gtk.main()


    return True

if __name__ == '__main__':
    sys.exit(main(sys.argv))