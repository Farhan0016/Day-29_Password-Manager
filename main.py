import json
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
    website = website_entry.get().title()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please make sure you haven't left any fields empty.")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These ae the details entered: \nEmail: {email} "
                                                              f"\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", mode='r') as data_file:
                    # Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", 'w') as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                # Updating old data with new data
                data.update(new_data)

                with open("data.json", mode='w') as data_file:
                    # Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)
                website_entry.focus()


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get().title()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo("Error", "No Data File Found.")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(website, message=f"Email: {email} \nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for the {website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
# Create and set the window of the application
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=20)

# Insert image in the App
img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=0, columnspan=3, row=0)

# Website Label
website_label = Label(text="Website:", justify="center")
website_label.grid(column=0, row=1)

# Website Entry Field
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(column=1, row=1)

# Search Button
search_btn = Button(text="Search", width=15, command=find_password)
search_btn.grid(column=2, row=1)

# Email Label
email_label = Label(text="Email/Username:", justify="center")
email_label.grid(column=0, row=2)

# Email Entry Field
email_entry = Entry(width=40)
email_entry.insert(0, "something@gmail.com")
email_entry.grid(column=1, columnspan=2, row=2)

# Password Label
password_label = Label(text="Password:", justify="center")
password_label.grid(column=0, row=3)

# Password Entry Field
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# Generate Password Button
generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3)

# Add Button
add_btn = Button(text="Add", width=33, command=save)
add_btn.grid(column=1, columnspan=3, row=4)

window.mainloop()
