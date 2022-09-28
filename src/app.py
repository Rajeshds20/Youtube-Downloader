import tkinter
from tkinter import filedialog, messagebox
import pytube

w = tkinter.Tk()
w.title('YT Video Download')
w.geometry('700x600')
w.resizable(0, 0)

v1=tkinter.StringVar(w)
v2=tkinter.StringVar(w)
v3=tkinter.StringVar(w)
v3.set('')


def bro():
    dr = tkinter.filedialog.askdirectory()
    v2.set(dr)
def msg():
    tkinter.messagebox.showinfo('DONE',"DOWNLOAD SUCCESSFUL")
    return
def dwd():
    a = v1.get()
    b = v2.get()
    c = v3.get()
    vid = pytube.YouTube(a)
    if c == '144p' :
        vd = vid.streams.get_lowest_resolution()
    else :
        vd = vid.streams.get_by_resolution(c)
    vd.download(output_path = b)
    msg()

l1 = tkinter.Label(w, text = 'YouTube Video Downloader', font = ('algerian',25,'bold'), fg='brown', bg='skyblue')
l2 = tkinter.Label(w, text = 'Enter the YT Video Link :', font = ('calibri',18), fg = 'blue')
l3 = tkinter.Label(w, text = 'Enter the Location to save :', font = ('calibri',18), fg = 'blue')
l4 = tkinter.Label(w, text = 'Select the resolution :', font = ('calibri',18), fg = 'blue')
l1.place(x = 100, y = 10)
l2.place(x = 10, y = 70)
l3.place(x = 10, y = 125)
l4.place(x = 10, y = 220)

b1 = tkinter.Button(w, text = 'Browse', command = bro, font = ('cooper black',16), fg = 'brown', bg = 'wheat')
b2 = tkinter.Button(w, text = 'DOWNLOAD', command = dwd, font = ('cooper black',18), fg = 'brown', bg = 'wheat')
b1.place(x = 420, y = 160)
b2.place(x = 260, y = 360)

r1 = tkinter.Radiobutton(w, text='144p', variable = v3, font=('arial', 15), value = '144p')
r2 = tkinter.Radiobutton(w, text='360p', variable = v3, font=('arial', 15), value = '360p')
r3 = tkinter.Radiobutton(w, text='720p', variable = v3, font=('arial', 15), value = '720p')
r1.place(x = 250, y = 230)
r2.place(x = 250, y = 260)
r3.place(x = 250, y = 290)

e1 = tkinter.Entry(w, textvariable = v1, width = 24, font=('arial', 15))
e2 = tkinter.Entry(w, textvariable = v2, width = 28, font=('arial', 15))

e1.place(x = 275, y = 75)
e2.place(x = 80, y = 170)


w.mainloop()
