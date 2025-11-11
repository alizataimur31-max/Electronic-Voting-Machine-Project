# importing required libraries
import tkinter
import sys
import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Window Setup
window = Tk()
window.title("Electronic Voting Machine")
window.geometry('600x600')
window.configure(background="light green")

provincial_list=["Sindh","Punjab","Baloachistan","Khyber Pakhtunkhwa","Azad Jammu aur Kashmir","Gilgit Baltistan"]
RU_list=["RURAl/دیہی ","URBAN, شہری"]

# Labelling initial inputs from Voter
a = Label(window ,text = "First Name/پہلا نام")  #Firstname
a.grid(row = 0,column = 0)
b = Label(window ,text = "Last Name/آخری نام")  #Lastname
b.grid(row = 1,column = 0)
d=Label(window ,text = "فون نمبر").grid(row = 3,column = 0)  # Phone Number
e=Label(window ,text = "CNIC").grid(row = 4,column = 0)
f=Label(window ,text = "Province").grid(row = 5,column = 0)  #Domicile
g=Label(window ,text = "دیہی / شہری").grid(row = 6,column = 0)  # Rural or Urban

# Entries for initial inputs on tkinter
a1 = ttk.Entry(window)  #Entry for firstname
a1.grid(row = 0,column = 1)
b1 = ttk.Entry(window)  #Entry for lastname
b1.grid(row = 1,column = 1)
d1 = Entry(window)
d1.grid(row = 3,column = 1)  #Entry for phone number
e1 =Entry(window)
e1.grid(row = 4,column = 1)  #Enry for CNIC
f1=ttk.Combobox(values=["Sindh","Punjab","Baloachistan","Khyber Pakhtunkhwa","Azad Jammu aur Kashmir","Gilgit Baltistan"])
f1.grid(row=5,column=1)  #Enrty for domicile
g1 =ttk.Combobox(values=["RURAl/دیہی ","URBAN, شہری"])  #Dropdown list for Rural and Urban
g1.grid(row = 6,column = 1)


def enter_data():
   counter=0
   firstname= a1.get()
   firstname=firstname.upper()
   lastname = b1.get()
   lastname=lastname.upper()
   if len(firstname)==0 or len(lastname)==0:
      tkinter.messagebox.showwarning(title="ERROR", message="FIRST AND LAST NAME REQUIRED")
      counter+=1
   comnum = d1.get()
   if len(comnum)!=11:
      tkinter.messagebox.showwarning(title="ERROR", message="INVALID PHONE NUMBER")
      counter+=1
   CNIC = e1.get()
   if len(CNIC)!=13:
      tkinter.messagebox.showwarning(title="ERROR", message="INVALID CNIC")
      counter+=1
   Province=f1.get()
   if Province not in provincial_list:
      tkinter.messagebox.showwarning(title="ERROR", message="Province NOT FOUND")
      counter += 1
   RU=g1.get()
   if RU not in RU_list:
      tkinter.messagebox.showwarning(title="ERROR", message="ERROR")
      counter += 1
   voter_info=[firstname,lastname,comnum,CNIC,Province,RU]
   if counter == 0:
     command=Votingwindow()
     value=counter
     with open("Voter Information.txt", "a",encoding="utf-8") as voterinfo:
        voterinfo.write(str(voter_info) + "\n")
   voterinfo.close()

def Votingwindow():
   newWindow=Toplevel(window)
   newWindow.geometry("600x600")
   newWindow.configure(background="light pink")

   P=Label(newWindow,text="Political Party/سیاسی جماعت").grid(row=1,column=1)
   P1=Label(newWindow,text="PPP/پاکستان پیپلز پارٹی").grid(row=2,column=1)
   P2 = Label(newWindow, text="PML-N/پاکستان مسلم لیگ نواز").grid(row=3, column=1)
   P3 = Label(newWindow, text="PTI/پاکستان تحریک انصاف").grid(row=4, column=1)

   def handle_selection():
      selected_option = var.get()
      print(selected_option)
      with open("Votes.txt", "a", encoding="utf-8") as file:
         file.write(selected_option+"\n")

   # Variable to store the selected option
   var = StringVar()

   # Create Radiobuttons
   option1 = ttk.Radiobutton(newWindow, text="PPP", variable=var, value="PPP").grid(row=2, column=2)
   option2 = ttk.Radiobutton(newWindow, text="PML-N", variable=var, value="PML-N").grid(row=3, column=2)
   option3 = ttk.Radiobutton(newWindow, text="PTI", variable=var, value="PTI").grid(row=4, column=2)

   # Create a button to handle the selection
   button = ttk.Button(newWindow, text="Select", command=handle_selection).grid(row=5, column=2)

   canvas1=Canvas(newWindow,width=100,height=100)
   canvas1.create_image(110,110, image=PhotoImage(file="C:\\Users\\sanko\\Pictures\\Saved Pictures\\22.png"),anchor="nw")
   canvas1.grid(row=2,column=5)

   canvas2 = Canvas(newWindow, width=100, height=100)
   canvas2.create_image(0, 0, image=PhotoImage(file="C:\\Users\\sanko\\Pictures\\Camera Roll\\PML-N.png"))
   canvas2.grid(row=3, column=5)

   canvas3 = Canvas(newWindow, width=100, height=100)
   canvas3.create_image(0,0, image=PhotoImage(file="C:\\Users\\sanko\\Pictures\\Camera Roll\\PML-N.png"))
   canvas3.grid(row=4, column=5)

   def reset():
      python=sys.executable
      os.execl(python, python, *sys.argv)

   vote=StringVar()
   btn=ttk.Checkbutton(newWindow,text="VOTE KO IZZAT DO",command=reset).grid(row=7,column=5)


btn = ttk.Button(window,command=enter_data,text="Next")
btn.grid(row=7,column=1)

window.mainloop()