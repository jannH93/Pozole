from tkinter import *

root = Tk()
root.geometry("500x250")

label_file_name = Label(root, text="Nombre")
label_file_name.place(relx=0.3,rely=0.1,anchor= CENTER)

input_file_name = Entry(root)
input_file_name.place(relx=0.5,rely=0.1, anchor= CENTER)

my_text= Text(root,height=5,width=40)
my_text.place(relx=0.5,rely=0.4,anchor= CENTER)


def clearInputFeild():
    input_file_name.delete(0, END)
    
def clearTextarea():
    my_text.delete(1.0, END)
    
def addData():
    input_file_name.insert(END,"mi archivo")


open_button=Button(root,text="Limpiar el campo de entrada", command=clearInputFeild)
open_button.place(relx=0.25,rely=0.7,anchor=CENTER)
save_button=Button(root, text="Borrar el área de texto", command=clearTextarea)
save_button.place(relx=0.455,rely=0.7,anchor= CENTER)
exit_button=Button(root, text="Añadir datos al campo de entrada", command=addData)
exit_button.place(relx=0.7,rely=0.7,anchor= CENTER)

root.mainloop()

