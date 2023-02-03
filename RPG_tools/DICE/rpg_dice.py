import random
import tkinter as tk

def roll_dice():
    roll = random.randint(1, 20)
    result.config(text="You rolled a " + str(roll))

app = tk.Tk()
app.title("RPG Dice Simulator")
app.geometry("400x100")

result = tk.Label(text="", font=("TkDefaultFont", 20))
result.pack()

button = tk.Button(text="Roll dice", command=roll_dice)
button.pack()

app.mainloop()

#simula um dado de rpg de vinte lados



