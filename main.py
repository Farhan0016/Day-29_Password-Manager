from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '+', '^', '@', '(', ')']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These ae the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", mode="a") as data:
                content = f"{website} | {email} | {password}\n"
                data.writelines(content)
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=0, columnspan=3, row=0)

website_label = Label(text="Website:", justify="center")
website_label.grid(column=0, row=1)

website_entry = Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, columnspan=2, row=1)

email_label = Label(text="Email/Username:", justify="center")
email_label.grid(column=0, row=2)

email_entry = Entry(width=40)
email_entry.insert(0, "something@gmail.com")
email_entry.grid(column=1, columnspan=2, row=2)

password_label = Label(text="Password:", justify="center")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, columnspan=3, row=4)

window.mainloop()
