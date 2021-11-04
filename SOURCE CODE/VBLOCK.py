from tkinter import *
from tkinter import messagebox
from ctypes import windll
import os
import sys
from PIL import ImageTk, Image





tk_title = "VBLOCK by mlv.ps"

root = Tk()
root.title(tk_title) 
root.overrideredirect(True)
root.geometry('600x600+75+75')

#root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='vblockicon.png'))

#iconpng=PhotoImage(file='C:\\Users\\User\\Desktop\\VBlock\\GUI\\vblockicon.png')
#root.iconphoto(False,iconpng)
#root.iconbitmap('snowman.ico')
#root.iconbitmap(os.path.join(sys.path[0], "/icon/vblockicon.ico"))
#root.iconbitmap(os.path.join(sys.path[0], 'vblockicon.ico'))
#Tk.call('wm', 'iconphoto', Tk._w, ImageTk.PhotoImage(Image.open('./icon/vblockicon.ico')))

img = PhotoImage(file='vblockicon.png')
root.tk.call('wm', 'iconphoto', root._w, img)



root.minimized = False
root.maximized = False

LGRAY = '#d03a4d'
DGRAY = '#222529'
RGRAY = '#1b1c1f'

root.config(bg="#25292e")
title_bar = Frame(root, bg=RGRAY, relief='raised', bd=0,highlightthickness=0)

def set_appwindow(mainWindow):

    GWL_EXSTYLE = -20
    WS_EX_APPWINDOW = 0x00040000
    WS_EX_TOOLWINDOW = 0x00000080
    # Magic
    hwnd = windll.user32.GetParent(mainWindow.winfo_id())
    stylew = windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    stylew = stylew & ~WS_EX_TOOLWINDOW
    stylew = stylew | WS_EX_APPWINDOW
    res = windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, stylew)
   
    mainWindow.wm_withdraw()
    mainWindow.after(10, lambda: mainWindow.wm_deiconify())

def minimize_me():
    root.attributes("-alpha",0)
    root.minimized = True

def deminimize(event):

    root.focus() 
    root.attributes("-alpha",1)
    if root.minimized == True:
        root.minimized = False

def maximize_me():

    if root.maximized == False:
        root.normal_size = root.geometry()
        root.geometry(f"{root.winfo_screenwidth()}x{root.winfo_screenheight()}+0+0")
        root.maximized = not root.maximized 
        
    else:
        root.geometry(root.normal_size)
        root.maximized = not root.maximized


close_button = Button(title_bar, text='  ×  ', command=root.destroy,bg=RGRAY,padx=2,pady=2,font=("calibri", 13),bd=0,fg='white',highlightthickness=0)
minimize_button = Button(title_bar, text=' – ',command=minimize_me,bg=RGRAY,padx=2,pady=2,bd=0,fg='white',font=("calibri", 13),highlightthickness=0)
title_bar_title = Label(title_bar, text=tk_title, bg=RGRAY,bd=0,fg='white',font=("helvetica", 10),highlightthickness=0)

window = Frame(root, bg=DGRAY,highlightthickness=0)

title_bar.pack(fill=X)
close_button.pack(side=RIGHT,ipadx=7,ipady=1)
minimize_button.pack(side=RIGHT,ipadx=7,ipady=1)
title_bar_title.pack(side=LEFT, padx=10)
window.pack(expand=1, fill=BOTH) # replace this with your main Canvas/Frame/etc.
#xwin=None
#ywin=None
# bind title bar motion to the move window function

def changex_on_hovering(event):
    global close_button
    close_button['bg']='red'
def returnx_to_normalstate(event):
    global close_button
    close_button['bg']=RGRAY

def changem_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=LGRAY
def returnm_size_on_hovering(event):
    global minimize_button
    minimize_button['bg']=RGRAY


def get_pos(event):

    if root.maximized == False:
        
        xwin = root.winfo_x()
        ywin = root.winfo_y()
        startx = event.x_root
        starty = event.y_root

        ywin = ywin - starty
        xwin = xwin - startx

        def move_window(event):
            root.config(cursor="fleur")
            root.geometry(f'+{event.x_root + xwin}+{event.y_root + ywin}')


        def release_window(event):
            root.config(cursor="arrow")
            
        title_bar.bind('<B1-Motion>', move_window)
        title_bar.bind('<ButtonRelease-1>', release_window)
        title_bar_title.bind('<B1-Motion>', move_window)
        title_bar_title.bind('<ButtonRelease-1>', release_window)
    else:
        root.maximized = not root.maximized


title_bar.bind('<Button-1>', get_pos)
title_bar_title.bind('<Button-1>', get_pos)

close_button.bind('<Enter>',changex_on_hovering)
close_button.bind('<Leave>',returnx_to_normalstate)

minimize_button.bind('<Enter>', changem_size_on_hovering)
minimize_button.bind('<Leave>', returnm_size_on_hovering)


root.bind("<FocusIn>",deminimize)
root.after(10, lambda: set_appwindow(root))
















def activate_clicked():
    try:
        os.system('netsh advfirewall firewall add rule name="mlvpsVBlockActive" dir=out remoteport=5223 protocol=TCP action=block')
    except:
        messagebox.showerror('VBLOCK ERROR', 'Could not execute command :( Make sure to run as administrator!')

def deactivate_clicked():
    try:
        os.system('netsh advfirewall firewall delete rule name="mlvpsVBlockActive')
    except:
        messagebox.showerror('VBLOCK ERROR', 'Could not execute command :( Make sure to run as administrator!')




#window = Tk()

root.geometry("600x600")
#window.geometry("600x600")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 600,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
    278.0, 297.0,
    image=background_img)


canvas.create_rectangle(
    147, 356, 147+306, 356+54,
    fill = "#bb3b4b",
    outline = "")

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = deactivate_clicked,
    relief = "flat")

b0.place(
    x = 148, y = 392, #356
    width = 303,
    height = 51)


canvas.create_rectangle(
    147, 287, 147+306, 287+54,
    fill = "#bb3b4b",
    outline = "")

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = activate_clicked,
    relief = "flat")

b1.place(
    x = 148, y = 323, #147 #322 Standard: #147 #287
    width = 303, #306
    height = 51) #54

#window.resizable(False, False)
window.mainloop()
root.mainloop()