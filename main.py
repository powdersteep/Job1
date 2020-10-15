from tkinter import*
import time

root = Tk()  # create window

root.title("Job 1")  # title for window
root.geometry('300x300')


def current_time():
    return time.strftime("%H:%M:%S")    #retrieve current time
def manage_time():
    now = current_time()
    if now!='':                         #check to make sure time isn't empty
        print(now)
        #timeNow.config(text="T: "+now)  #update time label
    root.after(1000,manage_time)
    return current_time()#repeat every second

def createTimerWindow():
    timeWindow = Toplevel(root)
    timeWindow.title("Timer")
    timeWindow.geometry("200x200+600+100")
    timeNow = Label(timeWindow, text="T: "+ manage_time()).pack()

# persons = [['Bill', 2, True], ['Faith', 6, False], ['Jake', 11, True], ['Louise', 15, False]]


lblTest = Label(root, text="Start")
lblTest.grid(column=1, row=2)


# button action listeners
def clickedpause():
    lblTest.configure(text="PAUSED")


def clickedunpause():
    lblTest.configure(text="UNPAUSED")


def clickedend():
    lblTest.configure(text="END")


# button creation
btnPause = Button(root, text="Pause", fg="black", bg="gray", command=clickedpause, height = 1, width = 10)

btnUnPause = Button(root, text="Un Pause", fg="black", bg="gray", command=clickedunpause, height = 1, width = 10)

btnEnd = Button(root, text="End", fg="black", bg="gray", command=clickedend, height = 1, width = 10)

# button placement
btnPause.grid(column=1, row=1)

btnUnPause.grid(column=2, row=1)

btnEnd.grid(column=3, row=1)

createTimerWindow()

root.mainloop()


