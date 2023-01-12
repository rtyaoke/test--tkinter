import tkinter


def create_tile(canvas: tkinter.Canvas):
    tile = [[True if (x + y) % 2 == 0 else False for x in range(10)] for y in range(7)]
    
    for y, x_list in enumerate(tile):
        for x, is_fill in enumerate(x_list):
            if is_fill:
                canvas.create_rectangle(x*80, y*80, x*80+80, y*80+80, fill='gray')



if __name__ == '__main__':
    root = tkinter.Tk()

    canvas = tkinter.Canvas(width=800, height=560, bg='white')
    canvas.pack()
    create_tile(canvas)
    
    root.mainloop()

