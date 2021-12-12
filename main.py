from tkinter import *
import random
import time

random.seed()
window = Tk()
window.geometry("600x400")

particles = {}
addingParticles = False

def heat():
    initParticle = canv.create_oval(165, 195, 170, 200, fill="blue")
    #Encode spin of 0.5 or -0.5
    particles[initParticle] = random.randint(0, 1) - 0.5

def updateParticles():
    removeParticles = []
    for p in particles:
        #Move to the right
        currentCoords = canv.coords(p)
        canv.coords(p, currentCoords[0] + 5, currentCoords[1], currentCoords[2] + 5, currentCoords[3])
        currentCoords = canv.coords(p)
        if canv.coords(p)[0] > magCenter:
            incrementY = 0.5*(currentCoords[0] - magCenter) / (550 - magCenter)
            #Introduce normal distribution
            incrementY += abs(random.gauss(0, 3))
            if particles[p] == 0.5:
                #Go up (incrementY is already positive)
                pass
            elif particles[p] == -0.5:
                #Go down (incrementY needs to be negative)
                incrementY = -incrementY
            
            canv.coords(p, currentCoords[0], currentCoords[1] + incrementY, currentCoords[2], currentCoords[3] + incrementY)

        if canv.coords(p)[0] >= 550:
            removeParticles.append(p)
    for rem in removeParticles:
        particles.pop(rem)
    
    window.after(10, updateParticles)

canv = Canvas(window, height=400, width=600)
title = canv.create_text(300, 20, text="Stern-Gerlach Experiment")

agBlock = canv.create_rectangle(50, 150, 150, 250, fill="#A4A1A0")
agTitle = canv.create_text(95, 195, text="Ag")

filterTop = canv.create_rectangle(200, 40, 210, 180, fill="black")
filterBot = canv.create_rectangle(200, 220, 210, 360, fill="black")

magCenter = 275
magTop = canv.create_polygon(250, 130, 300, 130, magCenter, 180, fill="#A4A1A0")
magBot = canv.create_polygon(250, 270, 300, 270, magCenter, 220, fill="#A4A1A0")

canv.grid(row=0, column=0)

heatButton = Button(window, text="Heat!", width=10, height=2, bg="#e87156", command=heat)
heatButton.place(x=55, y=300)

updateParticles()
window.mainloop()
