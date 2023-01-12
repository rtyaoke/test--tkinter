import tkinter


def key_down(e):
    label["text"] = e.keycode

if __name__ == '__main__':
    root = tkinter.Tk()

    label = tkinter.Label(font=("Times New Roman", 80))
    label.pack()

    root.bind("<KeyPress>", key_down)

    root.mainloop()
