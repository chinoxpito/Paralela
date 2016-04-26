from __future__ import division

import numpy as np
from PIL import Image
from PIL import ImageEnhance
import gtk
import time #Libreria

win = gtk.Window()
factor = 0.00
# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


#Trabajando en como matriz siempre
def aplicarBrillo(img,factor):
    arrImg=convertirImgMatrixRGB(img)
    #si el factor es menor a cero la imagen se oscurece (rango 0 a -1)
    if factor <0:#para oscurecer la imagen
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x*(1+factor)
                arrImg[i][j]=brillo(arrImg[i][j])
    #si el factor es mayor a cero se aclara (rango 0 a 1)
    else:#brillo
        for i in range(img.size[1]):
            for j in range(img.size[0]):
                brillo= lambda x: x+ (255-x)*factor
                arrImg[i][j]=brillo(arrImg[i][j])
    imgBrillante=Image.fromarray(arrImg)#se devuelve la matriz a imagen
    return imgBrillante

def valor(widget,spin):
    factor = spin.get_value()
    print factor
    img = Image.open("aux.jpg")
    starting_point = time.time()  # Donde quiere empezar a calcular el tiempo
    imgBrillo = aplicarBrillo(img, factor)
    imgBrillo.save("aux.jpg")
    elapsed_time = time.time() - starting_point  # calculo
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)  # segundos
    imgBrillo.show()
    win.destroy()


def main():

    win.set_title("Brillo")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(600, 80)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy", gtk.main_quit)

    hbox1= gtk.HBox(False, 0)
    adj = gtk.Adjustment(0.0, -1.0, 1.0, 0.1, 1.0, 0.0)
    spinner1 = gtk.SpinButton(adj, 1.0, 2)
    spinner1.set_wrap(True)


    label = gtk.Label()
    label.set_markup("<big>Ingrese factor\n</big>"
                      "<small>(se debe ingresar valor decimal entre -1 y 0 para oscurecer y entre 0 y 1 para aclarar)</small>")

    btn1 = gtk.Button("ok")
    btn1.connect("clicked",valor,spinner1)

    hbox1.add(label)
    hbox1.pack_start(spinner1, True, True, 1)
    hbox1.pack_start(btn1, True, True, 1)
    win.add(hbox1)
    win.show_all()
    gtk.main()

main() #donde realiza las acciones para el brillo