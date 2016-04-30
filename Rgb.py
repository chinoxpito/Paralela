__author__ = 'Fco_Hernan'

import numpy as np
from PIL import Image
import time
import pygtk
pygtk.require('2.0')
import gtk

win = gtk.Window()

def scale_set_default_values(scale):
    scale.set_update_policy(gtk.UPDATE_CONTINUOUS)
    scale.set_digits(1)
    scale.set_value_pos(gtk.POS_TOP)
    scale.set_draw_value(True)

# convierte una imagen tipo Imagen (de la libreria PIL) en una matriz(ETD) con la informacion RGB de la imagen
def convertirImgMatrixRGB(img):
    return np.array(img.convert("RGB"))


# procedimiento : Suma los componentes R, G, B del pixel de la imagen con el color que se quiere
# y cada suma se divide en dos, obteniendo un promedio
def mezclarRGB(img,r,g,b):
    arrImg=convertirImgMatrixRGB(img)
    for i in range(img.size[1]):
        for j in range(img.size[0]):
            arrImg[i][j][0] = (arrImg[i][j][0]+r)/2
            arrImg[i][j][1] = (arrImg[i][j][1]+g)/2
            arrImg[i][j][2] = (arrImg[i][j][2]+b)/2
    imgRGB=Image.fromarray(arrImg)
    return imgRGB
def valor(widget,hR,hG,hB):
    factorR = hR.get_value()
    factorG = hG.get_value()
    factorB = hB.get_value()

    img = Image.open("aux.jpg")

    # r,g,b componentes del color a mezclar en decimales
    # 255,0,0 rojo
    r = factorR
    g = factorG
    b = factorB
    starting_point = time.time()
    imgRGB = mezclarRGB(img, r, g, b)
    imgRGB.save("aux.jpg")  # guarda la imagen RGB
    elapsed_time = time.time() - starting_point
    print ""
    print "Serial Time [seconds]: " + str(elapsed_time)
    imgRGB.show()
    win.destroy()

def main():

    win.set_title("RGB")
    win.set_position(gtk.WIN_POS_CENTER)
    win.set_size_request(400, 200)
    win.connect('delete-event', gtk.main_quit)
    win.connect("destroy", gtk.main_quit)

    hboxR = gtk.HBox(False, 0)
    hboxG = gtk.HBox(False, 0)
    hboxB = gtk.HBox(False, 0)
    vbox2 = gtk.VBox(False, 0)

    adj1 = gtk.Adjustment(0, 0, 255, 0, 0, 0)
    hscale = gtk.HScale(adj1)
    hscale.set_size_request(300, 20)

    adj2 = gtk.Adjustment(0, 0, 255, 0, 0, 0)
    hscale2 = gtk.HScale(adj2)
    hscale2.set_size_request(300, 20)

    adj3 = gtk.Adjustment(0, 0, 255, 0, 0, 0)
    hscale3 = gtk.HScale(adj3)
    hscale3.set_size_request(300, 20)
   # scale_set_default_values(hscale)

    #self.hscale.show()


    labelR = gtk.Label()
    labelR.set_markup("Rojo")
    labelG = gtk.Label()
    labelG.set_markup("Verde")
    labelB = gtk.Label()
    labelB.set_markup("Azul")

    btn1 = gtk.Button("ok")
    btn1.connect("clicked", valor, hscale, hscale2, hscale3)

    hboxR.add(labelR)
    hboxR.add(hscale)
    hboxG.add(labelG)
    hboxG.add(hscale2)
    hboxB.add(labelB)
    hboxB.add(hscale3)

    vbox2.pack_start(hboxR, True, True, 1)
    vbox2.pack_start(hboxG, True, True, 1)
    vbox2.pack_start(hboxB, True, True, 1)
    vbox2.pack_start(btn1, True, True, 1)

    #hbox1.add(vbox2)
    #vbox2.pack_start(hscale, True, True, 1)
    #vbox2.pack_start(hscale2, True, True, 1)
    #vbox2.pack_start(hscale3, True, True, 1)
    #hbox1.pack_start(btn1, True, True, 1)
    win.add(vbox2)

    win.show_all()
    gtk.main()

main()