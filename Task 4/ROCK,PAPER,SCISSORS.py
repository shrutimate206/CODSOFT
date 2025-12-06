import tkinter as tk
import random

def play(user_choice):
    global user_score, comp_score

    computer_choice = random.choice(["Rock", "Paper", "Scissors"])

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        result = "You Win!"
        user_score += 1
    else:
        result = "You Lose!"
        comp_score += 1

    result_label.config(text=f"Result: {result}")
    choices_label.config(text=f"You: {user_choice}   |   Computer: {computer_choice}")
    score_label.config(text=f"Score - You: {user_score} | Computer: {comp_score}")

def reset_game():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    result_label.config(text="Result: ")
    choices_label.config(text="Make your choice!")
    score_label.config(text="Score - You: 0 | Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("350x400")

user_score = 0
comp_score = 0

tk.Label(root, text="Rock - Paper - Scissors", font=("Arial", 18)).pack(pady=10)

choices_label = tk.Label(root, text="Make your choice!", font=("Arial", 14))
choices_label.pack(pady=10)

result_label = tk.Label(root, text="Result: ", font=("Arial", 16))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score - You: 0 | Computer: 0", font=("Arial", 14))
score_label.pack(pady=10)

btn_rock = tk.Button(root, text="Rock", font=("Arial", 14), width=12, command=lambda: play("Rock"))
btn_rock.pack(pady=5)

btn_paper = tk.Button(root, text="Paper", font=("Arial", 14), width=12, command=lambda: play("Paper"))
btn_paper.pack(pady=5)

btn_scissors = tk.Button(root, text="Scissors", font=("Arial", 14), width=12, command=lambda: play("Scissors"))
btn_scissors.pack(pady=5)

reset_btn = tk.Button(root, text="Play Again", font=("Arial", 14), command=reset_game)
reset_btn.pack(pady=20)

root.mainloop()
