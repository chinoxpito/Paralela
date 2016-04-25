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
    imagenAnchuraMaxima = 600
    imagenAlturaMaxima = 600

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

def Brillo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Brillo.py')
    image.set_from_file('aux.jpg')
    image.show()

def Reflejo(event):
    import commands
    result = commands.getoutput('/usr/bin/python Reflejo.py')
    image.set_from_file('aux.jpg')
    image.show()

def Xxx(event):
    import commands
    result = commands.getoutput('/usr/bin/python wea.py')
    image.show()


def Ajustar(even):
    imagenAnchuraMaxima=600
    imagenAlturaMaxima=600
    img = Image.open("aux.jpg")
    width, height = img.size
    print height
    print width
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
    btn1 = gtk.Button("Agregar")
    btn1.connect("clicked", Agregar)
    btnA = gtk.Button("Ajustar")
    btnA.connect("clicked", Ajustar)
    btn3 = gtk.Button("Invertir")
    btn3.connect("clicked", Invertir)
    btn4 = gtk.Button("Rotar")
    btn4.connect("clicked", Rotar)
    btn5 = gtk.Button("Volver")
    btn5.connect("clicked", Volver)
    btn6 = gtk.Button("Infrarojo")
    btn6.connect("clicked", Infrarojo)
    btn8 = gtk.Button("Brillo")
    btn8.connect("clicked", Brillo)
    btn9 = gtk.Button("Reflejo")
    btn9.connect("clicked", Reflejo)

    btn7 = gtk.Button("XXX")
    btn7.connect("clicked", Xxx)


    btna = gtk.Button("Acerca de")
    btna.connect("clicked", about_win)
    btn2 = gtk.Button(" Salir")
    btn2.connect("clicked",gtk.main_quit)

    # ACA SE AGREGAN LOS BOTONES A LA CAJA hbox1
    hbox1 = gtk.HBox(False, 0) # declaracion de hbox1
    hbox1.pack_start(btn1, False, False, 1)
    hbox1.pack_start(btnA, False, False, 1)
    hbox1.pack_start(btn3, False, False, 1)
    hbox1.pack_start(btn4, False, False, 1)
    hbox1.pack_start(btn6, False, False, 1)
    hbox1.pack_start(btn8, False, False, 1)
    hbox1.pack_start(btn9, False, False, 1)

    hbox1.pack_start(btn5, False, False, 1)
    hbox1.pack_start(btn7, False, False, 1)
    hbox1.pack_start(btna, False, False, 1)
    hbox1.pack_start(btn2, False, False, 1)


    vbox0.pack_start(hbox1,False,False,10) # SE GENERA UN ESPACIO Y SE LE INCLUYEN LOS BOTONES
    vbox0.pack_start(image)

    #table = gtk.Table(2, 1, True)

    #table.attach(image,0,1,0,1)
    #table.add(vbox0)



    win.add(vbox0)
    win.show_all()
    gtk.main()

    return True

if __name__ == '__main__':
    sys.exit(main(sys.argv))