import random
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry("400x350")
window.title("Rock Paper Scissor")


user_score = 0
comp_score = 0


def choice_to_number(choice):
    rps = {"rock": 0, "paper": 1, "scissor": 2}
    return rps[choice]

def number_to_choice(number):
    rps = {0: "rock", 1: "paper", 2: "scissor"}
    return rps[number]


def random_computer_choice():
    return random.choice(["rock", "paper", "scissor"])


def result(human_choice, comp_choice):
    global user_score
    global comp_score

    
    user = choice_to_number(human_choice)
    comp = choice_to_number(comp_choice)

    if user == comp:
        result_text = "It's a tie!"
    elif (user - comp) % 3 == 1:
        result_text = "You win!"
        user_score += 1
    else:
        result_text = "Computer wins!"
        comp_score += 1

   
    text_area.delete(1.0, tk.END)
    answer = f"Your choice: {human_choice} \nComputer choice: {comp_choice} \n\nResult: {result_text}\nYour score: {user_score} \nComputer score: {comp_score}"
    text_area.insert(tk.END, answer)

    
    play_again = messagebox.askyesno("Play Again?", "Do you want to play another round?")
    if not play_again:
        window.quit()  # End the game if the user selects 'No'


def Rock():
    user_choice = "rock"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def Paper():
    user_choice = "paper"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

def Scissor():
    user_choice = "scissor"
    comp_choice = random_computer_choice()
    result(user_choice, comp_choice)

btn1 = tk.Button(text="Rock", width=8, height=2, bg="blue", command=Rock)
btn1.grid(row=1, column=0, padx=3, pady=3)

btn2 = tk.Button(text="Paper", width=8, height=2, bg="red", command=Paper)
btn2.grid(row=2, column=0, padx=3, pady=3)

btn3 = tk.Button(text="Scissor", width=8, height=2, bg="yellow", command=Scissor)
btn3.grid(row=3, column=0, padx=3, pady=3)


text_area = tk.Text(master=window, width=40, height=12, bg="#FFFF99")
text_area.grid(row=4, column=0, columnspan=3)


window.mainloop()
