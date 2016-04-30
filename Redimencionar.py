# -*- coding: cp1252 -*-
__author__ = 'Luis Miguel leon'
import numpy as np
from PIL import Image
import time
import pygtk
pygtk.require('2.0')
import gtk

win = gtk.Window()

def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def redimencionarImg(img,img2):
    ancho=img.size[0]
    alto=img.size[1]
    finalAncho=img2.size[0]
    finAlto= img2.size[1]
    print ancho
    print alto
    print finalAncho
    print finAlto
    distanX = (ancho-1)/float(finalAncho)
    distanY = (alto-1) /float(finAlto)
    arrImg=convertirImgMatrixRGB(img)
    arrImg2=convertirImgMatrixRGB(img2)



    print "*********************"

    print "*********************"
    print distanX
    print distanY

#   Proceso de redimensionado
    for i in range(finAlto-1 ):
        for j in range(finalAncho-1 ):
            #Variables x y dependiendo de resolucion de salida.

            x = (distanX * j);
            y = (distanY * i);

            #Tomo pixeles adyacentes, dependiendo de la resolucion que debo entregar.
            a = arrImg[y] [x]
            b = arrImg[y+1][x]
            c = arrImg[y][x+1]
            d = arrImg[y+1][x+1]




            #Direfencia entre distancia y el pixel que esta.
            diferX = (distanX * j) - x;
            diferY = (distanY * i) - y;
            # color azul
            blue =  ((a[2])&0xff)*(1-diferX)*(1-diferY) + ((b[2])&0xff)*(diferX)*(1-diferY) + ((c[2])&0xff)*(diferY)*(1-diferX) + ((d[2])&0xff)*(diferX*diferY)

            # color verde
            green = ((a[1])&0xff)*(1-diferX)*(1-diferY) + ((b[1])&0xff)*(diferX)*(1-diferY) + ((c[1])&0xff)*(diferY)*(1-diferX) + ((d[1])&0xff)*(diferX*diferY)

            # color rojo
            red =   ((a[0])&0xff)*(1-diferX)*(1-diferY) + ((b[0])&0xff)*(diferX)*(1-diferY) + ((c[0])&0xff)*(diferY)*(1-diferX) + ((d[0])&0xff)*(diferX*diferY)

            nuevoPixel = arrImg2[i][j]
            nuevoPixel[0]=red
            nuevoPixel[1]=green
            nuevoPixel[2]=blue

            arrImg2[i][j] = nuevoPixel;

    imgRedimencionada=Image.fromarray(arrImg2)
    return imgRedimencionada

def valor(widget,spin1, spin2):
    factor1 = spin1.get_value()
    factor2 = spin2.get_value()

    print  int(factor1)

    imag = Image.open("aux.jpg")
    # Tamaño de imagen tiene que estar en la misma escala que la original.
    imag = imag.resize((int(factor2), int(factor1)),Image.ANTIALIAS)  # para crear una imagen en blanco con la cual obtengo el tamaño de la final de la imagen redimencionada.
    imag.save("aux.jpg")

    img = Image.open("aux.jpg")
    img2 = Image.open("aux.jpg")

    starting_point = time.time()
    imgRedimencionada = redimencionarImg(img, img2)
    imgRedimencionada.save("aux.jpg")

    elapsed_time = time.time() - starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)
    imgRedimencionada.show()
    win.destroy()

def main():
    win.set_title("Redimencionar")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(400, 110)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy", gtk.main_quit)

    vbox1 = gtk.VBox(False, 0)
    hboxDat = gtk.HBox(False, 0)
    hboxAlt = gtk.HBox(False, 0)
    hboxAnc = gtk.HBox(False, 0)

    img = Image.open("aux.jpg")

    width, height = img.size
    print width #ancho
    print  height #alto

    Dato = gtk.Label()
    Dato.set_text("Dimension original (Alto x Ancho): %s" %height + " x %s" %width)
    Alto = gtk.Label()
    Alto.set_markup("Alto  ")
    Ancho = gtk.Label()
    Ancho.set_markup("Ancho")

    adjAlt = gtk.Adjustment(0, 0, 2000, 1, 0, 0)
    spinner1 = gtk.SpinButton(adjAlt, 1, 0)
    spinner1.set_wrap(True)

    adjAnc = gtk.Adjustment(0, 0, 2000, 1, 0, 0)
    spinner2 = gtk.SpinButton(adjAnc, 1, 0)
    spinner2.set_wrap(True)

    btn1 = gtk.Button("ok")
    btn1.connect("clicked", valor, spinner1, spinner2)

    hboxDat.pack_start(Dato, True, False, 1)
    hboxAlt.pack_start(Alto, True, False, 1)
    hboxAlt.pack_start(spinner1, True, False, 1)
    hboxAnc.pack_start(Ancho, True, False, 1)
    hboxAnc.pack_start(spinner2, True, False, 1)

    vbox1.pack_start(hboxDat, True, True, 1)
    vbox1.pack_start(hboxAlt, True, True, 1)
    vbox1.pack_start(hboxAnc, True, True, 1)
    vbox1.pack_start(btn1, True, True, 1)

    win.add(vbox1)
    win.show_all()
    gtk.main()
main()










