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
image = gtk.Image()
vbox0=gtk.VBox(False,0)
scrolled_window = gtk.ScrolledWindow()
scrolled_window.set_border_width(10)
scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_ALWAYS)

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

# VENTANA DE ACERCA DE ...
def about_win(widget):
    about = gtk.AboutDialog()
    about.set_program_name("WEAS DE IMAGEN APLIQUEICHON ")
    about.set_version("1.0")
    about.set_copyright("DISTRIBUCION LIBRE !!! Ni ahi con el copyright ")
    about.set_comments("Desarrolladores: Chinaski - Belaly - Borincho - Kathi ")
    about.set_website("https://www.facebook.com/chinoxpito")
    about.set_logo(gtk.gdk.pixbuf_new_from_file("utem.jpg"))
    about.run()
    about.destroy()

# FUNCION QUE LLAMA AL CODIGO ROTAR
def Rotar(event):
    import commands
    result=commands.getoutput('/usr/bin/python Rotar.py')
    image.set_from_file('aux.jpg')
    image.show()

def Invertir(event):
    import commands
    result = commands.getoutput('/usr/bin/python Invertir.py')
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

def Sepia(event): #Problemas con formato de imagen al apretar el boton ORIGINAL
    import commands
    result = commands.getoutput('/usr/bin/python Sepia.py')
    image.set_from_file('aux.png')
    image.show()

def Reflejo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Reflejo.py')
    image.set_from_file('aux.jpg')
    image.show()

def Agrandar(event):
    import commands
    result = commands.getoutput('/usr/bin/python Agrandar.py')
    image.show()


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


def main(args):

    win.set_title("... APLIKA ...")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(800, 650)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy",gtk.main_quit)
    image.set_from_file("utem.jpg")
    image.show()


    # BOTONES
    btnAgr = gtk.Button("Agregar")
    btnAgr.connect("clicked", Agregar)
    btnAju = gtk.Button("Ajustar")
    btnAju.connect("clicked", Ajustar)
    btnInv = gtk.Button("Invertir")
    btnInv.connect("clicked", Invertir)
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
    btnAgran = gtk.Button("Agrandar")
    btnAgran.connect("clicked", Agrandar)
    btnAce = gtk.Button("Acerca de")
    btnAce.connect("clicked", about_win)
    btnSal = gtk.Button(" Salir")
    btnSal.connect("clicked",gtk.main_quit)

    # ACA SE AGREGAN LOS BOTONES A LA CAJA hbox1
    hbox1 = gtk.HBox(False, 0) # declaracion de hbox1
    hbox2 = gtk.HBox(False,0)
    hbox1.pack_start(btnAgr, False, False, 1)
    hbox1.pack_start(btnAju, False, False, 1)
    hbox1.pack_start(btnInv, False, False, 1)
    hbox1.pack_start(btnRot, False, False, 1)
    hbox1.pack_start(btnInf, False, False, 1)
    hbox1.pack_start(btnBri, False, False, 1)
    hbox1.pack_start(btnSep, False, False, 1)
    hbox1.pack_start(btnDia, False, False, 1)
    hbox1.pack_start(btnRef, False, False, 1)

    hbox1.pack_start(btnVol, False, False, 1)
    hbox1.pack_start(btnAgran, False, False, 1)
    hbox2.pack_start(btnAce, False, False, 1)
    hbox2.pack_start(btnSal, False, False, 1)


    vbox0.pack_start(hbox1,False,False,1) # SE GENERA UN ESPACIO Y SE LE INCLUYEN LOS BOTONES
    vbox0.pack_start(hbox2, False, False, 1)
    vbox0.pack_start(image)

    win.add(vbox0)
    win.show_all()
    gtk.main()

    return True

if __name__ == '__main__':
    sys.exit(main(sys.argv))