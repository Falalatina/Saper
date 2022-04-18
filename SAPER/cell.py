from tkinter import Button
import random
import Settings

class Cell:
    all = []

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # append obj to the cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=10,
            height=4,
            text=f"{self.x},{self.y}"

        )
        btn.bind('<Button-1>', self.left_click_actions)  # left
        btn.bind('<Button-3>', self.right_click_actions)  # right
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()


    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y ==y:
                return cell


    def show_cell(self):
        surronded_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1),
        ]
        print(surronded_cells)

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')


    def right_click_actions(self, event):
        print(event)
        print("kliku kliku")

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, Settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x},{self.y})"
