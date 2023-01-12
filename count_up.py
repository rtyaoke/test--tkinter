import tkinter


COUNT_INTERVAL = 1000
count = 0

def count_up():
    global count
    count += 1
    label["text"] = count
    root.after(COUNT_INTERVAL, count_up)


if __name__ == '__main__':
    root = tkinter.Tk()

    label = tkinter.Label(font=("Times New Roman", 80))
    label.pack()

    root.after(1000, count_up)

    root.mainloop()
