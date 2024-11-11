from tkinter import *

root = Tk()
root.title('12 lab (18)')

# Making window and editing size
window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
    
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

#Importing image and anchoring it to label, showing in window
img = PhotoImage(file='./function.png')
image_label = Label(root, image=img, anchor=N)

lbl_main = Label(root, text="Enter value for X variable:", font=20, bg='green')

lbl_x = Label(root, text='X:', font=20)
lbl_x.place(relx=0.05, rely=0.5)
ent_x = Entry(root)


frame1 = Frame(root)

image_label.pack(ipady=30)
lbl_main.pack()
ent_x.pack(pady=10)

root.mainloop()