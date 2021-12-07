import tkinter 
from tkinter import *
from tkinter import ttk
import sqlite3
from typing import Sized


## Clear the display box
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
    connection.close()

## Output BACKDOOR table
def show_backdoor():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From BACKDOOR"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

## Output FILE_INFECTOR table
def show_fileinfector():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From FILE_INFECTOR"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()
    

## Output PUA table
def show_pua():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From PUA"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output RANSOMWARE table
def show_ransomware():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From RANSOMWARE"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output RISKWARE table
def show_riskware():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From RISKWARE"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output SCAREWARE table
def show_scareware():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From SCAREWARE"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output TROJAN table
def show_trojan():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From TROJAN"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output TROJANBANKER table
def show_trojanbanker():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From TROJAN_BANKER"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output TROJANDROPPER table
def show_trojandropper():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From TROJAN_DROPPER"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

    ## Output TROJANDSMS table
def show_trojansms():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From TROJAN_SMS"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

## Output TROJANSPY table
def show_trojanspy():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From TROJAN_SPY"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

 ## Output ZERODAY table
def show_zeroday():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From ZERO_DAY"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
    displaytree.heading(1, text="SR-Num")
    displaytree.heading(2, text="Malware Name")
    connection.close()

def insertbutton():
    ## open a new window
    #initialize window and display frame
    root = Tk()
    root.title('Add an entry to the database')
    root.geometry("500x200")
    displayframe = Frame(root)
    displayframe.grid()
    srnum = Entry(root, width=30)
    srnum.grid(row=0, column=1, padx=20)
    family = Entry(root, width=30)
    family.grid(row=1, column=1, padx=20)
    numsamples = Entry(root, width=30)
    numsamples.grid(row=2, column=1, padx=20)
    description = Entry(root, width=30)
    description.grid(row=3, column=1, padx=20)
    ##text box labels
    srnum_label = Label(root, text="SR_Num")
    srnum_label.grid(row=0, column=0)
    family_label = Label(root, text="Family")
    family_label.grid(row=1, column=0)
    numsamples_label = Label(root, text="Num_Captured_Samples")
    numsamples_label.grid(row=2, column=0)
    description_label = Label(root, text="Description")
    description_label.grid(row=3, column=0)
    ##submit button
    def submit():
            ## Delete values in text boxes from previous submission
            srnum.delete(0, END)
            family.delete(0, END)
            numsamples.delete(0, END)
            description.delete(0, END)

            connection = sqlite3.connect('malwaredatabase.db')
            c = connection.cursor()

            # Insert into the table
            c.execute("INSERT OR IGNORE INTO ADWARE VALUES (:srnum, :family, :numsamples, :description)",
            {
                'srnum' : srnum.get(),
                'family' : family.get(),
                'numsamples' : numsamples.get(),
                'description' : description.get()
            }
            )
            ## Save changes and close connection to DB
            connection.commit()
            connection.close()
    submit_button = Button(root, text="Add an entry to the Database", command=submit)
    submit_button.grid(row=6, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
            
def mainScreenButton():
    clearDisplay()
    connection = sqlite3.connect('malwaredatabase.db')
    cursor = connection.cursor()
    query = "SELECT * From VIRUSTYPES"
    cursor.execute(query)
    rows = cursor.fetchall()
    total = cursor.rowcount
    for i in rows:
        displaytree.insert('', 'end', values=i)
        
    displaytree.heading(1, text="Malware Type")
    displaytree.heading(2, text="Number of Families")
    connection.close()



def searchDB():
    searchWindow = Tk()
    searchWindow.title('Search')
    searchWindow.geometry("500x500")
        
    numSamples = IntVar()
    options = [
        "Adware",
        "Backdoor",
        "File_Infector",
        "PUA",
        "Ransomware",
        "Riskware",
        "Scareware",
        "Trojan",
        "Trojan_Banker",
        "Trojan_Dropper",
        "Trojan_SMS",
        "Trojan_Spy",
    ]

    typeFrame= ttk.Frame(searchWindow)
    typeFrame.pack(side=tkinter.TOP,pady=10)
    selectionCombo = ttk.Combobox(typeFrame,values=options,width=30,)
    selectionCombo['values'] = options
    selectionCombo.pack(side= tkinter.RIGHT, padx=10)
    typeLabel = ttk.Label(typeFrame, text="Select a Malware Type to Search: ")
    typeLabel.pack(side=tkinter.LEFT,padx=5)


    nameFrame = ttk.Frame(searchWindow)
    nameFrame.pack(side=tkinter.TOP,pady=10)
    nameLable = ttk.Label(nameFrame,text="Search By Malware Name: ")
    nameLable.pack(side=tkinter.LEFT,padx=8)
    nameEntry = ttk.Entry(nameFrame,width=30)
    nameEntry.pack(side=tkinter.RIGHT, padx= 10)

    numOptions = ["Greater Than" , "Less Than", "Equal To"]
    numSearchFrame= ttk.Frame(searchWindow)
    numSearchFrame.pack(side=tkinter.TOP, pady=10)
    numSearchLabel = ttk.Label(numSearchFrame, text="Search by Number of Samples: ")
    numSearchLabel.pack(side=tkinter.LEFT, padx=5)
    numEntry = ttk.Entry(numSearchFrame,width=30,textvariable=numSamples)
    numEntry.pack(side=tkinter.RIGHT, padx= 10)
    comparisonBox = ttk.Combobox(numSearchFrame, state="readonly", values=numOptions,width=20)
    comparisonBox.pack(side = tkinter.LEFT,padx=5)
    

    def runSearch():
        clearDisplay()
        connection = sqlite3.connect('malwaredatabase.db')
        cursor = connection.cursor()
        if nameEntry.get() == "" and (numEntry.get() == "" or int(numEntry.get()) < -1):
            query = "SELECT * From " + selectionCombo.get()
        else:
            if nameEntry.get() == "":
                if comparisonBox.get() == "Greater Than":
                    query = "SELECT * From " + selectionCombo.get() + " " + "WHERE Num_Captured_samples >=" + numEntry.get()
                if comparisonBox.get() == "Less Than":
                    query = "SELECT * From " + selectionCombo.get() + " " + "WHERE Num_Captured_samples <=" + numEntry.get()
                if comparisonBox.get() == "Equal To":
                    query = "SELECT * From " + selectionCombo.get() + " " + "WHERE Num_Captured_samples =" + numEntry.get()
            else:
                query = "SELECT * FROM " + selectionCombo.get() + " " + "WHERE FAMILY LIKE " + "'" + nameEntry.get() + "'"

        cursor.execute(query)
        rows = cursor.fetchall()
        total = cursor.rowcount
        for i in rows:
            displaytree.insert('', 'end', values=i)

        connection.close()

    sbuttonFrame = ttk.Frame(searchWindow)
    sbuttonFrame.pack(side=tkinter.BOTTOM, pady=10)
    sbutton = ttk.Button(sbuttonFrame, text="Search", command=runSearch)
    sbutton.pack(side=tkinter.TOP)
    searchWindow.mainloop()


def deleteitem():
    root = Tk()
    root.title('Delete an entry from the database')
    root.geometry("500x200")
    displayframe = Frame(root)
    displayframe.grid()
    connection = sqlite3.connect('malwaredatabase.db')
    c = connection.cursor()

    delete_box = Entry(root, width=30)
    delete_box.grid(row=0, column=1)
    delete_box_label = Label(
    root, text="Select virus type table to delete from:")
    delete_box_label.grid(row=0, column=0)
    srnum_box = Entry(root, width=30)
    srnum_box.grid(row=1, column=1)
    srnum_box_label = Label(root, text="Delete SR Number:")
    srnum_box_label.grid(row=1, column=0)

    def deleteentry():
        ...
       ## query = StringVar()
       ## query = "DELETE FROM % s WHERE SR_Num = % s" % deletetable, deletesrnum
        ##print(query)
        ##print("hello")
        ##query = "Delete FROM {} WHERE SR_Num = {}".format(deletetable, deletesrnum)

    delete_button = Button(root, text="Delete entry", command=deleteentry())
    delete_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    delete_box.delete(0, END)
    srnum_box.delete(0, END)
    connection.commit()
    connection.close()

#initialize window and display frame
root = Tk()
root.title('Malware Database Browser')
root.geometry("1500x1000")
displayframe = Frame(root)
displayframe.pack(fill=tkinter.BOTH,side=tkinter.TOP)

#create initial display table
displaytree = ttk.Treeview(displayframe, columns=(1,2,3,4), show="headings", height="15")
displaytree.pack()

mainScreenButton()

displaytree.column(1, minwidth=0,width=150)

displaytree.column(2, minwidth=0,width=150)
displaytree.heading(3, text="Number of Samples Found")
displaytree.column(3, minwidth=0,width=150)
displaytree.heading(4, text="Description", )
displaytree.column(4, minwidth=0,width=700)

#setup family buttons and labels
buttonFrame= Frame(root)
buttonFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=10)
search_by_type_label = ttk.Label(buttonFrame, text="Select Malware Family to View: ")
search_by_type_label.pack(side=LEFT)

adwareButton = ttk.Button(buttonFrame,text="Adware",command=show_adware)
adwareButton.pack(side=tkinter.LEFT, padx=5)
backdoorButton = ttk.Button(buttonFrame,text="Backdoor",command=show_backdoor)
backdoorButton.pack(side=tkinter.LEFT, padx=5)
fileInjectorButton = ttk.Button(buttonFrame,text="File Infector",command=show_fileinfector)
fileInjectorButton.pack(side=tkinter.LEFT, padx=5)
##noCatButton = ttk.Button(buttonFrame,text="No Category",command=show_adware)
##noCatButton.pack(side=tkinter.LEFT, padx=5)
PUAButton = ttk.Button(buttonFrame,text="Potentially Unwanted Application",command=show_pua)
PUAButton.pack(side=tkinter.LEFT, padx=5)
RansomButton = ttk.Button(buttonFrame,text="Ransomware",command=show_ransomware)
RansomButton.pack(side=tkinter.LEFT, padx=5)
riskButton = ttk.Button(buttonFrame,text="Riskware",command=show_riskware)
riskButton.pack(side=tkinter.LEFT, padx=5)
scareButton = ttk.Button(buttonFrame,text="Scareware",command=show_scareware)
scareButton.pack(side=tkinter.LEFT, padx=5)
trojanButton = ttk.Button(buttonFrame,text="Trojan",command=show_trojan)
trojanButton.pack(side=tkinter.LEFT, padx=5)
bankerButton = ttk.Button(buttonFrame,text="Banker",command=show_trojanbanker)
bankerButton.pack(side=tkinter.LEFT, padx=5)
dropperButton = ttk.Button(buttonFrame,text="Dropper",command=show_trojandropper)
dropperButton.pack(side=tkinter.LEFT, padx=5)
smsButton = ttk.Button(buttonFrame,text="SMS",command=show_trojansms)
smsButton.pack(side=tkinter.LEFT, padx=5)
spyButton = ttk.Button(buttonFrame,text="Spy",command=show_trojanspy)
spyButton.pack(side=tkinter.LEFT, padx=5)

editingButtonFrame = Frame(root)
editingButtonFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=5)

searchButton = ttk.Button(editingButtonFrame, text="Search Database", command=searchDB)
searchButton.pack(side=tkinter.TOP, pady=10)
insertButton = ttk.Button(editingButtonFrame, text="Insert an entry", command=insertbutton)
insertButton.pack(side=tkinter.TOP, pady=10)
deleteButton = ttk.Button(editingButtonFrame, text="Delete an entry", command=deleteitem)
deleteButton.pack(side=tkinter.TOP, padx=5)


mainMenuButtonFrame = Frame(root)
mainMenuButtonFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=5)
menuButton = ttk.Button(mainMenuButtonFrame,text="Return data to original view",command=mainScreenButton)
menuButton.pack(side=tkinter.TOP, pady=5)




##zeroDayButton = ttk.Button(buttonFrame,text="Zero-Day",command=show_zeroday)
##zeroDayButton.pack(side=tkinter.LEFT, padx=5)



root.mainloop()