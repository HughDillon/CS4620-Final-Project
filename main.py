import tkinter 
from tkinter import *
from tkinter import ttk
import sqlite3
from typing import Sized

def clearDisplay():
    for item in displaytree.get_children():
      displaytree.delete(item)  



def show_adware():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From ADWARE"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")

    


#initialize window and display frame
root = Tk()
root.title('Malware Database Browser')
root.geometry("1500x1000")
displayframe = Frame(root)
displayframe.pack(fill=tkinter.BOTH,side=tkinter.TOP)


#establish database connection
connection = sqlite3.connect('malwaredatabase.db')
cursor = connection.cursor()
query = "SELECT * From VIRUSTYPES"
cursor.execute(query)
rows = cursor.fetchall()
total = cursor.rowcount


#create initial display table
displaytree = ttk.Treeview(displayframe, columns=(1,2,3,4), show="headings", height="15")
displaytree.pack()
for i in rows:
    displaytree.insert('', 'end', values=i)

displaytree.heading(1, text="Malware Type")
displaytree.column(1, minwidth=0,width=150)
displaytree.heading(2, text="Number of Families")
displaytree.column(2, minwidth=0,width=150)
displaytree.heading(3, text="Number of Samples Found")
displaytree.column(3, minwidth=0,width=150)
displaytree.heading(4, text="Description", )
displaytree.column(4, minwidth=0,width=700)

#setup family buttons and labels
buttonFrame= Frame(root)
buttonFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=25)
search_by_type_label = ttk.Label(buttonFrame, text="Select Malware Family to View: ")
search_by_type_label.pack(side=LEFT)

adwareButton = ttk.Button(buttonFrame,text="Adware",command=show_adware)
adwareButton.pack(side=tkinter.LEFT, padx=5)
backdoorButton = ttk.Button(buttonFrame,text="Backdoor",command=show_adware)
backdoorButton.pack(side=tkinter.LEFT, padx=5)
fileInjectorButton = ttk.Button(buttonFrame,text="File Injector",command=show_adware)
fileInjectorButton.pack(side=tkinter.LEFT, padx=5)
noCatButton = ttk.Button(buttonFrame,text="No Category",command=show_adware)
noCatButton.pack(side=tkinter.LEFT, padx=5)
PUAButton = ttk.Button(buttonFrame,text="Potentially Unwanted Application",command=show_adware)
PUAButton.pack(side=tkinter.LEFT, padx=5)
RansomButton = ttk.Button(buttonFrame,text="Ransomware",command=show_adware)
RansomButton.pack(side=tkinter.LEFT, padx=5)
riskButton = ttk.Button(buttonFrame,text="Riskware",command=show_adware)
riskButton.pack(side=tkinter.LEFT, padx=5)
scareButton = ttk.Button(buttonFrame,text="Scareware",command=show_adware)
scareButton.pack(side=tkinter.LEFT, padx=5)
trojanButton = ttk.Button(buttonFrame,text="Trojan",command=show_adware)
trojanButton.pack(side=tkinter.LEFT, padx=5)
bankerButton = ttk.Button(buttonFrame,text="Banker",command=show_adware)
bankerButton.pack(side=tkinter.LEFT, padx=5)
dropperButton = ttk.Button(buttonFrame,text="Dropper",command=show_adware)
dropperButton.pack(side=tkinter.LEFT, padx=5)
smsButton = ttk.Button(buttonFrame,text="SMS",command=show_adware)
smsButton.pack(side=tkinter.LEFT, padx=5)
spyButton = ttk.Button(buttonFrame,text="Spy",command=show_adware)
spyButton.pack(side=tkinter.LEFT, padx=5)
zeroDayButton = ttk.Button(buttonFrame,text="Zero-Day",command=show_adware)
zeroDayButton.pack(side=tkinter.LEFT, padx=5)

connection.close()
root.mainloop()

