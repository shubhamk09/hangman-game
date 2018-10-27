from tkinter import *
import random
from tkinter import messagebox
window = Tk()
val=StringVar()
s=0
foo = ['always', 'believe', 'always', 'strong', 'affect']
#random chosing of string
asd=random.choice(foo)
for a in asd:
    s=s+1
#storing first and last character of string in variable
first=asd[:1]
second=a
#calculating lenght
lenght=len(asd)
lenght2=lenght
total=0
count=0
count2=0
count3=0
#function call 
def check():
    global total
    global count
    global count2
    global count3
    global lenght2
    ex=val.get()
    count2=0
    #checking wheather the string has th character or not
    count=asd.find(ex)+1
    if (count>0):
        count2=asd.count(ex)
    
    lenght2=lenght2-count2
    #creating hangman
    if(count==0):
        count3=count3+1
    if(count3==1):
        can.create_arc(40,10,80,50, start=90, extent=359,width=8)
    elif(count3==2):
        can.create_line(60,50,60,100, width=8 )
    elif(count3==3):
        can.create_line(60,100,20,140, width=8)
    elif(count3==4):
        can.create_line(60,100,100,140, width=8)
    elif(count3==5):
        can.create_line(60,50,20,90, width=8)
    elif(count3==6):
        can.create_line(60,50,100,90, width=8)
        messagebox.showinfo("Hangman","YOU LOSE")
    total=total+count2
    if(total==lenght):
        messagebox.showinfo("Hangman","YOU WIN")
#gui elements
window.title("HANGMAN GAME")
root= Frame(window)
l1=Label(root,text="WELCOME TO HANGMAN GAME", fg="red")
l1.config(width=70)
l1.config(font=("Courier",44))
l2=Label(root,text="Your word start from")
l2.config(font=("Arial",30))
l6=Label(root,text=first, fg="green")
l6.config(font=("Arial",20))
l3=Label(root,text="Your word end with")
l3.config(font=("Arial",30))
l7=Label(root,text=second, fg="green")
l7.config(font=("Arial",20))
l4=Label(root,text="Total number of words")
l4.config(font=("Arial",30))
l8=Label(root,text=lenght, fg="green")
l8.config(font=("Arial",20))
l5=Label(root, text="ENTER A CHARACTER")
l5.config(font=("Arial",30))
e1=Entry(root, textvariable = val)
bn=Button(root,text="check", command=check)
can=Canvas(root,width=200, height=200)
root.pack()
l1.pack()
l2.pack()
l6.pack()
l3.pack()
l7.pack()
l4.pack()
l8.pack()
l5.pack()
e1.pack()
bn.pack()
can.pack()
can.create_line(60,10,180,10, fill="red", width=8 )
can.create_line(180,9,180,190, fill="red", width=8 )
root.mainloop()
