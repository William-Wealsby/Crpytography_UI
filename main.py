import tkinter as tk
from tkinter import ttk
from collections import Counter

#import math
#import matplotlib.pyplot as plt
#from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from imports.encode import *
from imports.decode import *
from imports.tools import *

class Fullscreen_Window:

    def __init__(self):
        self.tk = tk.Tk()
        self.tk.title('Code Program')
        self.tk.state('zoomed')
        self.tk.grid_columnconfigure(0, weight=1)
        self.tk.grid_rowconfigure(0, weight=1)

        self.notebook = ttk.Notebook(self.tk)
        self.notebook.grid(pady = 10)
        self.style = ttk.Style()
        self.style.layout('TNotebook.Tab', [])
        self.style.configure("BW.TLabel", foreground = "black", background = "white")

        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)
        self.tk.bind("<Button-3>", self.showMenu)

        self.menubar=tk.Menu(self.tk)
        self.tk.config(menu = self.menubar)

        self.fileMenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label = "File", menu = self.fileMenu)

        self.Encodemenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label= "Encode", menu = self.Encodemenu)

        self.Decodemenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label= "Decode", menu = self.Decodemenu)
    
        self.Toolmenu = tk.Menu(self.menubar)
        self.menubar.add_cascade(label= "Tools", menu = self.Toolmenu)

        #self.rightclick = tk.Menu(self.tk, tearoff=0)
        #self.rightclick.add_command(label="null", command=None)
        #self.rightclick.add_command(label="Exit", command=self.end)


    def toggle_fullscreen(self, event = None):
        self.state = not self.state  # Just toggling the boolean
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event = None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"
    
    def showMenu(self, e):
        self.rightclick.post(e.x_root, e.y_root)
    
    def end(self):
        self.tk.quit()
    

class Frames:

    def __init__(self, name = str, type = None):
        self.name = name
        self.label = ttk.Frame(root.notebook)
        self.label.grid(sticky='nesw')
        root.notebook.add(self.label)
        self.index = root.notebook.index(self.label)
        if type == "main":
            root.fileMenu.add_command(label = self.name, command = self.selecttab)
        if type == "Encode":
            root.Encodemenu.add_command(label = self.name, command = self.selecttab)
        elif type == "Decode":
            root.Decodemenu.add_command(label = self.name, command = self.selecttab)
        elif type == "Tool":
            root.Toolmenu.add_command(label = self.name, command = self.selecttab)

    def selecttab(self):
        root.notebook.select(self.index)

class Buttons:

    def __init__(self, frame, name = str, x = int, y = int, function=None):
        self.label=ttk.Button(frame.label, text = name, command = function)
        self.label.grid(row = y, column = x)

class Labels:
    
    def __init__(self, frame, name = str, x = int, y = int, xspan = 1, yspan = 1):
        self.label=ttk.Label(frame.label, text = name)
        self.label.grid(row = y, column = x, rowspan = yspan, columnspan = xspan)

class EntryBox:
    
    def __init__(self, frame, x = int, y = int, xspan = 1, yspan = 1):
        self.label=ttk.Entry(frame.label)
        self.label.grid(row = y, column = x, rowspan = yspan, columnspan = xspan)

class TextBox:

        def __init__(self, frame, x = int, y = int, xspan = 1, yspan = 1):
            self.label=tk.Text(frame.label)
            self.label.grid(row = y, column = x, rowspan = yspan, columnspan = xspan, sticky="nesw")

#useful functions 
def alphabetise(textmsg = str):
    textmsg=textmsg.lower()
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"]
    for letter in textmsg:
        if letter not in alphabet:
            textmsg=textmsg.replace(letter,"")
    return textmsg
def alphabetise_ws(textmsg = str):
    textmsg=textmsg.lower()
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"," "]
    for letter in textmsg:
        if letter not in alphabet:
            textmsg=textmsg.replace(letter,"")
    return textmsg
def alphabetise_wn(textmsg = str):
    textmsg=textmsg.lower()
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","x","w","y","z"," ","1","2","3","4","5","6","7","8","9","0"]
    for letter in textmsg:
        if letter not in alphabet:
            textmsg=textmsg.replace(letter,"")
    return textmsg


#functions for encode tab

#functions for affine cypher
def sc_cypher():
    a=int(sc_entryA.label.get())
    b=int(sc_entryB.label.get())
    textvar = sc_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    sc_text.label.delete(1.0, "end")
    sc_text.label.insert(1.0, affine_cypher(a,b,textvar))

def sc_clear():
    sc_text.label.delete(1.0, "end")
    sc_entryA.label.delete(0, "end")
    sc_entryB.label.delete(0, "end")

#functions for square code
def Sqc_cypher():
    a=int(Sqc_entryA.label.get())
    b=str(Sqc_entryB.label.get())
    textvar = Sqc_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    Sqc_text.label.delete(1.0, "end")
    Sqc_text.label.insert(1.0, transposition_cypher(a,b,textvar))

def Sqc_clear():
    Sqc_text.label.delete(1.0, "end")
    Sqc_entryA.label.delete(0, "end")
    Sqc_entryB.label.delete(0, "end")

def vc_cypher():
    a=vc_entryA.label.get()
    textvar = vc_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    vc_text.label.delete(1.0, "end")
    vc_text.label.insert(1.0, vigenere_cypher(a,textvar))

def vc_clear():
    vc_text.label.delete(1.0, "end")
    vc_entryA.label.delete(0, "end")

#functions for decode

#functions for affine with key
def scdk_decypher():
    a=int(scd_entryA.label.get())
    b=int(scd_entryB.label.get())
    textvar = scd_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    scd_text.label.delete(1.0, "end")
    scd_text.label.insert(1.0, affine_decypher_wk(a,b,textvar))

def scdk_clear():
    scd_text.label.delete(1.0, "end")
    scd_entryA.label.delete(0, "end")
    scd_entryB.label.delete(0, "end")

#functions for affine without key
def scd_decypher():
    textvar = scd2_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    scd2_text2.label.insert(1.0, affine_decypher_nk(textvar))

def scd_clear():
    scd2_text.label.delete(1.0, "end")
    scd2_text2.label.delete(1.0, "end")
    scd2_label_top3.label.config(text="# of Characters = 0")


def scd_update(event):
    root.tk.after(1, _scd_update)

def _scd_update():
    textvar = scd2_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    scd2_label_top3.label.config(text=f"# of Characters = {len(textvar)}")

#functions for transposition with key
def td_decypher():
    a=int(td_entryA.label.get())
    b=str(td_entryB.label.get())
    textvar = td_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    td_text.label.delete(1.0, "end")
    td_text.label.insert(1.0, transposition_decypher(a,b,textvar))

def td_clear():
    td_text.label.delete(1.0, "end")
    td_entryA.label.delete(0, "end")
    td_entryB.label.delete(0, "end")


#functions for vigenere cypher with key
def vcd_decypher():
    a=vcd_entryA.label.get()
    textvar = vcd_text.label.get(1.0, "end")
    textvar=alphabetise_ws(textvar)
    vcd_text.label.delete(1.0, "end")
    vcd_text.label.insert(1.0, vigenere_decypher(a,textvar))

def vcd_clear():
    vcd_text.label.delete(1.0, "end")
    vcd_entryA.label.delete(0, "end")




#functions for tool tab
def countfromtbox(tbox):
    letters = tbox.label.get(1.0, "end")
    letters = letters.lower()
    dict = Counter(letters)
    templist = []
    for i in dict:
        templist.append((i, dict[i]))
    tlist = sorted(templist)
    print(tlist)
    if tlist[0][0] == "\t":
        tlist.pop(0)
    if tlist[0][0] == "\n":
        tlist.pop(0)
    if tlist[0][0] == " ":
        tlist.pop(0)
    return tlist

def clearfig():
    FCFrameTBox.label.delete(1.0, "end")
    barplot(tool_frame_list[0], 1, 1, {})

#functions for tool text manipulation

def shiftUpper():
    text = TM_text.label.get(1.0, "end")
    text = text.upper()
    TM_text.label.delete(1.0, "end")
    TM_text.label.insert(1.0, text)

def shiftLower():
    text = TM_text.label.get(1.0, "end")
    text = text.lower()
    TM_text.label.delete(1.0, "end")
    TM_text.label.insert(1.0, text)

def delSpaces():
    text = TM_text.label.get(1.0, "end")
    textlist = []
    for letter in text: 
        if letter == " ":
            continue
        textlist.append(letter)
    text = ''.join(textlist)
    TM_text.label.delete(1.0, "end")
    TM_text.label.insert(1.0, text)

def stdise():
    text = TM_text.label.get(1.0, "end")
    TM_text.label.delete(1.0, "end")
    TM_text.label.insert(1.0, wordsplit(text))

def TM_clear():
    TM_text.label.delete(1.0, "end")



if __name__ == "__main__":

    English_Freq=[("e", 0.1202),("t", 0.0910),("a", 0.0812),("o",0.0768),("i", 0.0731),
                ("n", 0.0695),("s", 0.0628),("r", 0.0602),("h",0.0592),("d", 0.0432),
                ("l", 0.0398),("u", 0.0288),("c", 0.0271),("m",0.0261),("f", 0.0230),
                ("y", 0.0211),("w", 0.0209),("g", 0.0203),("p",0.0182),("b", 0.0149),
                ("v", 0.0111),("k", 0.0069),("x", 0.0017),("q",0.0011),("j", 0.0010),
                ("z",0.0007)]

    root = Fullscreen_Window()

    print(root.tk.winfo_geometry())
    #main frames

    main_frame = Frames("Main", "main")

    main_widgets=[Labels(main_frame,"Welcome",1,1)]

    #encode frames

    #affine cypher
    sc_frame = Frames("Affine Cypher", "Encode")
    sc_label_top1 = Labels(sc_frame, "Affine cyphers are monoalphabetic substiution cyphers", 0, 0, 2, 1)
    sc_label_top2 = Labels(sc_frame, "Each letter is mapped one to one to another letter", 0, 1, 2, 1)
    sc_sep_tm = ttk.Separator(sc_frame.label, orient='horizontal')
    sc_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    sc_label_mid1 = Labels(sc_frame, "Key A must take a value of [1,3,5,7,9,11,15,17,19,21,23,25]", 0, 2, 2, 1)
    sc_label_mid2a = Labels(sc_frame, "Input key A:", 0, 3, 1, 1)
    sc_label_mid2b = Labels(sc_frame, "Input key B:",1 ,3, 1, 1)
    sc_entryA = EntryBox(sc_frame, 0, 4)
    sc_entryB = EntryBox(sc_frame, 1, 4)
    sc_sep_mb = ttk.Separator(sc_frame.label, orient='horizontal')
    sc_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    sc_button_cypher =  Buttons(sc_frame, "Cypher", 0, 5, lambda: sc_cypher())
    sc_button_clear = Buttons(sc_frame, "Clear", 1, 5, lambda: sc_clear())
    sc_text = TextBox(sc_frame, 2, 0, 10, 10)

    ## transposition cypher
    Sqc_frame = Frames("Transposition Cypher", "Encode")
    Sqc_label_top1 = Labels(Sqc_frame, "Transposition cyphers", 0, 0, 2, 1)
    Sqc_label_top2 = Labels(Sqc_frame, "They change the ordering but maintain the letter frequency", 0, 1, 2, 1)
    Sqc_sep_tm = ttk.Separator(Sqc_frame.label, orient='horizontal')
    Sqc_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    Sqc_label_mid1 = Labels(Sqc_frame, "The key(str) must be the same length as the # of columns", 0, 2, 2, 1)
    Sqc_label_mid2a = Labels(Sqc_frame, "# of columns:", 0, 3, 1, 1)
    Sqc_label_mid2b = Labels(Sqc_frame, "Input the key:",1 ,3, 1, 1)
    Sqc_entryA = EntryBox(Sqc_frame, 0, 4)
    Sqc_entryB = EntryBox(Sqc_frame, 1, 4)
    Sqc_sep_mb = ttk.Separator(Sqc_frame.label, orient='horizontal')
    Sqc_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    Sqc_button_cypher =  Buttons(Sqc_frame, "Cypher", 0, 5, lambda: Sqc_cypher())
    Sqc_button_clear = Buttons(Sqc_frame, "Clear", 1, 5, lambda: Sqc_clear())
    Sqc_text = TextBox(Sqc_frame, 2, 0, 10, 10)

    #vigenere cypher
    vc_frame = Frames("Vigenère Cypher", "Encode")
    vc_label_top1 = Labels(vc_frame, "Vigenère Cyphers are substitution cyphers", 0, 0, 2, 1)
    vc_label_top2 = Labels(vc_frame, "each letter is incremented depending on the corresponding letter in the key", 0, 1, 2, 1)
    vc_sep_tm = ttk.Separator(vc_frame.label, orient='horizontal')
    vc_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    vc_label_mid1 = Labels(vc_frame, "Enter a string as a key:", 0, 2, 2, 1)
    vc_entryA = EntryBox(vc_frame, 0, 3, 2, 1)
    vc_sep_mb = ttk.Separator(vc_frame.label, orient='horizontal')
    vc_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    vc_button_cypher =  Buttons(vc_frame, "Cypher", 0, 5, lambda: vc_cypher())
    vc_button_clear = Buttons(vc_frame, "Clear", 1, 5, lambda: vc_clear())
    vc_text = TextBox(vc_frame, 2, 0, 10, 10)


    #decode frames

    #Decode Affine with key
    scd_frame = Frames("Affine Decrpytion-With Key", "Decode")
    scd_label_top1 = Labels(scd_frame, "Affine cyphers are monoalphabetic substiution cyphers", 0, 0, 2, 1)
    scd_label_top2 = Labels(scd_frame, "Each letter is mapped one to one to another letter", 0, 1, 2, 1)
    scd_sep_tm = ttk.Separator(scd_frame.label, orient='horizontal')
    scd_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    scd_label_mid1 = Labels(scd_frame, "Key A must take a value of [1,3,5,7,9,11,15,17,19,21,23,25]", 0, 2, 2, 1)
    scd_label_mid2a = Labels(scd_frame, "Input key A:", 0, 3, 1, 1)
    scd_label_mid2b = Labels(scd_frame, "Input key B:",1 ,3, 1, 1)
    scd_entryA = EntryBox(scd_frame, 0, 4)
    scd_entryB = EntryBox(scd_frame, 1, 4)
    scd_sep_mb = ttk.Separator(scd_frame.label, orient='horizontal')
    scd_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    scd_button_cypher =  Buttons(scd_frame, "Decypher", 0, 5, lambda: scdk_decypher())
    scd_button_clear = Buttons(scd_frame, "Clear", 1, 5, lambda: scdk_clear())
    scd_text = TextBox(scd_frame, 2, 0, 10, 10)

    #Decode Affine without key
    scd2_frame = Frames("Affine Decrpytion-Without Key", "Decode")
    scd2_label_top1 = Labels(scd2_frame, "Type the text you want decoded in the left box", 0, 0, 2, 1)
    scd2_label_top2 = Labels(scd2_frame, "Warning: This will be ineffective for small sample sizes of characters, check your text frequency in the tool tab",3,0,14,1)
    scd2_label_top3 = Labels(scd2_frame, "# of Characters = 0", 17, 0, 1, 1)
    scd2_button_cypher =  Buttons(scd2_frame, "Decypher", 18, 0, lambda: scd_decypher())
    scd2_button_clear = Buttons(scd2_frame, "Clear", 19, 0, lambda: scd_clear())
    scd2_text = TextBox(scd2_frame, 0, 1, 10, 10)
    scd2_text2 = TextBox(scd2_frame, 10, 1, 10, 10)
    root.tk.bind("<Key>", scd_update)


    #Decode Transposition with key
    td_frame = Frames("Transposition Decrpytion", "Decode")
    td_label_top1 = Labels(td_frame, "Transposition cyphers", 0, 0, 2, 1)
    td_label_top2 = Labels(td_frame, "They change the ordering but maintain the letter frequency", 0, 1, 2, 1)
    td_sep_tm = ttk.Separator(td_frame.label, orient='horizontal')
    td_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    td_label_mid1 = Labels(td_frame, "The key(str) must be the same length as the # of columns", 0, 2, 2, 1)
    td_label_mid2a = Labels(td_frame, "# of columns:", 0, 3, 1, 1)
    td_label_mid2b = Labels(td_frame, "Input the key:",1 ,3, 1, 1)
    td_entryA = EntryBox(td_frame, 0, 4)
    td_entryB = EntryBox(td_frame, 1, 4)
    td_sep_mb = ttk.Separator(td_frame.label, orient='horizontal')
    td_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    td_button_cypher =  Buttons(td_frame, "Decypher", 0, 5, lambda: td_decypher())
    td_button_clear = Buttons(td_frame, "Clear", 1, 5, lambda: td_clear())
    td_text = TextBox(td_frame, 2, 0, 10, 10)

    #vigenere decode
    vcd_frame = Frames("Vigenère Cypher-With Key", "Decode")
    vcd_label_top1 = Labels(vcd_frame, "Vigenère Cyphers are substitution cyphers", 0, 0, 2, 1)
    vcd_label_top2 = Labels(vcd_frame, "each letter is incremented depending on the corresponding letter in the key", 0, 1, 2, 1)
    vcd_sep_tm = ttk.Separator(vcd_frame.label, orient='horizontal')
    vcd_sep_tm.grid(column=0,row=2,columnspan=2,sticky='new')
    vcd_label_mid1 = Labels(vcd_frame, "Enter a string as a key:", 0, 2, 2, 1)
    vcd_entryA = EntryBox(vcd_frame, 0, 3, 2, 1)
    vcd_sep_mb = ttk.Separator(vcd_frame.label, orient='horizontal')
    vcd_sep_mb.grid(column = 0, row = 5, columnspan = 2 ,sticky = 'new')
    vcd_button_cypher =  Buttons(vcd_frame, "Decypher", 0, 5, lambda: vcd_decypher())
    vcd_button_clear = Buttons(vcd_frame, "Clear", 1, 5, lambda: vcd_clear())
    vcd_text = TextBox(vcd_frame, 2, 0, 10, 10)


    #tool frames

    #letter frequency tool
    tool_frame_list = [Frames("Letter Frequency Chart", "Tool"), Frames("Text Manipulation", "Tool")]
    barplot(tool_frame_list[0], 1, 1, {})
    FCFrameTBox = TextBox(tool_frame_list[0], 15, 1, 10, 10)
    FCButton = Buttons(tool_frame_list[0], "Calculate", 1, 11, lambda: barplot(tool_frame_list[0], 1, 1, countfromtbox(FCFrameTBox)))
    FCButton_Eng = Buttons(tool_frame_list[0], "English Frequencies", 5, 11, lambda: barplot(tool_frame_list[0], 1, 1, sorted(English_Freq)))
    FCButton_clear = Buttons(tool_frame_list[0], "Clear", 9, 11, lambda: clearfig())

    TM_text = TextBox(tool_frame_list[1], 1, 0, 15, 15)
    TM_Button_UP = Buttons(tool_frame_list[1], "Upper Case", 0, 0, lambda: shiftUpper())
    TM_Button_LO = Buttons(tool_frame_list[1], "Lower Case", 0, 1, lambda: shiftLower())
    TM_Button_RS = Buttons(tool_frame_list[1], "Remove Spaces", 0, 2, lambda: delSpaces())
    TM_Button_ST = Buttons(tool_frame_list[1], "Standardise", 0, 3, lambda: stdise())
    TM_Button_clear = Buttons(tool_frame_list[1], "Clear", 0, 4, lambda: TM_clear())
 


    root.fileMenu.add_command(label = "Exit", command = root.end)
    root.tk.mainloop()