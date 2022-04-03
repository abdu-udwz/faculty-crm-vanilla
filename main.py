import tkinter as tk
import scene


def main():
    root = tk.Tk()
    main_scene = scene.Scene(root)
    main_scene.pack(fill="both", expand=True)

    root.mainloop()


if __name__ == '__main__':
    main()
