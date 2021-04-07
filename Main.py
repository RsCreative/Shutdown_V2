# Shutdown Center version 2.0
# Raj Sandhu
# GUI Python app to create a dashboard for various Windows shutdown commands


import os
import tkinter as tk

import Shutdown as osf
import tkinter.font as font


def shutdown_in():
    os.system(f"shutdown /s /t {time.get() * 60}")


def select():
    if time.get() == 60:
        shutdownTimer_BTN.config(text=f"Shutdown in 1 Hour")
    elif time.get() == 120:
        shutdownTimer_BTN.config(text=f"Shutdown in 2 Hours")
    else:
        shutdownTimer_BTN.config(text=f"Shutdown in {time.get()} Minutes")


# Window Setup
window = tk.Tk()
window.geometry('600x800')
window.resizable(False, False)
window.title("Shutdown Center")
window.configure(bg='#25262a')

# Image Imports
banner_IMG = tk.PhotoImage(file=r"Media/images/Banner.png")
cancel_IMG = tk.PhotoImage(file=r"Media/images/Cancel.png")
cancelAlt_IMG = tk.PhotoImage(file=r"Media/images/Cancel_ALT.png")
power_IMG = tk.PhotoImage(file=r"Media/images/Power.png")
powerAlt_IMG = tk.PhotoImage(file=r"Media/images/Power_ALT.png")
radio01_IMG = tk.PhotoImage(file=r"Media/images/r1.png")
radio02_IMG = tk.PhotoImage(file=r"Media/images/r2.png")
radio03_IMG = tk.PhotoImage(file=r"Media/images/r3.png")
radio04_IMG = tk.PhotoImage(file=r"Media/images/r4.png")
radio01Alt_IMG = tk.PhotoImage(file=r"Media/images/r1_ALT.png")
radio02Alt_IMG = tk.PhotoImage(file=r"Media/images/r2_ALT.png")
radio03Alt_IMG = tk.PhotoImage(file=r"Media/images/r3_ALT.png")
radio04Alt_IMG = tk.PhotoImage(file=r"Media/images/r4_ALT.png")
restart_IMG = tk.PhotoImage(file=r"Media/images/Restart.png")
restartAlt_IMG = tk.PhotoImage(file=r"Media/images/Reset_ALT.png")
shutdown_IMG = tk.PhotoImage(file=r"Media/images/Shutdown.png")
shutdownAlt_IMG = tk.PhotoImage(file=r"Media/images/Shutdown_ALT.png")
bg_IMG = tk.PhotoImage(file=r"Media/images/bg.png")
banner_BG = tk.Label(window, image=bg_IMG, borderwidth=0, highlightthickness=0).place(x=0, y=0, relwidth=1, relheight=1)

# Create Font object
font_BTN = font.Font(family='Segoe UI')

# GUI elements
# Create Frames
titleBanner_Frame = tk.Frame()
shutdown_Frame = tk.Frame()
shutdownTimer_Frame = tk.Frame()
cancel_Frame = tk.Frame()

# GUI Framework
titleBanner_Frame.grid(row=0, sticky="nsew")
shutdown_Frame.grid(row=1, sticky="nsew")
shutdownTimer_Frame.grid(row=2, sticky="nsew")
cancel_Frame.grid(row=4, sticky="nsew")

# Banner Frame
# Banner
banner_BG = tk.Label(titleBanner_Frame, image=banner_IMG, borderwidth=0, highlightthickness=0)
banner_BG.grid(row=0, column=0, columnspan=4, sticky="nsew")

# Shutdown Frame
# Buttons
shutdown_BTN = tk.Button(
    shutdown_Frame,
    image=power_IMG,
    command=osf.shutdown_now,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#36363e',
    bg='#36363e',
    compound="center",
)
restart_BTN = tk.Button(
    shutdown_Frame,
    image=restart_IMG,
    command=osf.restart,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#36363e',
    bg='#36363e',
    compound="center",
)
# Shutdown Layout
shutdown_BTN.grid(row=0, column=0, sticky="nsew")
restart_BTN.grid(row=0, column=1, sticky="nsew")

# Shutdown Timer Frame
time = tk.IntVar()
# Radios
time_R01 = tk.Radiobutton(
    shutdownTimer_Frame,
    image=radio01_IMG,
    selectimage=radio01Alt_IMG,
    borderwidth=0,
    highlightthickness=0,
    indicatoron=0,
    bg='#34353c',
    activebackground='#34353c',
    selectcolor="#34353c",
    variable=time,
    value=15,
    compound="center",
    command=select

)
time_R02 = tk.Radiobutton(
    shutdownTimer_Frame,
    image=radio02_IMG,
    selectimage=radio02Alt_IMG,
    borderwidth=0,
    highlightthickness=0,
    indicatoron=0,
    bg='#34353c',
    activebackground='#34353c',
    selectcolor="#34353c",
    variable=time,
    value=30,
    compound="center",
    command=select

)
time_R03 = tk.Radiobutton(
    shutdownTimer_Frame,
    image=radio03_IMG,
    selectimage=radio03Alt_IMG,
    borderwidth=0,
    highlightthickness=0,
    indicatoron=0,
    bg='#34353c',
    activebackground='#34353c',
    selectcolor="#34353c",
    variable=time,
    value=60,
    compound="center",
    command=select
)
time_R04 = tk.Radiobutton(
    shutdownTimer_Frame,
    image=radio04_IMG,
    selectimage=radio04Alt_IMG,
    borderwidth=0,
    highlightthickness=0,
    indicatoron=0,
    bg='#34353c',
    activebackground='#34353c',
    selectcolor="#34353c",
    variable=time,
    value=120,
    compound="center",
    command=select
)

# Button
shutdownTimer_BTN = tk.Button(
    shutdownTimer_Frame,
    fg="#8d90a7",
    text=f"Select Shutdown Delay",
    command=shutdown_in,
    image=shutdown_IMG,
    borderwidth=0,
    highlightthickness=0,
    bg='#323239',
    activebackground='#323239',
    compound="center",
)

# Shutdown Timer Layout
time_R01.grid(row=0, column=0, sticky="nsew")
time_R02.grid(row=0, column=1, sticky="nsew")
time_R03.grid(row=0, column=2, sticky="nsew")
time_R04.grid(row=0, column=3, sticky="nsew")
shutdownTimer_BTN.grid(row=1, column=0, columnspan=4, sticky="nsew")
shutdownTimer_BTN['font'] = font_BTN

# Cancel Frame
cancel_BTN = tk.Button(
    cancel_Frame,
    fg="white",
    command=osf.cancel,
    image=cancel_IMG,
    borderwidth=0,
    highlightthickness=0,
    activebackground='#2f3036',
    bg='#2f3036',
    height=0,
)
cancel_BTN.grid(row=0, column=0, sticky="nsew")


# Button binding and gui functions
# GUI functions
def power_up(event, btn):
    btn.configure(image=power_IMG)


def power_down(event, btn):
    btn.configure(image=powerAlt_IMG)


def restart_up(event, btn):
    btn.configure(image=restart_IMG)


def restart_down(event, btn):
    btn.configure(image=restartAlt_IMG)


def shutdown_timer_up(event, btn):
    btn.configure(image=shutdown_IMG)


def shutdown_timer_down(event, btn):
    btn.configure(image=shutdownAlt_IMG)


def cancel_up(event, btn):
    btn.configure(image=cancel_IMG)


def cancel_down(event, btn):
    btn.configure(image=cancelAlt_IMG)


# Binding
shutdown_BTN.bind('<ButtonRelease-1>', lambda event: power_up(event, shutdown_BTN))
shutdown_BTN.bind('<Button-1>', lambda event: power_down(event, shutdown_BTN))
shutdownTimer_BTN.bind('<ButtonRelease-1>', lambda event: shutdown_timer_up(event, shutdownTimer_BTN))
shutdownTimer_BTN.bind('<Button-1>', lambda event: shutdown_timer_down(event, shutdownTimer_BTN))
restart_BTN.bind('<ButtonRelease-1>', lambda event: restart_up(event, restart_BTN))
restart_BTN.bind('<Button-1>', lambda event: restart_down(event, restart_BTN))
cancel_BTN.bind('<ButtonRelease-1>', lambda event: cancel_up(event, cancel_BTN))
cancel_BTN.bind('<Button-1>', lambda event: cancel_down(event, cancel_BTN))

# Main
window.mainloop()
