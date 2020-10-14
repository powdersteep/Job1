from tkinter import*


root = Tk()  # create window

root.title("Job 1")  # title for window
root.geometry('300x300')

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

root.mainloop()
