from tkinter import *
#import array
import numpy as np
#for exit option in file
import sys
#for getting the file from the computer we use the modul filename
from tkinter import filedialog
import os
import matplotlib.pyplot as plt
#function to select a file from the system upon clicking the button
def getfile():
    root.filename=(filedialog.askopenfilename(title="Choose your File",filetypes=(("txt","*.txt"),("All files","*.*"))))
    se.manipulate()
#to transfer file to display the columns to be selected
class se: 
    def manipulate():
        print(root.filename)
        f = open(root.filename, "r") #opening the file selected by the user
        scrollbar.pack(side="right", fill=Y) #to place it vertically
        
        listb.pack(); #pack is the method again
        #for getting the first line of the File selected
        for row in f: 
                break
        arr=[" "] #for creation of an array to place an the list of columns in the Listbox
        arr=row.split( ) #to split the words based on spaces
        #inserting the Columns of the file in the Listbox
        for i in range((len(arr))):
                listb.insert(END,arr[i])
    #Function to select x attributes upon clicking selx button
    def selectx():
        lbx=Label(root,text="Select only 1 attribute for x-coordinate for plotting")
        lbx.place(x=1000,y=180)
        listb.bind('<<ListboxSelect>>', se.onselect)#bind function is used to send the clicked option
    #Function to select y attributes upon clicking sely button
    def selecty():
        lby=Label(root,text="Select only 1 attribute for y-coordinate for plotting")
        lby.place(x=1000,y=430)
        listb.bind('<<ListboxSelect>>',se.onselect1)
    #Onselect function is used to get the index of the column clicked
    def onselect(event):
            w = event.widget #to get the widget
            idx=int(w.curselection()[0]) #curselection is the function to know which widget is selected
            idx1.append(idx)
            value.append(w.get(idx))
            lbxd=Label(root,text=value)
            lbxd.place(x=1000,y=210)
    #onselect1 function is used to get the index of the column clicked
    def onselect1(event):
            w = event.widget
            idx=int(w.curselection()[0]) #curselection is the function to know which widget is clicked
            idx1.append(idx)
            value1.append(w.get(idx))
            lbyd=Label(root,text=value1)
            lbyd.place(x=1000,y=450)
    #plot function used for plotting the data
    def plot1():
            x1=int(idx1[0]) #to convert the index from string to int
            y1=int(idx1[1])
            f=open(root.filename,"r") #open the file selected
            f1=f.readline() #to eliminate the first line of the file selected
            f2=f.readlines() #to read the file line by line
            t=[ ] #
            spl=[ ]
            for row in f2:
                t.append(float(row.split( )[x1]))
                spl.append(float(row.split( )[y1]))
            x=t #assigning the x selected attributes to the x-axis
            y=spl #assigning the y selected attributes to the y-axis
            fig=plt.figure() #to initialise the figure from matplotlib
            ax1=fig.add_subplot(111) #subplot is used to get the plot of the figure
            ax1.set_title("Analysis of data") #to set the title
            ax1.set_xlabel(value) #
            ax1.set_ylabel(value1)
            ax1.plot(x,y,c='r')
            #leg=ax1.legend()
            plt.xticks(np.arange(min(x),max(x)+1,5.0))
            plt.yticks(np.arange(min(y),max(y)+1,1.0))
            plt.show()

#creating a window using Tkinter
root=Tk()
root.title("2D PLOT")
#addig a strins s to display the items in list
global s
s=[]
global arr
global value
value=[]
global idx
idx=[]
global idx1
idx1=[]
global value1
value1=[]
global listb
#creating the frame for listbox
frame1=Frame(root)
frame1.pack()
scrollbar = Scrollbar(frame1, orient="vertical") #scrollbar is used for Listbox for selection
listb=Listbox(frame1,yscrollcommand=scrollbar.set) #listbox is used to display the comments
scrollbar.config(command=listb.yview) #to configure the scrollbar
#adding Menu's
menu = Menu(root) 
root.config(menu=menu) #to config the menu's in the menu 
filemenu = Menu(menu) 
menu.add_cascade(label='File', menu=filemenu) #cascade is used to add the menu to the frame
filemenu.add_command(label='New') #adding the options in the menu File
filemenu.add_command(label='Open') 
filemenu.add_separator() #to add the line which seperates the menu options
filemenu.add_command(label='Exit',command=root.destroy) 
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='About')
#creation of button to load file
button=Button(root,text='Load File',width=25,command=getfile)
button.place(x=100,y=250)
#creating object for class se
p1=se
#button for selecting the x-axis
selx=Button(root,text='SelectX',width=25,command=se.selectx)
selx.place(x=1050,y=150)
#button for selecting the y-axis
sely=Button(root,text='SelectY',width=25,command=se.selecty)
sely.place(x=1050,y=400)
#button for plotting
ploto=Button(root,text="PLOT",width=25,command=se.plot1)
ploto.place(x=590,y=470)
root.geometry("1500x1500") #geometry function is used for initialising the frame size
root.mainloop()
