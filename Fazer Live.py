
#Segue Projeto que fiz na época que eu fazia lives


from tkinter import *
import pyautogui
import os
import time
####


root = Tk()
root.title("Abrir OBS para fazer Live")
root.iconbitmap("C:/Users/lucah/Downloads/twitch--v1.png")
root.geometry("976x511")
bg = PhotoImage(file = "C:/Users/lucah/Downloads/twitch--v1.png")
bg2 = PhotoImage(file = "C:/Users/lucah/Downloads/1024px-OBS.svg (1).png")
label1 = Label(root, image = bg)
label1.place(x = 0, y = 50)
label2 = Label (root, image = bg2)
label2.place(x = 530, y = 50)
def abrir_obs() :
    os.startfile("C:/Users/lucah/Desktop/Jogos/OBS Studio.lnk")

def apex():
    abrir_obs()
    time.sleep(7)
    ### Vai abrir o OBS. ###


    jogo = ("Apex Legends")

    titulo = ("PT:EN// Alta gameplay no Apex Solo, SO CHEGA! // !sociais ")
    notificacao = ("Apexzinho solo, alta gameplay, COLA!!!")

    pyautogui.click(x=117, y=206)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(titulo)
    ### Vai clicar no título e colocar o mesmo. ###

    time.sleep(0.5)
    pyautogui.click(x=101, y=337)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(notificacao)
    ### Vai clicar na notificação e colocar a mesma. ###

    time.sleep(0.5)
    pyautogui.click(x=141, y=437)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(jogo)
    time.sleep(1)
    pyautogui.click(x=95, y=483)
    ### Vai clicar no jogo e colocar o mesmo. ###

    pyautogui.click(x=114, y=814)
    time.sleep(0.5)
    pyautogui.click(x=47, y=873)
    ### Vai atualizar as informações ###

def warzone() :
    abrir_obs()
    time.sleep(7)
    ### Vai abrir o OBS. ###

    jogo = ("COD")
    titulo = ("PT:EN// High Level gameplay no Warzone, SO CHEGA! // !sociais ")
    notificacao = ("Warzonezinho , alto nível de gameplay. COLA!!!")

    pyautogui.click(x=117, y=206)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(titulo)
    ### Vai clicar no título e colocar o mesmo. ###

    time.sleep(0.5)
    pyautogui.click(x=101, y=337)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(notificacao)
    ### Vai clicar na notificação e colocar a mesma. ###

    time.sleep(0.5)
    pyautogui.click(x=141, y=437)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(jogo)
    time.sleep(1)
    pyautogui.click(x=95, y=483)
    ### Vai clicar no jogo e colocar o mesmo. ###

    pyautogui.click(x=114, y=814)
    time.sleep(0.5)

    pyautogui.click(x=36, y=888)
    ### Vai trocar a cena ###

def valorant():
    abrir_obs()
    time.sleep(7)
    ### Vai abrir o OBS. ###

    
    jogo = ("Valorant")
    titulo = ("PT:EN// High elo gameplay no volante, SO CHEGA! // !sociais ")
    notificacao = ("Volantezinho, COLA!!!")

    pyautogui.click(x=117, y=206)
    time.sleep(0.5)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(titulo)
    ### Vai clicar no título e colocar o mesmo. ###

    time.sleep(0.5)
    pyautogui.click(x=101, y=337)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(notificacao)
    ### Vai clicar na notificação e colocar a mesma. ###

    time.sleep(0.5)
    pyautogui.click(x=141, y=437)
    time.sleep(0.3)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.typewrite(jogo)
    time.sleep(1)
    pyautogui.click(x=95, y=483)
    ### Vai clicar no jogo e colocar o mesmo. ###

    pyautogui.click(x=114, y=814)
    time.sleep(0.5)

    pyautogui.click(x=44, y=854)
    ### Vai trocar a cena ###


my_label = Label(root, text="Clique no jogo que quer fazer live.", font=("Arial", 22))
my_label.pack (pady=10)

my_button = Button(root, text="Apex", font=("Arial", 15), command=apex)
my_button1 = Button(root, text="Warzone", font=("Arial", 15), command=warzone)
my_button2 = Button(root, text="Valorant", font=("Arial", 15), command=valorant)
my_button.pack (pady=30)
my_button1.pack (pady=30)
my_button2.pack (pady=30)
root.mainloop()

