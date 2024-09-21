def login():
    import tkinter as tk
    from tkinter import PhotoImage
    from PIL import Image, ImageTk
    from sketchpy import library as lib
    import turtle
    from PIL import Image, ImageDraw, ImageFont
    from sketchpy import canvas
    import anim
    
    def open_drawing():
        create_drawing_ui()

    def open_animation():
        anim.create_animation_ui()

    root = tk.Tk()

    root.title("Button")
  
    frame = tk.Frame(root, padx=1200, pady=450, bg="#128")
    frame.place(relx=0.24, rely=0.28, anchor=tk.CENTER)

    

    label_userid = tk.Label(frame, text="WELCOME ", font=("Arial", 35, "bold"),bg= "#128", fg="#FFFFFF")
    label_userid.grid(row=0, column=0, padx=2, pady=2, sticky=tk.W)
    label_userid.place(relx=1.6, rely=0, anchor=tk.CENTER)

    label_userid = tk.Label(frame, text="Choose option ", font=("Arial", 35, "bold"),bg= "#128", fg="#FFFFFF")
    #label_userid.grid(row=0, column=1, padx=2, pady=2, sticky=tk.W)
    label_userid.place(relx=1.6, rely=2, anchor=tk.CENTER)

    drawing_button = tk.Button(frame, text="DRAWING", font=("Arial", 40,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=open_drawing)
    drawing_button.grid(row=4, column=20, padx=30, pady=30, sticky=tk.W)

    animation_button = tk.Button(frame, text="ANIMATION", font=("Arial", 40,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=open_animation)
    animation_button.grid(row=4, column=30, padx=30, pady=30, sticky=tk.W)

        
    def create_drawing_ui():
        def text_to_image():
            def name():
                status1["text"]= "Options Available: \n 1) Doctor\n 2) Mahatma Gandhi"

            def place():
                status1["text"]= "Options Available: \n 1) Red fort\n 2) Temple"

            def animal():
                status1["text"]= "Options Available: \n 1) Elephant\n 2) Peacock"

            def thing():
                status1["text"]= "Options Available: \n 1) Bus\n 2) Laptop"

            def image_insert():
                s= infor.get()
                if s=="Doctor":
                    pen= canvas.sketch_from_image('doctor.png')
                    pen.draw()
                elif s=="Mahatma gandhi":
                    pen= canvas.sketch_from_image('mahatma.png')
                    pen.draw()
                elif s=="Abhinav":
                    pen= canvas.sketch_from_image('true.png')
                    pen.draw()
                elif s=="Red fort":
                    pen= canvas.sketch_from_image('red.png')
                    pen.draw()
                elif s=="Dog":
                    pen= canvas.sketch_from_image('dog.png')
                    pen.draw()
                elif s=="Temple":
                    pen= canvas.sketch_from_image('temple.png')
                    pen.draw()
                elif s=="Elephant":
                    pen= canvas.sketch_from_image('elephant.png')
                    pen.draw()
                elif s=="Peacock":
                    pen= canvas.sketch_from_image('peacock.png')
                    pen.draw()
                elif s=="Bus":
                    pen= canvas.sketch_from_image('bus.png')
                    pen.draw()
                elif s=="Laptop":
                    pen= canvas.sketch_from_image('laptop.png')
                    pen.draw()
                else:
                    status["text"]= "SORRY! Cannot draw"

            screen= tk.Tk()
            screen.title("Text to image conversion")
            tab = tk.Frame(screen, padx=60, pady=30, bg="#128")
            tab.pack()

            choose_button = tk.Button(tab, text="Name", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=name)
            choose_button.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)

            choose_button = tk.Button(tab, text="Place", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=place)
            choose_button.grid(row=0, column=1, padx=0, pady=0, sticky=tk.W)

            choose_button = tk.Button(tab, text="Animals", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=animal)
            choose_button.grid(row=0, column=2, padx=0, pady=0, sticky=tk.W)

            choose_button = tk.Button(tab, text="Things", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=thing)
            choose_button.grid(row=0, column=3, padx=0, pady=0, sticky=tk.W)

            status1 = tk.Label(tab, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
            status1.grid(row=1, column=1, columnspan=3, padx=5, pady=5, sticky=tk.W)


            re = tk.Label(tab, text="Text", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
            re.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)

            infor = tk.Entry(tab, font=("Arial", 25))
            infor.grid(row=2, column=1, padx=1, pady=70, sticky=tk.W)
  
            enter_button = tk.Button(tab, text="Enter", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=image_insert)
            enter_button.grid(row=4, column=0, padx=0, pady=0, sticky=tk.W)

            status = tk.Label(tab, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
            status.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)

            screen.mainloop()

        def drawing_of_face():
            screen= tk.Tk()
            screen.title("Potrait")

            tab = tk.Frame(screen, padx=60, pady=30, bg="#128")
            tab.pack()
            def face_structure():
                image= Image.open("face.jpg")
                image.show()

            def final_face():
                s= infor.get()
                if s=="561b781":
                    pen= canvas.sketch_from_image('c1.png')
                    pen.draw()             
                else:
                    status["text"]= "SORRY! Cannot draw"

            enter_button = tk.Button(tab, text="Show", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF",command=face_structure)
            enter_button.grid(row=0, column=0, padx=0, pady=0, sticky=tk.W)

            re = tk.Label(tab, text="Choose", font=("Arial", 25, "bold"), bg='#128', fg="#ffffff")
            re.grid(row=2, column=0, padx=2, pady=2, sticky=tk.W)

            infor = tk.Entry(tab, font=("Arial", 25))
            infor.grid(row=2, column=0, padx=1, pady=70, sticky=tk.W)
  
            enter_button = tk.Button(tab, text="Enter", font=("Arial", 20,"bold"), bg="#5d3fd3", fg="#FFFFFF",command=final_face)
            enter_button.grid(row=4, column=0, padx=0, pady=0, sticky=tk.W)

            status = tk.Label(tab, text="", bg="#3457d5", fg="white", font=("Arial", 20,"bold"))
            status.grid(row=5, column=0, columnspan=3, padx=5, pady=5, sticky=tk.W)


            screen.mainloop()

        # Create the main window
        window = tk.Tk()
        window.title("Drawing App")

        box = tk.Frame(window, padx=60, pady=30, bg="#128")
        box.pack()

        drawing_button = tk.Button(box, text="TEXT TO IMAGE", font=("Arial", 40,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=text_to_image)
        drawing_button.grid(row=2, column=0, padx=30, pady=30, sticky=tk.W)

        animation_button = tk.Button(box, text="POTRAIT", font=("Arial", 40,"bold"), bg="#5d3fd3", fg="#FFFFFF", command=drawing_of_face)
        animation_button.grid(row=3, column=0, padx=30, pady=30, sticky=tk.W)

        window.mainloop()

    root.mainloop()