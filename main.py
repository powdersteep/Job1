from tkinter import *
from tkinter import font as tkFont
import time

root = Tk()  # create window

root.title("Job 1")  # title for window
root.geometry('302x100') #main window geometry
#change font size
largerFont = tkFont.Font(family = 'Helvetica', size=12, weight=tkFont.BOLD)
# persons = [['Bill', 2, True], ['Faith', 6, False], ['Jake', 11, True], ['Louise', 15, False]]


lblTest = Label(root, text="Start")
lblTest.grid(column=1, row=2)



#create Timer Window
timeWindow = Toplevel(root)
timeWindow.title("Timer")
timeWindow.geometry("200x200+600+00")
timeNow = Label(timeWindow,text =" ", font=largerFont)
timeNow.pack()

#create Log Window
logWindow = Toplevel(root)
logWindow.title("Log")
logWindow.geometry("300x300+1000+00")


#creation of labels for the Log Window
labelName = Label(logWindow, text="Name              ", font=largerFont)
labelName.grid(column=1, row=1)
labelEvent = Label(logWindow, text="Event                ", font=largerFont)
labelEvent.grid(column=2, row=1)
labelEvent = Label(logWindow, text="Time", font=largerFont)
labelEvent.grid(column=3, row=1)


def current_time():
    return time.strftime("%H:%M:%S")
def manage_time():
    now = current_time()
    timeNow.config( text="T: "+now)
    root.after(1000, manage_time)

manage_time()

# button action listeners
def clickedpause():
    lblTest.configure(text="PAUSED")


def clickedunpause():
    lblTest.configure(text="UNPAUSED")


def clickedend():
    lblTest.configure(text="END")


# button creation
btnPause = Button(root, text="Pause", fg="black", bg="gray", command=clickedpause, height=1, width=13)

btnUnPause = Button(root, text="Un Pause", fg="black", bg="gray", command=clickedunpause, height=1, width=13)

btnEnd = Button(root, text="End", fg="black", bg="gray", command=clickedend, height=1, width=13)

# button placement
btnPause.grid(column=1, row=1)

btnUnPause.grid(column=2, row=1)

btnEnd.grid(column=3, row=1)

# tm.timeClass.run(root)
root.mainloop()
