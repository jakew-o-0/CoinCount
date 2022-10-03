import tkinter
import tkinter.ttk

class Logic:
    def __init__(self):
        targetWeight = {"£2":120, "£1":0, "50p":160, "20p":250, "10p":0, "5p":325, "2p":0, "1p":356}

    def Validate_Data(self):
        pass

class TotalBags_Page(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)
        
        nameLabel = tkinter.Label(self, text="Name")
        totalBagsLabel = tkinter.Label(self, text="Total Bags")
        acccuracyLabel = tkinter.Label(self, text="Accuracy")

        nameLabel.grid(column=0, row=0)
        totalBagsLabel.grid(column=1, row=0)
        acccuracyLabel.grid(column=2, row=0)

class Total_Page(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)

        totalFrame = tkinter.Frame(self, padx=10, pady=10)
        totalMoneyLabel = tkinter.Label(totalFrame, text="TotalMoney: ")
        totalBagsLabel = tkinter.Label(totalFrame, text="TotalBags: ")

        totalFrame.grid(column=0, row=0)
        totalMoneyLabel.grid(column=0, row=0)
        totalBagsLabel.grid(column=0, row=1)


        bagsFrame = tkinter.Frame(self, padx=10, pady= 10)
        bagsCorrect = tkinter.Label(bagsFrame, text="Correct bags: ")
        bagsAccuracy = tkinter.Label(bagsFrame, text="Accuracy: ")

        bagsFrame.grid(column=1, row=0)
        bagsCorrect.grid(column=0, row=0)
        bagsAccuracy.grid(column=0, row=1)

class Home_Page(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)

        nameLabel = tkinter.Label(self, text="Name: ")
        coinTypeLabel = tkinter.Label(self, text="Coin Type: ")
        weightLabel = tkinter.Label(self, text="Weight: ")

        nameSVar = tkinter.StringVar()
        weightSVar = tkinter.StringVar()
        coinTypeSVar = tkinter.StringVar()
        nameEntry = tkinter.Entry(self, textvariable=nameSVar)
        weightEntry = tkinter.Entry(self, textvariable=weightSVar)

        coinTypeCB = tkinter.ttk.Combobox(self, textvariable=coinTypeSVar)
        coinTypeCB['values'] = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
        coinTypeCB['state'] = 'readonly'

        submitButton = tkinter.Button(self, text="Submit", command="")

        nameLabel.grid(column=0,row=0)
        coinTypeLabel.grid(column=0, row=2)
        weightLabel.grid(column=0, row=1)
        nameEntry.grid(column=1, row=0)
        weightEntry.grid(column=1, row=1)
        coinTypeCB.grid(column=1, row=2)
        submitButton.grid(column=0, row=3, columnspan=2)
    
    def submitButton_Pressed(self):
        pass


class gui(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.currentFrame = None
        self.switch_frame(Home_Page)

        menuBar = tkinter.Menu(self)
        self.config(menu=menuBar)

        fmenu = tkinter.Menu(menuBar, tearoff=False)
        fmenu.add_command(label="Home", command=lambda: self.switch_frame(Home_Page))
        fmenu.add_command(label="Total", command=lambda: self.switch_frame(Total_Page))
        fmenu.add_command(label="All Bags", command=lambda: self.switch_frame(TotalBags_Page))
        fmenu.add_separator()
        fmenu.add_command(label="Help", command="")
        fmenu.add_command(label="Quit", command=lambda: self.quit())
        menuBar.add_cascade(label="Options", menu=fmenu)

    ########: changes the curent frame
    ########: when called a new frame is given (nFrame), which is initialised as a child to the gui class
    ########: old frame is destroyed and new frame is packed
    def switch_frame(self, nFrame):
        newFrame = nFrame(self)
        if(self.currentFrame is not None):
            self.currentFrame.destroy()
        self.currentFrame = newFrame
        self.currentFrame.pack(padx=5, pady=5)

if(__name__ == "__main__"):
    gui = gui()
    gui.mainloop()