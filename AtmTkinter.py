from tkinter import *
import time

root=Tk()
root.geometry("500x500")
root.title("ATM MACHINE")
root.configure(bg="black")

tops = Frame(root, bg="white", width=800, height=50, relief=FLAT)
tops.pack(side=TOP)

f1 = Frame(root, bg="black", width=300, height=700, relief=FLAT)
f1.pack(side=LEFT)


f2= Frame(root, bg="black", width=400, height=700, relief=FLAT)
f2.pack(side=RIGHT)

localtime=time.asctime(time.localtime(time.time()))

lbl1=Label(tops,font=('aria',30,'bold'),text="ATM MACHINE",fg="Black",bd=10,anchor='w')
lbl1.grid(row=0,column=0)

lbl2=Label(tops,font=('aria',20,'bold'),text=localtime,fg="blue",bd=10,anchor='w')
lbl2.grid(row=1,column=0)

number = StringVar()
amount = StringVar()
withd=StringVar()
acca = " "


def bank():
    global acca
    accno = ["0009879","0001234","0009829","1002789","2030456"]
    account = number.get()
    if account in accno:
        label.config(text="Registered user")
        blank = {"0009879":10000,"000123":20000,"0009829":30000}
        balance = bank[account]
        acca = balance
    else:
        label.config(text="Non-Registered User")

    
def deposit():
    global acca
    amo = amount.get()
    bal = acca+amo
    label3.config(text=("Net Balance:",str(bal)))


def withdrawn():
    global acca
    wd =withd.get()
    if acca >= wd:
        ace = acca-wd
        label4.configur(text=("Net Balance : ",str(ace)))
    else:
        label4.config(text="Insufficient Balance")

def bal():
    global acca 
    label5.config(text=("Net Balance",str(acca)))

def reset():
    number.set(" ")
    amount.set(" ")
    withdrawn.set(" ")
    label.config(text=" ")
    label3.config(text="  ")
    label4.config(text="  ")
    label5.config(text="   ")

lbl = Label(f1, font=( 'aria',16, 'bold'),text="Enter the account number :             ",bg = "black",fg="Powder Blue",bd=10,anchor='w')
lbl.grid(row=0,column=3)
txt = Entry(f1, font=('ariel',16,'bold'),textvariable= number ,bd=6,insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=0,column=4)
label = Label(f1, fg="white",bg="black",font=( 'aria',16,'bold'))
label.grid(row=1,column=4)
btnsubmit =Button(f2,padx=16,pady=4, bd=10, fg="black",font=('ariel',16,'bold'),width=7,text="SUBMIT",bg="Powder Blue",command=bank)
btnsubmit.grid(row=0,column=4)


lblTotal = Label(f1,text="  ",fg="white",bg = "black")
lblTotal.grid(row=3,columnspan=10)

lbl = Label(f1, font=( 'aria',16, 'bold'),text="Enter the account to be deposited :        ",bg = "black",fg="Powder Blue",bd=10,anchor='w')
lbl.grid(row=4,column=3)
txt = Entry(f1, font=('ariel',16,'bold'),textvariable= amount,bd=6,insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=4,column=4)
label3 = Label(f1, fg="white",bg="black",font=( 'aria',16,'bold'))
label3.grid(row=5,column=4)
btndeposit =Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="DEPOSIT",bg="Powder Blue",command=deposit)
btndeposit.grid(row=4,column=4)

lbltotal = Label(f1,text="             ",fg="white",bg = "black")
lbltotal.grid(row=7,columnspan=10)

lbl = Label(f1, font=( 'aria',16, 'bold'),text="Enter the account to be withdrawn:              ",bg = "black",fg="Powder Blue",bd=10,anchor='w')
lbl.grid(row=8,column=3)
txt = Entry(f1, font=('ariel',16,'bold'),textvariable= withdrawn,bd=6,insertwidth=4,bg="Powder Blue",justify='right')
txt.grid(row=8,column=4)
label4= Label(f1, fg="white",bg="black",font=( 'aria',16,'bold'))
label4.grid(row=9,column=4)
label5 = Label(f1, fg="white",bg="black",font=( 'aria',16,'bold'))
label5.grid(row=10,column=4)



btnwithdraw =Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="WITHDRAWAL",bg="Powder Blue",command=withdrawn)
btnwithdraw.grid(row=8,column=4)
btnbal =Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="BALANCE",bg="Powder Blue",command=bal)
btnbal.grid(row=10,column=4)
btnreset =Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="RESET",bg="Powder Blue",command=reset)
btnreset.grid(row=11,column=4)
btnexit =Button(f2,padx=16,pady=4,bd=10,fg="black",font=('ariel',16,'bold'),width=7,text="EXIT",bg="Powder Blue",command=root.destroy)
btnexit.grid(row=12,column=4)



root.mainloop()
