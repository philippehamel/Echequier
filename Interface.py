from tkinter import Canvas, Tk, Button

# Question 1


class CanvasEchequier(Canvas):
    def __init__(self, root, n_pixels_par_case):
        self.root = root
        self.n_pixels_par_case = n_pixels_par_case
        self.n_row, self.n_col = 8, 8
        self.width = self.n_row * self.n_pixels_par_case
        self.height = self.n_col * self.n_pixels_par_case

        super().__init__(self.root, height=self.height, width=self.width)

        self.create_rectangle(50, 50, self.width-50, self.height-50, fill="green")

        self.row_name = ['1', '2', '3', '4', '5', '6', '7', '8']
        self.col_name = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'g']

        self.pieces = {
            'a1': 'TB', 'b1': 'CB', 'c1': 'FB', 'd1': 'DB', 'e1': 'RB', 'f1': 'FB', 'g1': 'CB', 'h1': 'TB',
            'a2': 'PB', 'b2': 'PB', 'c2': 'PB', 'd2': 'PB', 'e2': 'PB', 'f2': 'PB', 'g2': 'PB', 'h2': 'PB',
            'a7': 'PN', 'b7': 'PN', 'c7': 'PN', 'd7': 'PN', 'e7': 'PN', 'f7': 'PN', 'g7': 'PN', 'h7': 'PN',
            'a8': 'TN', 'b8': 'CN', 'c8': 'FN', 'd8': 'DN', 'e8': 'RN', 'f8': 'FN', 'g8': 'CN', 'h8': 'TN',
        }

    def draw_case(self):
        for i in self.n_row:
            for j in self.n_col:
                pass
            pass


if __name__ == '__main__':
    root = Tk()

    canvas = CanvasEchequier(root, 100)
    canvas.grid()

    button = Button(root, text="Quit", command=root.quit)
    button.grid(row=1)

    root.mainloop()