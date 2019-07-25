from tkinter import *
import random
import time
from tkinter.font import Font
from tkinter.ttk import Combobox
from tkinter.scrolledtext import ScrolledText
from tkinter.ttk import Progressbar

#function declaration section starts

def call_generate():
  w=int(i.get())
  x=int(j.get())
  y=int(k.get())
  z=int(l.get())
  num = int(lengthcombo.get())
  pwdlen = int(scalelength.get())
  if w==0 and x==0 and y==0 and z==1:	#1
    chars = '!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen,chars)
  elif w==0 and x==0 and y==1 and z==0:	#2
    chars = '0123456789'
    call_generator(num, pwdlen, chars)
  elif w==0 and x==0 and y==1 and z==1:	#3
    chars = '0123456789!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==0 and x==1 and y==0 and z==0:	#4
    chars = 'abcdefghijklmnopqrstuvwxyz'
    call_generator(num, pwdlen, chars)
  elif w==0 and x==1 and y==0 and z==1:	#5
    chars = 'abcdefghijklmnopqrstuvwxyz!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==0 and x==1 and y==1 and z==0:	#6
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789'
    call_generator(num, pwdlen, chars)
  elif w==0 and x==1 and y==1 and z==1:	#7
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==0 and y==0 and z==0:	#8
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==0 and y==0 and z==1:	#9
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==0 and y==1 and z==0:	#10
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==0 and y==1 and z==1:	#11
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==1 and y==0 and z==0:	#12
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==1 and y==0 and z==1:	#13
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==1 and y==1 and z==0:	#14
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    call_generator(num, pwdlen, chars)
  elif w==1 and x==1 and y==1 and z==1:	#15
    chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!#$%&"() *+,-/:;<=>?@[\]^_`{|}'
    call_generator(num, pwdlen, chars)

def call_generator(num, pwdlen, chars):
  readtext.delete(0.0, "end")
  for pwd in range(num):
    password = ''
    for c in range(pwdlen):
      password +=random.choice(chars)
    randompassword = password
    readtext.insert(0.0, randompassword + "\n")

def copy(): 
  readtext.clipboard_clear()
  readtext.clipboard_append(readtext.selection_get())

def cleartext():
  readtext.delete(0.0, "end")

def paste():
  pwdentry.insert(INSERT, readtext.clipboard_get())

def checkpwd():
  password= pwdentry.get()
  lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
  symbollist = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
  length = int()
  upper = int()
  lower = int ()
  number = int()
  symbol = int()
  password_strength = 0
  if len(password) >= 8:
    length = 1
  for i in lower_alphabet:
    if i in password:
      lower = 1
  for i in upper_alphabet:
    if i in password:
      upper = 1
  for i in numbers:
    if i in password:
      number = 1
  for i in symbollist:
    if i in password:
      symbol = 1
  if length == 1:
    password_strength += 1
  if lower == 1:
    password_strength +=1
  if upper == 1:
    password_strength +=1
  if number == 1:
    password_strength +=1
  if symbol == 1:
    password_strength +=2
  password_rank = int()
  if password_strength >= 5:
    password_rank = 980
    progressstatus(password_rank)
    resultnum = Label(psubframe1, text="100%" , font=selectorfont, fg="green")
    resultnum.grid(row=5, column=0, sticky="E", padx=10, pady=10)
    result1 = Label(psubframe1, text="Very Strong Password", font=selectorfont, fg="green")
    result1.grid(row=6, sticky="W", padx=20)
  elif password_strength == 4:
    password_rank = 784
    progressstatus(password_rank)
    resultnum = Label(psubframe1, text="  "+"75%", font=selectorfont, fg="purple")
    resultnum.grid(row=5, column=0, sticky="E", padx=10, pady=10)
    result1 = Label(psubframe1, text="Strong Password"+"  "+"  "+"  "+"  "+"  ", font=selectorfont, fg="purple")
    result1.grid(row=6, column=0, sticky="W", padx=20)
  elif password_strength == 3:
    password_rank = 500
    progressstatus(password_rank)
    resultnum = Label(psubframe1, text="  "+"50%", font=selectorfont, fg="black")
    resultnum.grid(row=5, column=0, sticky="E", padx=10, pady=10)
    result1 = Label(psubframe1, text="Medium Password"+"  "+"  "+"  ", font=selectorfont, fg="black")
    result1.grid(row=6, columnspan=6, sticky="W", padx=20)
  elif password_strength == 2:
    password_rank = 300
    progressstatus(password_rank)
    resultnum = Label(psubframe1, text="  "+"25%", font=selectorfont, fg="red")
    resultnum.grid(row=5, column=0, sticky="E", padx=10, pady=10)
    result1 = Label(psubframe1, text="Weak Password"+"  "+"  "+"  ", font=selectorfont, fg="red")
    result1.grid(row=6, columnspan=6,  sticky="W", padx=20)

def progressstatus(password_rank):
  progress["maximum"]=980
  for i in range(password_rank):
    progress["value"]= i
    time.sleep(0.005)
    progress.update()


def clearpwd():
  pwdentry.delete(0, 1000)



#main window starts


root = Tk()

framefont1=Font(family="Times New Roman", weight="bold", size=23, slant="italic")
selectorfont=Font(size=20)
selectorfont1=Font(size=15)
selectorfont2=Font(size=18)

root.title("Random Password Generator & Strength Checker")
root.geometry("1070x850+120+120")

#randompassword generator frame starts

generatorframe = LabelFrame(root, fg="red" ,text="Random Password Generator", font=framefont1)


#subframe1 starts

subframe1 = LabelFrame(generatorframe)

setnumber = Label(subframe1, text="Set Number of Passwords", fg= "blue", font=selectorfont)
setnumber.grid(row=0, column=0, sticky="W", padx=10)

length=list(range(1,501))
lengthcombo= Combobox(subframe1, values=length, width=27, font=selectorfont1)
lengthcombo.set("Choose Number")
lengthcombo.grid(row=1, column=0,padx=20, sticky="W")


setlength = Label(subframe1, text="Set Password Length", fg= "blue", font=selectorfont)
setlength.grid(row=2, column=0, padx=10, sticky="W")

scalelength =Scale(subframe1, from_=8, to_=32, orient =HORIZONTAL, length=383, width=20, sliderlength=50, font=selectorfont1)
scalelength.set(50)
scalelength.grid(row=3, column=0, padx=20, sticky="W")

choosetype = Label(subframe1, text="Characters Type in Password", fg= "blue", font=selectorfont)
choosetype.grid(row=4, padx=10, sticky="W",)

i = IntVar()
pwdtype1 = Checkbutton(subframe1, text="Uppercase", variable=i, font=selectorfont1)
pwdtype1.grid(row=5, padx=10, sticky="W")

j = IntVar()
pwdtype2 = Checkbutton(subframe1, text="Lowercase", variable=j, font=selectorfont1)
pwdtype2.grid(row=6, padx=10, sticky="W")

k = IntVar()
pwdtype3 = Checkbutton(subframe1, text="Numeric", variable=k, font=selectorfont1)
pwdtype3.grid(row=7, padx=10, sticky="W")

l = IntVar()
pwdtype4 = Checkbutton(subframe1, text="Symbols", variable=l, font=selectorfont1)
pwdtype4.grid(row=8, padx=10, sticky="W")

generatebutton=Button(subframe1, text="Generate Passwords", command=call_generate, font=selectorfont1)
generatebutton.grid(row=9, columnspan=10, padx=30, sticky="W", pady=20)




#subframe2 starts

subframe2 = LabelFrame(generatorframe)

generatetitle = Label(subframe2, text="Generated Passwords", fg= "blue", font=selectorfont)
generatetitle.grid(row=0, column=0)

readtext = ScrolledText(subframe2, font=selectorfont1, width=40, height=10, borderwidth=6)
readtext.grid(row=1, column=0, padx=10, pady=11)

copybutton=Button(subframe2, text="Copy", font=selectorfont1, command=copy)
copybutton.grid(row=2, columnspan=10, padx=30, sticky="W", pady=20)

clearbutton=Button(subframe2, text="Clear", font=selectorfont1, command=cleartext)
clearbutton.grid(row=2, columnspan=10, padx=120, sticky="W", pady=20)


#password strength checker section

passwordframe = LabelFrame(root, fg="red" ,text="Password Strenght Checker", font=framefont1)



#password checker subframe1 starts
psubframe1 = LabelFrame(passwordframe)

enterpassword = Label(psubframe1, text="Enter Password", font=selectorfont, fg="blue")
enterpassword.grid(row=0, column=0, sticky="W", padx=10)

pwdentry = Entry(psubframe1, font=selectorfont1, width=40)
pwdentry.grid(row=1, columnspan=1, sticky="W", padx=20)

pastebutton = Button(psubframe1, text="Paste", font=selectorfont1, command=paste, width=5)
pastebutton.grid(row=2, column=0, sticky="W", padx=20, pady=5)

cleanbutton = Button(psubframe1, text="Clear", font=selectorfont1, command=clearpwd, width=5)
cleanbutton.grid(row=2, column=0, sticky="W", padx=123, pady=5)

#resetbutton = Button(psubframe1, text="Reset", font=selectorfont1, command=reset, width=5)
#resetbutton.grid(row=2, column=0, sticky="W", padx=227, pady=5)

checkbutton = Button(psubframe1, text="Check Strength", font=selectorfont1, width=13, command=checkpwd)
checkbutton.grid(row=3, column=0, sticky="W", padx=20, pady=5)

strength = Label(psubframe1, text="Password Strength", font=selectorfont, fg="blue")
strength.grid(row=4, column=0, sticky="W", padx=10)

progress = Progressbar (psubframe1, orient=HORIZONTAL, length=980, mode='determinate')
progress.grid(row=5, column=0, sticky="W", padx=20, pady=10)

spacelabel1 =Label(psubframe1, text="")
spacelabel1.grid(rowspan=6, pady=15)


#closing section

subframe1.grid(row=0, column=0, sticky="NW", padx=10, pady=10)
subframe2.grid(row=0, column=1, sticky="NE", padx=10, pady=10)
psubframe1.grid(row=0, column=0, sticky="NW", padx=10, pady=10)
generatorframe.grid(sticky="NW", padx=10)
passwordframe.grid(sticky="W", padx=10, pady=20)

root.mainloop()
