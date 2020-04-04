from PIL import Image
from notify_run import Notify
import pyscreenshot as ImageGrab
import pyautogui
import keyboard
import time

notify = Notify()
x,y = 0,0
sair=False

def get_coordenadas():
    print("Selecione com o mouse e aperte 'x' para pegar as coordenadas x,y")
    while True:
            if keyboard.is_pressed('x'):
                global x,y
                x,y = pyautogui.position()
                print("x="+str(x)+",y="+str(y))   
                break
    print("Alvo selecionado. Tirando screenshot e pegando a cor do pixel...")

get_coordenadas()
im=ImageGrab.grab(bbox=(x,y,x+10,y+10))
filename="C:\\Users\\Jam\\Desktop\\cor.png"
im.save(filename)
print("Screenshot salva. Pegando a cor do pixel.")

image = Image.open(filename)
coordinate = xx, yy = 5, 5
rgba = image.getpixel(coordinate)
print("rgba = "+str(rgba))
print("Monitorando as coordenadas...")

while True:
    im=ImageGrab.grab(bbox=(x,y,x+10,y+10))
    im.save(filename)
    image = Image.open(filename)
    rgba_at = image.getpixel(coordinate)
    
    if rgba_at == rgba:
        print("Não há ninguém.")
        time.sleep(1)
    else:
        print("Tem alguém.")
        notify.send('Um cliente chegou! :D')
        print("Digite 'x' para continuar monitorando ou 'q' para sair...")
        while True:
            if keyboard.is_pressed('x'):
                break
            elif keyboard.is_pressed('q'):
                sair=True
                break
    if sair==True:
        break