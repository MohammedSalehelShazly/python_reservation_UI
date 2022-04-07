from asyncio.windows_events import NULL
from  tkinter import  *
from  tkinter import  ttk
from  tkinter import  messagebox

root=Tk()
ttk.Label(root,text="Full name:").grid(row=0, column=0, pady=10,padx=10)
EntryFullName=ttk.Entry(root, width=30, font = ('Arial', 16))
EntryFullName.grid(row=0, column=1,columnspan=2, pady=10)
root.title("Reservation UI")
#style
root.configure(background="#e1d8b2")
style=ttk.Style()
style.theme_use("classic")
style.configure("TLabel",background="#e1d8b2")
style.configure("TButton",background="#e1d8b2")
style.configure("TRadiobutton",background="#e1d8b2")
SpanGender=StringVar()
SpanGender.set("Male")
ttk.Label(root,text="Gender").grid(row=1, column=0)
ttk.Radiobutton(root,text="Male",variable=SpanGender, value="Male").grid(row=1, column=1)
ttk.Radiobutton(root,text="Female",variable=SpanGender, value="Female").grid(row=1, column=2)

TextComments=Text(root,width=30, height=15, font = ('Arial', 16))
TextComments.grid(row=3, column=1,columnspan=2)
ttk.Label(root,text="Comments:").grid(row=3, column=0)

buButton=ttk.Button(root,text="Submit")
buButton.grid(row=4,column=3)
buClear=ttk.Button(root,text="Clear")
buClear.grid(row=4,column=2)


def clearTxt(**showMsgBox):
    print('showMsgBox<' + str(showMsgBox) + '>')
    EntryFullName.delete(0,'end')
    TextComments.delete(1.0,'end')
    showBox = showMsgBox == NULL or showMsgBox == {}
    if(showBox):
        messagebox.showinfo(title='Warring', message='Entered Data Are cleared Successfully')



def ButtonClick():
    if(EntryFullName.get() == '' or TextComments.get(1.0,'end') == ''):
        return;
    nameMsg = 'Hello ' + EntryFullName.get() + '\n' + 'Welcome To Our Service'
    commentsMsg = 'your comment (' + TextComments.get(1.0,'end')+' )' +'\n' +'\n' +'is submitted'
    messagebox.showinfo(title="Add info", message= nameMsg +'\n'+ commentsMsg)
    clearTxt(False)

buButton.config(command=ButtonClick)
buClear.config(command=clearTxt)

root.mainloop()