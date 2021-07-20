from tkinter import *
root = Tk()
root.geometry("500x300")

def getvals():
    print("Accepted")

#Heading
Label(root, text="Registration form", font="ar 15 bold").grid(row=0, column=3)

#Field Name
name = Label(root, text="Name")
address = Label(root, text="Address")
birthdate = Label(root, text="Birhtdate")
birthplace = Label(root, text="Birthplace")
phone = Label(root, text="Phone")

#Packing Fields
name.grid(row=1, column=2)
address.grid(row=2, column=2)
birthdate.grid(row=3, column=2)
birthplace.grid(row=4, column=2)
phone.grid(row=5, column=2)

namevalue = StringVar
addressvalue= StringVar
birthdatevalue = StringVar
birthplacevalue = StringVar
phonevalue = IntVar
checkvalue = IntVar

#Creatingentryfield
nameentry = Entry(root, textvariable = namevalue)
addressentry = Entry(root, textvariable = addressvalue)
birthdateentry = Entry(root, textvariable = birthdatevalue)
birthplaceentry = Entry(root, textvariable = birthplacevalue)
phoneentry = Entry(root, textvariable = phonevalue)

#Packingentry
nameentry.grid(row=1, column=3)
addressentry.grid(row=2, column=3)
birthdateentry.grid(row=3, column=3)
birthplaceentry.grid(row=4, column=3)
phoneentry.grid(row=5, column=3)

#Creating Checkbox
checkbtn = Checkbutton(text="when agree, please tick the box", variable = checkvalue)
checkbtn.grid(row=6, column=3)

#Submit button
Button(text="Submit", command=getvals).grid(row=7, column =3)


root.mainloop()