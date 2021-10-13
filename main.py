from tkinter import *
from tkinter import messagebox
from pandas.core.window.rolling import Window
import pyperclip
import json


#----------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePass():
  import random
  from random import choice, randint, shuffle
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  passwordLetters = [choice(letters) for _ in range(randint(8, 10))]

  passwordSymbols = [choice(symbols) for _ in range(randint(2, 4))]

  passwordNumbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = passwordLetters + passwordNumbers + passwordSymbols
  shuffle(password_list)

  password = "".join(password_list)
  passwordEntry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()
    newDict = {
        website: {
            "email": email,
            "password": password
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="Please don't leave any of the fields empty!")
    else:
        try:
            with open("data.json", "r") as dataFile:
                data = json.load(dataFile)
        except FileNotFoundError:
            with open("data.json", "w") as dataFile:
                json.dump(newDict, dataFile, indent=4)
        else:
            data.update(newDict)
            with open("data.json", "w") as dataFile:
                json.dump(data, dataFile, indent=4)
        finally:
            websiteEntry.delete(0, END)
            passwordEntry.delete(0, END)
# ---------------------------- FIND PASSWORD ------------------------------- #
def findPass():
    website = websiteEntry.get()
    try:
        with open("data.json") as dataFile:
            data = json.load(dataFile)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details of {website}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lockIMG = PhotoImage(file="pngegg.png")
canvas.create_image(100, 100, image=lockIMG)
canvas.grid(column=1, row=0)

#Labels
website = Label(text="Website:")
website.grid(row=1, column=0)
email = Label(text="Email/Username:")
email.grid(row=2, column=0)
password = Label(text="Password:")
password.grid(row=3, column=0)

#Entries
websiteEntry = Entry(width=35)
websiteEntry.grid(row=1, column=1)
websiteEntry.focus()
emailEntry = Entry(width=35)
emailEntry.grid(row=2, column=1)
emailEntry.insert(0, "mitulsingh@gmail.com")
passwordEntry = Entry(width=35)
passwordEntry.grid(row=3, column= 1)

#Buttons
genPassword = Button(text="Generate Pasword", command=generatePass)
genPassword.grid(row=3, column=2)
add = Button(text="Add", width=35, command=save)
add.grid(row=4, column=1, columnspan=1)
search = Button(text="Search", width=10, command=findPass)
search.grid(row=1, column=2)

window.mainloop()