from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
#--------------------generate password-----------------#
def generatepassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)


    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#---------------Save password---------------------------------#
def save():
    # get  method used to get data in entry
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    #to validate no entry fields are empty
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message="Please make sure all details are filled")

    # for dialog box after entering data
    else:
        is_ok = messagebox.askyesno(title=website, message=f"These are the details entered: \n Email: {email}" f"\n Password: {password}\n Is It okay to save?")
        # using 'with' we dont have to use 'close' method
        if is_ok:
            with open("data.txt", "a") as user_data:
                user_data.write(f"{website} | {email} | {password}\n")
                # delete method used to delete data from frontend after saving the user data
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)





#--------------------------UI setup----------------#
#creating window class for o/p window

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50)

#using canvas
canvas = Canvas(height=200, width=150)
logo_img = PhotoImage(file="images/logo.png")
canvas.create_image(100, 90, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/UserName")
email_label.grid(row=2, column=0)
Password_label = Label(text="Password")
Password_label.grid(row=3, column=0)

#Entry
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2)
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1,columnspan=2)

#Buttons
generate_pass_button = Button(text="Generate Password", width=15, command=generatepassword)
generate_pass_button.grid(row=4, column=2)
add_button = Button(text="Add", width=17, command=save)
add_button.grid(row=4, column=1)




window.mainloop()