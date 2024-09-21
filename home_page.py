import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
from sketchpy import library as lib
import turtle
from PIL import Image, ImageDraw, ImageFont
from sketchpy import canvas
import we_er


root = tk.Tk()
root.title("HOME PAGE")

image = Image.open('king.png')
# Get the size of the image
image_width, image_height = image.size
# Create a tkinter window with the same size as the image
root.geometry(f"{image_width}x{image_height}")

photo_image = ImageTk.PhotoImage(image)

frame_login = tk.Label(root, image=photo_image)
frame_login.place(x=0, y=0)

frame_login = tk.Frame(root, padx=45, pady=460, bg="#128")
frame_login.place(relx=0.24, rely=0.28, anchor=tk.CENTER)

picture= Image.open("left.png")
pi= ImageTk.PhotoImage(picture)
frame = tk.Label(frame_login, image=pi)
frame.place(x=0, y=0,relx=0.5, rely=1.26, anchor=tk.CENTER)


DATABASE = {"s": "0", "user2": "password2"}

def forgotpassword():
    create_forgotpassword_ui()

def newlogin():
    create_newlogin_ui()

def check_credentials():
    userid = entry_userid.get()
    password = entry_password.get()

    if userid not in DATABASE or DATABASE[userid] != password:
        label_status["text"] = "Invalid user ID or password."
    else:
        label_status["text"] = "Login successful!"

        we_er.login()
       
def create_forgotpassword_ui():
    def tellpassword():
    
        userid = entry.get()
        if userid in DATABASE:
            status["text"] = "Password is " + DATABASE[userid]
        else:
            status["text"]= "Userid does not exist"

    root = tk.Tk()
    root.title("FORGOT PASSWORD")

    fp = tk.Frame(root, padx=600, pady=300, bg="#128")
    fp.pack()

    ud = tk.Label(fp, text="User ID:", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
    ud.grid(row=10, column=0, padx=2, pady=2, sticky=tk.W)
        #ud.place(relx=0.1, rely=0.6, anchor=tk.CENTER)

    entry = tk.Entry(fp, font=("Arial", 25))
    entry.grid(row=10, column=1, padx=1, pady=70, sticky=tk.W)
        #entry.place(relx=0.55, rely=0.6, anchor=tk.CENTER)
        
    forgot_button = tk.Button(fp, text="know", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=tellpassword)
    forgot_button.grid(row=11, column=0, padx=0, pady=0, sticky=tk.W)
        #forgot_button.place(relx=0.04, rely=1.25, anchor=tk.CENTER)
        
    status = tk.Label(fp, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
    status.grid(row=12, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)

    root.mainloop()

def create_newlogin_ui():
    def register():
        userid= enter_id.get()
        password = enter_password.get()
        if userid not in DATABASE:
            DATABASE[userid] = password
            status["text"] = "Registration successful " 
        else:
            status["text"]= "Userid already exist"

    window = tk.Tk()
    window.title("New login")

    box = tk.Frame(window, padx=600, pady=300, bg="#128")
    box.pack()

    re = tk.Label(box, text="User ID:", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
    re.grid(row=10, column=0, padx=2, pady=2, sticky=tk.W)

    enter_id = tk.Entry(box, font=("Arial", 25))
    enter_id.grid(row=10, column=1, padx=1, pady=70, sticky=tk.W)

    pas= tk.Label(box, text="Password:", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
    pas.grid(row=11, column=0, padx=2, pady=2, sticky=tk.W)
#label_password.place(relx=0.1, rely=1, anchor=tk.CENTER)

    enter_password = tk.Entry(box, show="*", font=("Arial", 25))
    enter_password.grid(row=11, column=1, padx=2, pady=2, sticky=tk.W)
#entry_password.place(relx=0.7, rely=1.2, anchor=tk.CENTER)

    register_button = tk.Button(box, text="Register", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=register)
    register_button.grid(row=12, column=0, padx=0, pady=0, sticky=tk.W)

    status = tk.Label(box, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
    status.grid(row=13, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)

    window.mainloop()


new_label = tk.Label(frame_login, text="Welcome to\n Drawing and Animation App", font=("Arial", 40, "bold"), bg='#128', fg="#ffffff")
new_label.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
new_label.place(relx=0.5, rely=0, anchor=tk.CENTER)
#create_new_label("WELECOME TO \n DRAWING AND ANIMATION APP")

label_userid = tk.Label(frame_login, text="User ID:", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")

label_userid.place(relx=0.1, rely=0.6, anchor=tk.CENTER)

entry_userid = tk.Entry(frame_login, font=("Arial", 25))

entry_userid.place(relx=0.55, rely=0.6, anchor=tk.CENTER)

label_password = tk.Label(frame_login, text="Password:", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
label_password.grid(row=15, column=0, padx=2, pady=2, sticky=tk.W)


entry_password = tk.Entry(frame_login, show="*", font=("Arial", 25))
entry_password.grid(row=15, column=1, padx=2, pady=2, sticky=tk.W)


button_login = tk.Button(frame_login, text="Login", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=check_credentials)
button_login.place(relx=0.04, rely=1.25, anchor=tk.CENTER)

button_forgot = tk.Button(frame_login, text="Forgot password?", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=forgotpassword)
button_forgot.place(relx=0.42, rely=1.25, anchor=tk.CENTER)

button_help = tk.Button(frame_login, text="Help :)", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF")
button_help.grid(row=10, column=3,padx=0, pady=70, sticky=tk.W)
#button_new.place(relx=0.6, rely=1.25, anchor=tk.CENTER)

button_new = tk.Button(frame_login, text="Register", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=newlogin)
#button_new.grid(row=10, column=5,padx=0, pady=70, sticky=tk.W)
button_new.place(relx=0.85, rely=1.25, anchor=tk.CENTER)

label_status = tk.Label(frame_login, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
#label_status.grid(row=10, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)
label_status.place(relx=0.35, rely=1.6, anchor=tk.CENTER)

root.mainloop()
