from tkinter import *
from tkinter import messagebox
import random
import json

FONT = ("New Times Roman", 10, "bold")


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    generated_password = ""
    for char in password_list:
        generated_password += char

    pass_entry.insert(0, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add_to_txt():
    website = web_entry.get()
    email = name_entry.get()
    password = pass_entry.get()
    new_entry = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Warning", message="You left some fields empty!")
    else:
        try:
            with open("data.json", "r") as password_file:
                data = json.load(password_file)
                data.update(new_entry)
        except FileNotFoundError:
            with open("data.json", "w") as password_file:
                json.dump(new_entry, password_file, indent=4)
        else:
            with open("data.json", "w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            web_entry.delete(0, END)
            # name_entry.delete(0, END)
            pass_entry.delete(0, END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #


def search_entry():
    try:
        with open("data.json", "r") as password_file:
            data = json.load(password_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No Data File Found")
    else:
        try:
            messagebox.showinfo(title=f"{web_entry.get()}",
                                message=f"Email/Username: {data[web_entry.get()]['email']}"
                                        f"\nPassword: {data[web_entry.get()]['password']}")
        except KeyError:
            messagebox.showwarning(title="Error", message=f"No details for {web_entry.get()} exist...")


# ---------------------------- UI SETUP ------------------------------- #


# create the window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the lock image
lock_img = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# create the website label
web_label = Label(text="Website:", font=FONT)
web_label.grid(column=0, row=1)

# create the website entry
web_entry = Entry(width=26)
web_entry.grid(column=1, row=1)
web_entry.focus()

# create the search button
search_button = Button(text="Search", font=FONT, command=search_entry, width=16)
search_button.grid(column=2, row=1)

# create the email/username label
name_label = Label(text="Email/Username:", font=FONT)
name_label.grid(column=0, row=2)

# create the email/username entry
name_entry = Entry(width=49)
name_entry.grid(column=1, row=2, columnspan=2)
name_entry.insert(0, "ariskoliadimas@gmail.com")

# create the password label
pass_label = Label(text="Password:", font=FONT)
pass_label.grid(column=0, row=3)

# create the password entry
pass_entry = Entry(width=26)
pass_entry.grid(column=1, row=3)

# create the generate button
generate_button = Button(text="Generate Password", font=FONT, command=generate_password)
generate_button.grid(column=2, row=3)

# create the add button
add_button = Button(text="Add", width=36, font=FONT, command=add_to_txt)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
