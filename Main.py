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


win = gtk.Window()
image = gtk.Image()
ima = gtk.Image()
vbox0=gtk.VBox(False,0)
vbox7=gtk.VBox(False,0)

def make_image_from_file(fname):
  im = gtk.Image()
  im.set_from_file(fname)
  return im


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

def Rotar(event):
    import commands
    result=commands.getoutput('/usr/bin/python rotar.py')
    print "caca"

def ventana(img):
    window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    window.set_position(gtk.WIN_POS_CENTER)
    window.set_size_request(600, 600)
    window.set_title(". . . P R U E B A . . .")

    box = gtk.VBox(False,0)
    box.pack_start(img)
    window.add(box)
    window.show_all()
    window.connect("destroy", self.destroy)

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
        # self.pix = gtk.gdk.pixbuf_new_from_file(dialog.get_filename())
        # self.pix = self.pix.scale_simple(640, 480, gtk.gdk.INTERP_BILINEAR)
        image.set_from_file(dialog.get_filename())
        vbox0.pack_start(image)
        ima = Image.open(dialog.get_filename())
        ima.save("imagenaux.jpg")

    elif response == gtk.RESPONSE_CANCEL:
        print "Archivo no seleccionado"
        print  "Saliendo . . ."
        em = gtk.MessageDialog(None, gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_ERROR,
                               gtk.BUTTONS_CLOSE, "Error al cargar imagen")
        em.run()
        em.destroy()
        raise SystemExit
    dialog.destroy()

def Invertir(event):
    #print "cacaINVERTIR"
    import commands
    result = commands.getoutput('/usr/bin/python Invertir.py')
    image.set_from_file('imageninvertida.png')
    image.show()

def Infrarojo(event):
    #print "cacaINVERTIR"
    import commands
    result = commands.getoutput('/usr/bin/python Infrarojo.py')
    image.set_from_file('final.png')
    image.show()

def Volver(event):
    image.set_from_file("imagenaux.jpg")
    image.show()

def main(args):

    win.set_title("... APLIKA ...")
    win.set_position(gtk.WIN_POS_CENTER)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy",gtk.main_quit)


    image.set_from_file("utem.jpg")
    image.show()


    btn1 = gtk.Button("Agregar")
    btn1.connect("clicked", Agregar)
    btn3 = gtk.Button("Invertir")
    btn3.connect("clicked", Invertir)
    btn4 = gtk.Button("Rotar")
    btn4.connect("clicked", Rotar)
    btn5 = gtk.Button("Volver")
    btn5.connect("clicked", Volver)
    btn6 = gtk.Button("Infrarojo")
    btn6.connect("clicked", Infrarojo)
    btna = gtk.Button("Acerca de")
    btna.connect("clicked", about_win)
    btn2 = gtk.Button(" Salir")
    btn2.connect("clicked",gtk.main_quit)


    hbox1 = gtk.HBox(False, 0)
    hbox1.pack_start(btn1, False, False, 10)
    hbox1.pack_start(btn3, False, False, 10)
    hbox1.pack_start(btn4, False, False, 10)
    hbox1.pack_start(btn6, False, False, 10)
    hbox1.pack_start(btn5, False, False, 10)
    hbox1.pack_start(btna, False, False, 10)
    hbox1.pack_start(btn2, False, False, 10)




    vbox0.pack_start(hbox1,False,False,10)
    vbox0.pack_start(image)


    win.add(vbox0)
    win.show_all()
    gtk.main()

    return True

if __name__ == '__main__':
    sys.exit(main(sys.argv))