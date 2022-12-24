from tkinter import *
from tkinter import messagebox
import random
import pyperclip as pyp
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    l=[random.choice(letters) for _ in range(nr_letters)]

    s=[random.choice(symbols) for _ in range(nr_symbols)]

    n=[random.choice(numbers) for _ in range(nr_numbers)]

    password_list=l+s+n
    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyp.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
'''---------------adding data in entry.json-------------'''
def add_entry():
    web=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={
        web:{
            'email': email,
            'password': password
        }
    }
    if len(web)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title='opps',message='Please fill the empty fields.')
    else:
        try:
            with open('entry.json', 'r') as f:
                data=json.load(f)
        except FileNotFoundError:
            with open('entry.json', 'w') as f:
                json.dump(new_data,f,indent=4)
        else:
            data.update(new_data)
            with open('entry.json', 'w') as f:
                json.dump(data,f,indent=4)
        
        website_entry.delete(0,END)
        password_entry.delete(0,END)

'''----searching for website in entry.json--------'''

def search_website():
    web=website_entry.get()
    try:
        with open('entry.json', 'r') as f:
            data=json.load(f)
    except FileNotFoundError:
        messagebox.showinfo(title='Error',message='no data file found')
    else:
        if web in data:
            email=data[web]['email']
            password=data[web]['password']
            messagebox.showinfo(title=web,message=f'Email:{email} \nPassword:{password}\n')
        else:
            messagebox.showerror(title='Error',message=f'The data for the {web} is not present')

# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50,bg='pink')

'''---------------------------CANVAS------------------------------'''

canvas=Canvas(width=200,height=200,highlightthickness=0,bg='pink')
photo_img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=photo_img)
canvas.grid(column=1,row=0)

'''-----------------------------LABELS---------------------------------'''

website_label=Label(text='Website:',font=(12),highlightthickness=0,bg='pink')
website_label.grid(column=0,row=1)


email_label=Label(text='Email/Username:',font=(12),highlightthickness=0,bg='pink')
email_label.grid(column=0,row=2)

password_label=Label(text='Password:',font=(12),highlightthickness=0,bg='pink')
password_label.grid(column=0,row=3)


'''-------------------------Entry--------------------------'''

website_entry=Entry(width=30)
website_entry.grid(column=1,row=1)
website_entry.focus()

email_entry=Entry(width=49)
email_entry.insert(END,'sidhant@email.com')
email_entry.grid(column=1,row=2,columnspan=2)

password_entry=Entry(width=29)
password_entry.grid(column=1,row=3)

'''----------------------------Button-----------------------------'''

generate_pass_button=Button(text='Generate Password',command=password_generator)
generate_pass_button.grid(column=2,row=3)

add_button=Button(text='Add',width=39,command=add_entry)
add_button.grid(column=1,row=4,columnspan=2)

search_button=Button(text='Search',width=15,command=search_website)
search_button.grid(column=2,row=1)

window.mainloop()
