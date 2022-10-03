import tkinter
import tkinter.ttk

class Logic:
    def __init__(self):
        self.targetWeight = {"£2":120, "£1":175, "50p":160, "20p":250, "10p":325, "5p":235, "2p":356, "1p":356}

    def Validate_Data(self, coinType, coinWeight, name):
        ########: checks if the inputed weight is the same as the target weight
        ########: if true, the total correct bags is updated in both the totals dict and the volenteers dict
        ########: other wise the the same is done without incrementing the correct totals
        try:
            if(int(coinWeight) == self.targetWeight[coinType]):
                self.update_Totals(True, name)
                return "Correct Bag"
            else:
                self.update_Totals(False, name)
                return "Incorect Bag"

        ########: input sanitation thangs        
        except(ValueError):
            return "Invalid, please only use a Number"
        except(KeyError):
            return "Please select a coin type"
    
    def update_Totals(self, correct, name):
        with open("CoinCount.txt", 'r') as coinCount:
            total = eval(coinCount.readline())
            volenteers = eval(coinCount.readline())

        ########: updates the total dict
        total["Total"] += 1
        total["TotalBags"] += 1
        total["Accuracy"] = (total["TotalCorrect"] / total["TotalBags"]) * 100
        if(correct):
            total["TotalCorrect"] +=1

        ########: func updates the volenteers list
        self.update_Volenteers(volenteers, name, correct)
        
        with open("./CoinCount.txt", 'w') as coinCount:
            coinCount.write(str(total) + "\n")
            coinCount.write(str(volenteers))
    
    def update_Volenteers(self, volenteers, name, correct):
        if(correct):
            totalCorect = 1
            accuracy = 100
        else:
            totalCorect = 0
            accuracy  = 0

        for i in range(len(volenteers)):
            if(volenteers[i]["name"] == name):
                volenteers[i]["TotalBags"] += 1
                volenteers[i]["TotalCorrect"] += totalCorect
                volenteers[i]["Accuracy"] = (int(volenteers[i]["TotalCorrect"]) / int(volenteers[i]["TotalBags"])) * 100
                return None
        
        volenteers.append(dict({"name":name, "TotalBags":1, "TotalCorrect":totalCorect, "Accuracy":accuracy}))
        
class Help_Page(tkinter.Frame):
    def __init__(self, root):
        tkinter.Frame.__init__(self, root)

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
        weightLabel = tkinter.Label(self, text="Weight(g): ")
        self.outputLabel = tkinter.Label(self)

        self.nameSVar = tkinter.StringVar()
        self.weightSVar = tkinter.StringVar()
        coinTypeSVar = tkinter.StringVar()
        nameEntry = tkinter.Entry(self, textvariable=self.nameSVar)
        weightEntry = tkinter.Entry(self, textvariable=self.weightSVar)

        self.coinTypeCB = tkinter.ttk.Combobox(self, textvariable=coinTypeSVar)
        self.coinTypeCB['values'] = ["£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p"]
        self.coinTypeCB['state'] = 'readonly'

        submitButton = tkinter.Button(self, text="Submit", command=lambda: self.submitButton_Pressed())

        nameLabel.grid(column=0,row=0)
        coinTypeLabel.grid(column=0, row=2)
        weightLabel.grid(column=0, row=1)
        nameEntry.grid(column=1, row=0)
        weightEntry.grid(column=1, row=1)
        self.outputLabel.grid(column=0, row=4, columnspan=2)
        self.coinTypeCB.grid(column=1, row=2)

        submitButton.grid(column=0, row=3, columnspan=2)
    
    def submitButton_Pressed(self):
        logic = Logic()
        outText = logic.Validate_Data(coinType=self.coinTypeCB.get(), coinWeight=self.weightSVar.get(), name=self.nameSVar.get())
        self.outputLabel.config(text=outText)
        
class gui(tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.resizable(False, False)
        self.title("Coin Count")
        self.currentFrame = None
        self.switch_frame(Home_Page)

        menuBar = tkinter.Menu(self)
        self.config(menu=menuBar)

        fmenu = tkinter.Menu(menuBar, tearoff=False)
        fmenu.add_command(label="Home", command=lambda: self.switch_frame(Home_Page))
        fmenu.add_command(label="Total", command=lambda: self.switch_frame(Total_Page))
        fmenu.add_command(label="All Bags", command=lambda: self.switch_frame(TotalBags_Page))
        fmenu.add_separator()
        fmenu.add_command(label="Help", command=lambda: self.switch_frame(Help_Page))
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