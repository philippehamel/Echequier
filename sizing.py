import tkinter as tk

root = tk.Tk()


def resize_print(event):
    print("Height: {} ; Width: {}".format(event.height, event.width))


root.bind('<Configure>', resize_print)
quitter = tk.Button(root, text="Quit", command=root.quit)
quitter.grid()

root.mainloop()