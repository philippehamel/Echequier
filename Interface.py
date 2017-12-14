from tkinter import Canvas, Tk, Button


class CanvasEchequier(Canvas):
    def __init__(self, root, n_pixels_par_case):
        self.root = root
        self.n_pixels_par_case = n_pixels_par_case
        self.n_row, self.n_col = 8, 8
        self.width = self.n_row * self.n_pixels_par_case
        self.height = self.n_col * self.n_pixels_par_case

        super().__init__(self.root, height=self.height, width=self.width)

        self.pieces = {
            'a1': 'TB', 'b1': 'CB', 'c1': 'FB', 'd1': 'DB', 'e1': 'RB', 'f1': 'FB', 'g1': 'CB', 'h1': 'TB',
            'a2': 'PB', 'b2': 'PB', 'c2': 'PB', 'd2': 'PB', 'e2': 'PB', 'f2': 'PB', 'g2': 'PB', 'h2': 'PB',
            'a7': 'PN', 'b7': 'PN', 'c7': 'PN', 'd7': 'PN', 'e7': 'PN', 'f7': 'PN', 'g7': 'PN', 'h7': 'PN',
            'a8': 'TN', 'b8': 'CN', 'c8': 'FN', 'd8': 'DN', 'e8': 'RN', 'f8': 'FN', 'g8': 'CN', 'h8': 'TN',
        }

    def draw_case(self):
        for i in range(self.n_row):
            for j in range(self.n_col):
                x0 = j * self.n_pixels_par_case
                x1 = i * self.n_pixels_par_case
                y0 = j * self.n_pixels_par_case + self.n_pixels_par_case
                y1 = i * self.n_pixels_par_case + self.n_pixels_par_case

                if (i + j) % 2 == 0:
                    couleur = "white"
                else:
                    couleur = "grey"

                self.create_rectangle(x0, x1, y0, y1, fill=couleur)

    def draw_pieces(self):
        caracteres_pieces = {'PB': '\u2659',
                             'PN': '\u265f',
                             'TB': '\u2656',
                             'TN': '\u265c',
                             'CB': '\u2658',
                             'CN': '\u265e',
                             'FB': '\u2657',
                             'FN': '\u265d',
                             'RB': '\u2654',
                             'RN': '\u265a',
                             'DB': '\u2655',
                             'DN': '\u265b'
                             }
        for position, pieces in self.pieces.items():
            pass


if __name__ == '__main__':
    root = Tk()

    canvas = CanvasEchequier(root, 100)
    canvas.draw_case()
    canvas.grid()

    button = Button(root, text="Quit", command=root.quit)
    button.grid(row=1)

    root.mainloop()