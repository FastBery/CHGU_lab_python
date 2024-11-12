from tkinter import *
import math as m

def event():
    x = int(ent_x.get())
    result = 0
    if x<=3 and x>-3:
        result = 3
    elif x > 3:
        result = m.sin(x+3)/m.pow(m.pow((x+3),2), 0.2) 
    else:
        result = abs(x-1)/(x*x - 4*x + 3)

    lbl_result = Label(root, text=f"{result}", font=20)
    lbl_result.grid(column=0, row=2)

root = Tk()
root.title('12 lab (18)')

# Making window and editing size
window_width = 400
window_height = 500

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)
    
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

#Importing image and anchoring it to label, showing in window
img = PhotoImage(file='./12_lab/function.png')
image_label = Label(root, image=img, anchor=N)

lbl_main = Label(root, text="Enter value for X variable:", font=20, bg='green')

lbl_x = Label(root, text='X:', font=20)
ent_x = Entry(root)

image_label.grid(column=0 , row=0, padx=5, pady=5, sticky=N, columnspan=2)
lbl_x.grid(column=0, row=1, padx=15, pady=5, sticky=NE)
ent_x.grid(column=1, row=1, padx=15, pady=5, sticky=NW)


bt = Button(root, text="Calculate", command=event)
bt.grid(column=1, row=2)

root.mainloop()