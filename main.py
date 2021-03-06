import tkinter 
from tkinter import *
from tkinter import ttk
import sqlite3
from typing import Sized
import webbrowser


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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
        
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    displaytree.heading(1, text="SR_Num")
    displaytree.heading(2, text="Family name")
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.heading(4, text="Description", )
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
    srnum.grid(row=1, column=1, padx=20)
    family = Entry(root, width=30)
    family.grid(row=2, column=1, padx=20)
    numsamples = Entry(root, width=30)
    numsamples.grid(row=3, column=1, padx=20)
    description = Entry(root, width=30)
    description.grid(row=4, column=1, padx=20)

    table = Entry(root, width=30)
    table.grid(row=0, column=1, padx=20)
    ##text box labels
    srnum_label = Label(root, text="SR_Num:")
    srnum_label.grid(row=1, column=0)
    family_label = Label(root, text="Family:")
    family_label.grid(row=2, column=0)
    numsamples_label = Label(root, text="Num_Captured_Samples:")
    numsamples_label.grid(row=3, column=0)
    description_label = Label(root, text="Description:")
    description_label.grid(row=4, column=0)
    description_label = Label(root, text="Virustype:")
    description_label.grid(row=0, column=0)
    ##submit button
    def submit():
            ## Delete values in text boxes from previous submission
            

        connection = sqlite3.connect('malwaredatabase.db')
        c = connection.cursor()
        print("INSERT OR IGNORE INTO " + table.get() + " VALUES(" + srnum.get() + ", " + "'" + family.get() + "'" + ", " + numsamples.get() + ", " + "'" + description.get() + "'" + ")")
        c.execute("INSERT OR IGNORE INTO " + table.get() + " VALUES(" + srnum.get() + ", " + "'" + family.get() + "'" + ", " + numsamples.get() + ", " + "'" + description.get() + "'" + ")")
        # Insert into the table
        ##c.execute("INSERT OR IGNORE INTO ADWARE VALUES (:srnum, :family, :numsamples, :description)",
        ##{
            ##'srnum' : srnum.get(),
            ##'family' : family.get(),
            ##'numsamples' : numsamples.get(),
            ##'description' : description.get()
        ##}
        ##)
        ## Save changes and close connection to DB
        srnum.delete(0, END)
        family.delete(0, END)
        numsamples.delete(0, END)
        description.delete(0, END)  
        table.delete(0, END)  
        connection.commit()
        c.close()
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
    displaytree.column(1, minwidth=0,width=150)
    displaytree.heading(2, text="Number of Families")
    displaytree.column(2, minwidth=0,width=150)
    displaytree.heading(3, text="Number of Samples Found")
    displaytree.column(3, minwidth=0,width=150)
    displaytree.heading(4, text="Description", )
    displaytree.column(4, minwidth=0,width=700)

    ## Need to figure out how to output multivalue attributes
    ##displaytree.heading(5, text="Symptoms", )
    ##displaytree.column(5, minwidth=0,width=700)

    connection.close()



def searchDB():
    searchWindow = Tk()
    searchWindow.title('Search')
    searchWindow.geometry("500x300")

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
    nameLable = ttk.Label(nameFrame,text="Search By Malware Family: ")
    nameLable.pack(side=tkinter.LEFT,padx=8)
    nameEntry = ttk.Entry(nameFrame,width=30)
    nameEntry.pack(side=tkinter.RIGHT, padx= 10)

    numOptions = ["Greater Than" , "Less Than", "Equal To"]
    numSearchFrame= ttk.Frame(searchWindow)
    numSearchFrame.pack(side=tkinter.TOP, pady=10)
    numSearchLabel = ttk.Label(numSearchFrame, text="OR: Search by Number of Samples: ")
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
        
        displaytree.heading(1, text="SR_Num")
        displaytree.heading(2, text="Family name")
        displaytree.heading(3, text="Number of Samples Found")
        displaytree.heading(4, text="Description", )
        connection.close()

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
    delete_box_label = Label(root, text="Select virus type table to delete from:")
    delete_box_label.grid(row=0, column=0)
    srnum_box = Entry(root, width=30)
    srnum_box.grid(row=1, column=1)
    srnum_box_label = Label(root, text="Delete SR Number:")
    srnum_box_label.grid(row=1, column=0)

    def deleteentry():
        string = "DELETE FROM " + delete_box.get() + " WHERE SR_Num = " + srnum_box.get()
        print(string)
        c.execute("DELETE FROM " + delete_box.get() + " WHERE SR_NUM = " + srnum_box.get())
        delete_box.delete(0, END)
        srnum_box.delete(0, END) 
        connection.commit()
        connection.close()

    delete_button = Button(root, text="Delete entry", command=deleteentry)
    delete_button.grid(row=4, column=0, columnspan=2, pady=10, padx=10, ipadx=100)
    
   

def compareTwoTables():
    
    searchWindow = Tk()
    searchWindow.title('Compare Two Tables')
    searchWindow.geometry("500x500")
    
    malwareName = StringVar()
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
    selectionCombo0 = ttk.Combobox(typeFrame,values=options,width=30,)
    selectionCombo0['values'] = options
    selectionCombo0.pack(side= tkinter.RIGHT, padx=10)
    tableLabel0 = ttk.Label(typeFrame, text="Select a table to compare")
    tableLabel0.pack(side=tkinter.LEFT,padx=5)

    typeFrame= ttk.Frame(searchWindow)
    typeFrame.pack(side=tkinter.TOP,pady=12)
    selectionCombo1 = ttk.Combobox(typeFrame,values=options,width=30,)
    selectionCombo1['values'] = options
    selectionCombo1.pack(side= tkinter.RIGHT, padx=12)
    tableLabel1 = ttk.Label(typeFrame, text="Select another table")
    tableLabel1.pack(side=tkinter.LEFT,padx=5)

    ## Compare two tables
    ##SELECT * FROM table1 INNER JOIN table2 ON table1.Num_Captured_Samples = table2.Num_Captured_Samples
    def compare():
        clearDisplay()
        connection = sqlite3.connect('malwaredatabase.db')
        cursor = connection.cursor()
        query = "SELECT * FROM " + selectionCombo0.get() + " INNER JOIN " + selectionCombo1.get() + " ON " + selectionCombo0.get() + ".Num_Captured_Samples = " + selectionCombo1.get() + ".Num_Captured_Samples"
        cursor.execute(query)
        rows = cursor.fetchall()
        total = cursor.rowcount /2

        for i in rows:
            j = [i[0],i[1],i[2],i[3]]
            #for k in j:
            displaytree.insert('', 'end', values=j)

        for i in rows:
            k = [i[4],i[5],i[6],i[7]]
            displaytree.insert('', 'end', values=k)
            
        displaytree.heading(1, text="SR_Num")
        displaytree.heading(2, text="Family name")
        displaytree.heading(3, text="Number of Samples Found")
        displaytree.heading(4, text="Description", )

        connection.close()


    submitbuttonFrame = ttk.Frame(searchWindow)
    submitbuttonFrame.pack(side=tkinter.BOTTOM, pady=20)
    submitbutton = ttk.Button(submitbuttonFrame, text="Submit", command=compare)
    submitbutton.pack(side=tkinter.TOP)
    searchWindow.mainloop()

## Open a malwarebytes information page on a certain virustype
def moreInfoBrowserOpener():
    searchWindow = Tk()
    searchWindow.title('More Information')
    searchWindow.geometry("700x150")
    
    malwareName = StringVar()
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
    selectionCombo0 = ttk.Combobox(typeFrame,values=options,width=30,)
    selectionCombo0['values'] = options
    selectionCombo0.pack(side= tkinter.RIGHT, padx=10)
    type = ttk.Label(typeFrame, text="Select a virustype to get more information about\nThis will open a page on your machines default browser")
    type.pack(side=tkinter.LEFT,padx=5)
    
    
    ##webbrowser.open('http://youtube.com')  https://www.malwarebytes.com/adware
    def openPage():
            if selectionCombo0.get() == "File_Infector":
               url = "https://blog.malwarebytes.com/detections/sivis-virus-fileinfector-dds/"
               webbrowser.open(url) 
            elif selectionCombo0.get() == "PUA":
                url = "https://support.malwarebytes.com/hc/en-us/articles/360038522194-Potentially-Unwanted-Programs-and-Potentially-Unwanted-Modifications-Frequently-Asked-Questions-for-Endpoint-Security-customers"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Riskware":
                url = "https://blog.malwarebytes.com/detections/riskware/"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Scareware":
                url = "https://blog.malwarebytes.com/101/2021/07/what-is-scareware/"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Trojan_Banker":
                url = "https://blog.malwarebytes.com/detections/trojan-trickbot/"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Trojan_Dropper":
                url = "https://blog.malwarebytes.com/detections/trojan-dropper/"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Trojan_SMS":
                url = "https://blog.malwarebytes.com/threats/sms-trojan/"
                webbrowser.open(url)
            elif selectionCombo0.get() == "Trojan_Spy":
                url = "https://blog.malwarebytes.com/detections/android-trojan-spy-joker-gfth/"
                webbrowser.open(url)
            else:
                url = "https://www.malwarebytes.com/" + selectionCombo0.get()
                webbrowser.open(url)

    submitbuttonFrame = ttk.Frame(searchWindow)
    submitbuttonFrame.pack(side=tkinter.BOTTOM, pady=20)
    submitbutton = ttk.Button(submitbuttonFrame, text="Submit", command=openPage)
    submitbutton.pack(side=tkinter.TOP)
    searchWindow.mainloop()

def largestNumSamples():
    searchWindow = Tk()
    searchWindow.title('Find a family with the largest number of samples')
    searchWindow.geometry("500x200")
        
    malwareName = StringVar()
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
    selectionCombo0 = ttk.Combobox(typeFrame,values=options,width=30,)
    selectionCombo0['values'] = options
    selectionCombo0.pack(side= tkinter.RIGHT, padx=10)
    type = ttk.Label(typeFrame, text="Select a virustype:")
    type.pack(side=tkinter.LEFT,padx=5)

    ## SELECT FAMILY, MAX(Num_Captured_Samples) FROM ADWARE
    def findLargestNumSamples():
            clearDisplay()
            connection = sqlite3.connect('malwaredatabase.db')
            c = connection.cursor()
            query = "SELECT FAMILY, MAX(Num_Captured_Samples) FROM " + selectionCombo0.get()
            c.execute(query)
            rows = c.fetchall()
            total = c.rowcount
            for i in rows:
                displaytree.insert('', 'end', values=i)

            displaytree.heading(1, text="Family")
            displaytree.heading(2,text="Number of Samples")
            displaytree.heading(3,text="")
            displaytree.heading(4,text="")
            connection.close()
            

    submitbuttonFrame = ttk.Frame(searchWindow)
    submitbuttonFrame.pack(side=tkinter.BOTTOM, pady=20)
    submitbutton = ttk.Button(submitbuttonFrame, text="Submit", command=findLargestNumSamples)
    submitbutton.pack(side=tkinter.TOP)
    searchWindow.mainloop()

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

searchButton = ttk.Button(editingButtonFrame, text="Search Database", width=50, command=searchDB)
searchButton.pack(side=tkinter.TOP, pady=10)
insertButton = ttk.Button(editingButtonFrame, text="Insert an entry", width=50, command=insertbutton)
insertButton.pack(side=tkinter.TOP, pady=10)
deleteButton = ttk.Button(editingButtonFrame, text="Delete an entry", width=50, command=deleteitem)
deleteButton.pack(side=tkinter.TOP, padx=5)


mainMenuButtonFrame = Frame(root)
mainMenuButtonFrame.pack(fill=tkinter.BOTH,side=tkinter.BOTTOM, pady=5)
menuButton = ttk.Button(mainMenuButtonFrame,text="Return to the main menu screen",width=50,command=mainScreenButton)
menuButton.pack(side=tkinter.TOP, pady=5)

compareTwoTablesFrame = Frame(root)
compareTwoTablesFrame = Frame(root)
compareTwoTablesFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=5)
compareTwoTablesButton = ttk.Button(editingButtonFrame,text="Match number of samples between two tables", width=50, command=compareTwoTables)
compareTwoTablesButton.pack(side=tkinter.TOP, pady=10)


largestNumSamplesFrame = Frame(root)
largestNumSamplesFrame = Frame(root)
largestNumSamplesFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=8)
largestNumSamplesButton = ttk.Button(editingButtonFrame,text="Find a family with the largest number of samples",width=50, command=largestNumSamples)
largestNumSamplesButton.pack(side=tkinter.TOP, pady=8)

moreInfoFrame = Frame(root)
moreInfoFrame = Frame(root)
moreInfoFrame.pack(fill=tkinter.BOTH,side=tkinter.TOP, pady=9)
moreInfoButton = ttk.Button(editingButtonFrame,text="Get more information on a virustype", width=50,command=moreInfoBrowserOpener)
moreInfoButton.pack(side=tkinter.TOP, pady=9)







##zeroDayButton = ttk.Button(buttonFrame,text="Zero-Day",command=show_zeroday)
##zeroDayButton.pack(side=tkinter.LEFT, padx=5)



root.mainloop()