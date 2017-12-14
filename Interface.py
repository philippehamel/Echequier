from tkinter import Canvas, Tk, Button

# Question 1


class CanvasEchequier(Canvas):
    def __init__(self, root, n_pixels_par_case):
        self.root = root
        self.width = n_pixels_par_case
        self.height = n_pixels_par_case

        super().__init__(self.root, height=self.height, width=self.width)

        self.create_rectangle(50, 50, self.width-50, self.height-50, fill="green")


if __name__ == '__main__':
    root = Tk()

    canvas = CanvasEchequier(root, 600)
    canvas.grid()

    button = Button(root, text="Quit", command=root.quit)
    button.grid(row=1)

    root.mainloop()