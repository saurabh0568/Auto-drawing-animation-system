def create_animation_ui():
    import tkinter as tk
    from tkinter import PhotoImage
    from PIL import Image, ImageTk
    from sketchpy import library as lib
    import turtle
    from PIL import Image, ImageDraw, ImageFont
    from sketchpy import canvas
    import boy1
    import cycle1

    def animation_insert():
        s= infor.get()
        if s=="Running boy":
            boy1.anima_boy()
        elif s=="Cycling":
            cycle1.anima_cycle()
        else:
            status["text"]= "This Animation does not exist"
    
    window = tk.Tk()
    window.title("Animation App")

    tab = tk.Frame(window, padx=60, pady=30, bg="#128")
    tab.pack()

    re = tk.Label(tab, text="Text", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
    re.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)

    infor = tk.Entry(tab, font=("Arial", 25))
    infor.grid(row=2, column=1, padx=1, pady=70, sticky=tk.W)
  
    enter_button = tk.Button(tab, text="Enter", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command= animation_insert)
    enter_button.grid(row=4, column=0, padx=0, pady=0, sticky=tk.W)

    status = tk.Label(tab, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
    status.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)


    window.mainloop()
