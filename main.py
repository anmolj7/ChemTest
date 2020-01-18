import tkinter as tk 
from tkinter import messagebox as tkMessageBox
import random 
import time 


def get_index_by_val(List, value):
    for index, el in enumerate(List):
        if value in el:
            return index
    return False


class Game:
    def __init__(self):
        self.app = tk.Tk()
        self.input = tk.StringVar()
        self.label = tk.StringVar()
        self.tries = tk.StringVar()

        self.Counter = 0 

        with open('elements.txt') as f:
            data = f.read().split('\n')
            data = [x.split() for x in data]
            self.elements = data

        self.app.title("PeriodicTable")
        self.create_widgets()
        self.element_rand()
        self.app.mainloop()

    def create_widgets(self):
        self.app.geometry("350x300+0+0")
        tk.Label(self.app, text="Guess Any Element", font=('arial', 25, "bold"), fg="black").pack()
        tk.Label(self.app, text="Enter the symbol", font=('arial', 15, "bold"), fg="black").pack()
        tk.Label(self.app, textvariable=self.label, bd=3, font=('Arial', 20, "bold"), relief="solid", width=4, height=2).pack(pady=20)
        tk.Entry(self.app, textvariable=self.input, bg="white", justify="center").pack()
        canvas = tk.Canvas(self.app)
        canvas.pack(pady=10)
        tk.Button(canvas, text="Submit", bg="white", command=self.submit_ans).grid(row=0, column=0)
        tk.Button(canvas, text="Get Answer", bg="white", command=self.show_ans).grid(row=0, column=1)
        tk.Button(canvas, text="New Game", bg="white", command=self.new_game).grid(row=0, column=2)
        tk.Label(self.app, textvariable=self.tries).pack()
        self.tries.set(f'Tries Left: {5-self.Counter}')

    def submit_ans(self):
        curr_input = self.input.get()
        
        #check if the current input is a valid element or not...
        if not get_index_by_val(self.elements, curr_input):
            self.popup('Invalid Input! Make sure the element\'s symbol is correct!')
        else:
            #Checking if answer is correct!
            correct_ans = self.elements[get_index_by_val(self.elements, self.label.get())][1]
            if correct_ans == curr_input:
                self.popup("Correct Answer!")
                self.element_rand()
            else:
                self.popup('Incorrect Answer!')
                self.show_hint()
                self.Counter += 1
                if self.Counter == 5:
                    self.popup('Game over!')
                    choice = tkMessageBox.askquestion("ChemTest", "Do you want to try again?")
                    if choice == 'yes':
                        self.new_game()
                    else:
                        self.app.destroy()
                        exit()
                self.tries.set(f'Tries Left: {5-self.Counter}')
        self.input.set("")

    def element_rand(self):
        element = random.choice(list(self.elements))[0]
        self.label.set(element)
    
    def popup(self, text):
        tkMessageBox.showinfo("ChemTest", text)

    def show_ans(self):
        el = self.elements[get_index_by_val(self.elements, self.label.get())]
        self.popup(f'The symbol of the atomic number {self.label.get()} is: {el[1]}, and the name of the element is: {el[2]}')
        
    def new_game(self):
        self.app.destroy()
        Game()

    def show_hint(self):
        curr_element = self.elements[get_index_by_val(self.elements, self.input.get())]
        correct_ans = self.elements[get_index_by_val(self.elements, self.label.get())]

        curr_element_ind = int(get_index_by_val(self.elements, curr_element[0]))
        correct_ans_ind = int(get_index_by_val(self.elements, correct_ans[0]))

        if curr_element_ind < correct_ans_ind:
            self.popup(f"The correct element has the atomic number higher than {curr_element[2]}.")
        else:
            self.popup(f"The correct element has the atmoic number lower than {curr_element[2]}.")

def main():
    Game()


if __name__ == "__main__":
    main()
