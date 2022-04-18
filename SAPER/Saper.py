from tkinter import *
import Settings
import Utilty
from cell import Cell

root = Tk()
# sitting of the window
root.configure(bg="black")
root.geometry(f'{Settings.WIDTH}x{Settings.HEIGHT}')
root.title("Saper")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=Settings.WIDTH,
    height=Utilty.height_prct(25)
                  )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="black",
    width=Utilty.width_prct(25),
    height=Utilty.height_prct(75)
)

left_frame.place(x=0, y=Utilty.height_prct(25))

center_frame = Frame(
    root,
    bg='black',
    width=Utilty.width_prct(75),
    height=Utilty.height_prct(75),
)
center_frame.place(
    x=Utilty.width_prct(25),
    y=Utilty.height_prct(25),
)

# btn1 = Button(
#     center_frame,
#     bg='lightblue',
#     text='First Button'
# )
# btn1.place(x=0, y=0)

# c1 = Cell()
# c1.create_btn_object(center_frame)
# c1.cell_btn_object.grid(
#    column=0, row=0
# )
#
# c2 = Cell()
# c2.create_btn_object(center_frame)
# c2.cell_btn_object.grid(
#    column=0, row=1
# )

for x in range(Settings.GRID_SIZE):
    for y in range(Settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )

Cell.randomize_mines()



# run window
root.mainloop()