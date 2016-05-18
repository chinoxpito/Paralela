import ImageFilter
import numpy as np
import time
from numpy import array, shape, reshape, zeros, transpose
from PIL import Image, ImageChops, ImageOps
import gtk

win = gtk.Window()
# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))

def rotar90(widget,img,fac):

    arrImg = convertirImgMatrixRGB(img)
    n = img.size[0]
    m = img.size[1]
    final = np.array(Image.new("RGB",(m,n)))
    for i in range(n): #fila
        for j in range(m): #columna
            final[i][j] = arrImg[::, ((i*-1)-1)][j]
    imgColor = Image.fromarray(final)
    imgColor.save("aux.jpg")

    if fac == 0:
        win.destroy()
        return imgColor
    else:
        return imgColor


def rotar180(widget,img):
    imgTrans = rotar90(rotar90, img, 1)
    imgTrans = rotar90(rotar90, imgTrans, 0)
    return imgTrans #debido a que el algoritmo de cambio de posicion es el mismo

def rotar270(widget,img):
    imgTrans = rotar180(rotar90,img)
    imgTrans = rotar90(rotar90, imgTrans, 0)
    return imgTrans

def Salir(event):
    win.destroy()

def main(): #Comentar el que no se quiera utilizar

    win.set_title("Rotar")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(600, 50)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy", gtk.main_quit)

    hbox1 = gtk.HBox(False, 0)

    img = Image.open("aux.jpg")

    btnR90Izq = gtk.Button("90 Izq")
    btnR90Izq.connect("clicked", rotar90, img, 0)
    btnR90Der = gtk.Button("90 Der")
    btnR90Der.connect("clicked", rotar270, img)
    btnR180 = gtk.Button("180")
    btnR180.connect("clicked", rotar180, img)
    btnR270 = gtk.Button("270")
    btnR270.connect("clicked", rotar270, img)
    btnRSal = gtk.Button("Salir")
    btnRSal.connect("clicked", Salir)

    hbox1.pack_start(btnR90Izq, True, True, 1)
    hbox1.pack_start(btnR90Der, True, True, 1)
    hbox1.pack_start(btnR180, True, True, 1)
    hbox1.pack_start(btnR270, True, True, 1)
    hbox1.pack_start(btnRSal, True, True, 1)

    win.add(hbox1)
    win.show_all()
    gtk.main()


main()