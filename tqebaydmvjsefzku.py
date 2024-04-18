import yagmail
from tkinter import *
import threading
import random


window=Tk()


sujets = [
    "Le chat", "La girafe", "Un pingouin", "Une licorne", "Le président", "Une pomme", 
    "Un kangourou", "La lune", "Un astronaute", "Une soucoupe volante", "Un ninja", 
    "Un dinosaure", "Un vampire", "Un robot", "Un fantôme", "Un pirate", "Un extraterrestre",
    "Une princesse", "Un magicien", "Un explorateur", "Un super-héros", "Un clown", "Un sorcier",
    "Un lutin", "Un troll", "Un pharaon", "Un savant fou", "Un génie", "Un chevalier", "Un dragon"
]

verbes = [
    "mange", "danse avec", "observe", "construit", "déguise", "parle à", 
    "vole avec", "lance", "cherche", "embrasse", "cherche", "caresse", 
    "imite", "capture", "défie", "sauve", "détruit", "protège", "espionne",
    "poursuit", "surprend", "cache", "évite", "combat", "découvre", "explore"
]

complements = [
    "une baleine", "une montagne", "un nuage", "un arc-en-ciel", "un éléphant", 
    "une étoile filante", "un trampoline", "un château en chocolat", "un robot", 
    "un trésor", "une licorne rose", "une soucoupe volante en papier", "une forêt enchantée",
    "une grotte mystérieuse", "une île déserte", "un volcan en éruption", "un champ de fleurs",
    "une fusée spatiale", "une fontaine de chocolat", "un tapis volant", "une licorne volante",
    "un pégase", "un abominable homme des neiges", "un monstre marin", "un vaisseau spatial",
    "une baguette magique", "un cristal magique", "un trésor caché", "une potion magique",
    "une machine à voyager dans le temps", "une porte dimensionnelle", "un livre enchanté"
]

adjectifs = [
    "rose", "bleu", "vert", "rouge", "orange", "jaune", "violet", "brillant", "scintillant",
    "magique", "mystérieux", "enchanté", "fantastique", "extraordinaire", "effrayant", "amusant",
    "géant", "minuscule", "invisible", "gourmand", "féroce", "amusant", "étrange", "surnaturel",
    "lumineux", "sombre", "arc-en-ciel", "multicolore", "sauvage", "divin", "farfelu", "mythique"
]


def generate_random_sentence():
    sujet = random.choice(sujets)
    verbe = random.choice(verbes)
    complement = random.choice(complements)
    adjectif = random.choice(adjectifs)
    phrase = f"{sujet} {verbe} {complement} {adjectif}."
    return phrase


def send_mail():
    user = txtfld4.get()
    app_password = txtfld5.get()
    to = txtfld.get()
    subject = 'helo'

    amount = txtfld3.get()

    with yagmail.SMTP(user, app_password) as yag:    
        for i in range(int(amount)):
            threading.Thread(target=yag.send(to, generate_random_sentence(), generate_random_sentence()))


btn=Button(window, text="Send", fg='red', command=send_mail)
btn.place(x=210, y=197)
lbl=Label(window, text="Amuse toi bien :)", fg='red', font=("Helvetica", 16))
lbl.place(x=60, y=20)
lbl2=Label(window, text="Son Email", fg='red', font=("Helvetica", 10))
lbl2.place(x=12, y=72)
txtfld=Entry(window, text="Email de ta victime", bd=5)
txtfld.place(x=80, y=70)
lbl4=Label(window, text="Combien ?", fg='red', font=("Helvetica", 10))
lbl4.place(x=10, y=200)
txtfld3=Entry(window, text="amount", bd=1)
txtfld3.place(x=80, y=200)

lbl5=Label(window, text="Ton email", fg='red', font=("Helvetica", 10))
lbl5.place(x=12, y=125)
txtfld4=Entry(window, text="ton email", bd=5)
txtfld4.place(x=80, y=125)
lbl6=Label(window, text="App MDP", fg='red', font=("Helvetica", 10))
lbl6.place(x=10, y=150)
txtfld5=Entry(window, text="mdp appli", bd=5)
txtfld5.place(x=80, y=150)

window.title('Mail Harasser 3000 v0.1')
window.geometry("300x250+600+250")
window.mainloop()






