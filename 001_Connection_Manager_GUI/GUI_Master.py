from tkinter import *

class RootGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Serial Communication")
        self.root.geometry("360x120")
        self.root.config(bg="white")

class CommGUI:
    def __init__(self, root):
        self.root = root
        self.frame = LabelFrame(root, text="Comm Manager", padx=5, pady=5, bg="white")
        self.label_com = Label(self.frame, text = "Available Port(s): ", bg = "white", width=15, anchor="w")
        self.label_bd = Label(self.frame, text = "Baude Rate: ", bg="white", width = 15, anchor="w")
        self.CommOptionsMenu()
        self.BaudOptionsMenu()
        self.publish()

    def CommOptionsMenu(self):
        coms = ["-", "COM3", "COM4", "COM5"]
        self.clicked_com = StringVar()
        self.clicked_com.set(coms[0])
        self.drop_com = OptionMenu(self.frame, self.clicked_com, *coms)
        self.drop_com.config(width=10)

    def BaudOptionsMenu(self):
        self.clicked_bd = StringVar()
        bds = ["-", "300", "600", "1200", "2400", "4800", "9600", "14400", "19200", "28800", "38400"]
        self.clicked_bd.set(bds[0])
        self.drop_baud = OptionMenu(self.frame, self.clicked_bd, *bds)
        self.drop_baud.config(width=10)
        
    def publish(self):
        self.frame.grid(row=0, column=0, rowspan=3, columnspan=3, padx=5, pady=5)
        self.label_com.grid(column=1, row=2)
        self.drop_com.grid(column=2, row=2)
        self.label_bd.grid(column=1, row=3)
        self.drop_baud.grid(column=2, row=3)


if __name__ == "__main__":
    RootGUI()
    CommGUI()
