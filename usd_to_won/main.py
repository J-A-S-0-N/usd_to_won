from tkinter import *


def execute(): 
    won = 1199
    sum = usd * won
def main():
    root = Tk()
    w = Label(root, text="Usd to Won\n") 
    usdbox = Entry(root, text="Enter here .....")
    enterbotten = Button(root, text="Enter", command=execute)
    global usd 
    usd = enterbotten.get()
    w.pack()
    enterbotten.pack()
    usdbox.pack()
    root.mainloop()
    
if __name__ == "__main__":
    main()