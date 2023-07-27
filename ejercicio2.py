import numpy as np
import cv2

def linea(lado):
    im = np.zeros((lado,lado,3), np.uint8)
    im[:,:] = [0,0,255]
    tamaño = int(lado*0.75)
    x = (lado - tamaño) //2
    y = (lado - tamaño) //2
    im[y:y + tamaño, x:x + tamaño]= [0,255,0]
    tamaño2 = int(tamaño*0.65)
    x1 = (tamaño - tamaño2) //2 + x
    y1 = (tamaño - tamaño2) //2 + y
    im[y1:y1 + tamaño2, x1:x1 + tamaño2]= [255,0,0]
    tamaño3 = int(tamaño2*0.5)
    x2 = (tamaño2 - tamaño3) //2 + x1
    y2 = (tamaño2 - tamaño3) //2 + y1
    im[y2:y2 + tamaño3, x2:x2 + tamaño3]= [0,0,0]

    cv2.imwrite('ejercicio2.png', im)

linea(100)