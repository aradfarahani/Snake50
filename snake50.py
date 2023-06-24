from tkinter import *
from tkinter import messagebox
from tkinter import StringVar,IntVar
import matplotlib.pyplot as plt
import tkinter.messagebox as tmsg

#-----تابع دکمه ی خروج---------------
def exist():
    if messagebox.askokcancel('exist','Do you want to exist?'):
        frm.destroy()
#----------------------------------------------------------------form 2
def form2():
    frm.destroy()
    frm2=Toplevel
    frm2=Tk(className='Entering information form')
    frm2.geometry('500x500')
    frm2.resizable(width=False, height=False)
    frm2.configure(bg='gray')
    Label(frm2, text='please enter the information carefully !!', bg='gray', fg='yellow', font=20).place(x=10, y=10)
    Label(frm2, text='Name : ', bg='gray', fg='light blue', font=13).place(x=10, y=50)
    s1=StringVar()


    e1 = Entry(frm2)
    e1.place(x=80, y=50)
    Label(frm2, text='Family : ', bg='gray', fg='light blue', font=13).place(x=10, y=90)
    e2 = Entry(frm2)
    e2.place(x=80, y=90)

    Label(frm2, text='Math grade : ', bg='gray', fg='light blue', font=13).place(x=10, y=140)
    e3= Entry(frm2)
    e3.place(x=130, y=140)
    Label(frm2, text='Sience grade : ', bg='gray', fg='light blue', font=13).place(x=10, y=180)
    e4= Entry(frm2)
    e4.place(x=140, y=180)
    Label(frm2, text='Literacy grade : ', bg='gray', fg='light blue', font=13).place(x=10, y=210)
    e5 = Entry(frm2)
    e5.place(x=140, y=210)

#-----------------------------function for average
    def avg():
        result=(int(e3.get())+int(e4.get())+int(e5.get()))/3
        s1.set(str(result))

    def form3():
        def plot_sem1():
            import matplotlib.pyplot as plt
            x = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get())]
            index=["Math", "sience", "literacy"]
            plt.title("Marks of Lessons")
            plt.bar(index,x,label="SEM 1")
            plt.xlabel("Lessons")
            plt.ylabel("Marks")
            plt.title("Marks of Lessons")
            plt.show()
        def plot_sem2():
            import matplotlib.pyplot as plt
            x = [int(sub1ent2.get()),int(sub2ent2.get()),int(sub3ent2.get()),int(sub4ent2.get()),int(sub5ent2.get()),int(sub6ent2.get()),int(sub7ent2.get())]
            index=["Math", "sience", "literacy"]
            plt.title("Marks of Lessons")
            plt.bar(index,x,label="SEM 2")
            plt.xlabel("subjects")
            plt.ylabel("Marks")
            plt.title("Marks of Lessons")
            plt.show()

        def entry_delete():
            sub1ent.delete(first=0,last=50)
            sub2ent.delete(first=0, last=50)
            sub3ent.delete(first=0, last=50)

            sub1ent2.delete(first=0, last=50)
            sub2ent2.delete(first=0, last=50)
            sub3ent2.delete(first=0, last=50)

        root=Tk()
        root.geometry("900x600")
        root.config(bg='wheat3')

        Label(root,text="Plot Grades",font="helvatica 25 bold italic",pady=15,fg="wheat3",bg="black").grid(row=2)

        f4=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
        f4.grid(row=3)

        f2=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
        f2.grid(row=5)

        f3=Frame(root,borderwidth=3,relief=SUNKEN,bg="black")
        f3.grid(row=6,column=7)

        plot1=Label(f2,text="for see the bar plot of grade click on bellow button ",fg="wheat3",bg="black")
        plot1.grid()
        Button(f2,text="Click here",command=plot_sem1,fg="wheat3",bg="black",borderwidth=8).grid(row=1,column=0,pady=10)

        def cgpa_calculator():
            if(len(sub1ent.get())==0 or len(sub2ent.get())==0 or len(sub3ent.get())==0 or len(sub4ent.get())==0 or len(sub5ent.get())==0 or len(sub6ent.get())==0 or len(sub7ent.get())==0 or len(sub1ent2.get())==0 or len(sub2ent2.get())==0 or len(sub3ent2.get())==0 or len(sub4ent2.get())==0 or len(sub5ent2.get())==0 or len(sub6ent2.get())==0 or len(sub7ent2.get())==0):
                tmsg.showwarning("Warning","Fill marks of all the subjects")


            tmsg.showinfo("")
            credit1=[]
            credit2 = []
            marks1 = [int(sub1ent.get()),int(sub2ent.get()),int(sub3ent.get()),int(sub4ent.get()),int(sub5ent.get()),int(sub6ent.get()),int(sub7ent.get())]
            marks2 = [int(sub1ent2.get()),int(sub2ent2.get()),int(sub3ent2.get()),int(sub4ent2.get()),int(sub5ent2.get()),int(sub6ent2.get()),int(sub7ent2.get())]

            tgpa1,first1,first2,i=0,0,0,0
            tgpa2,second1, second2,i1 =0,0,0,0
            print("")
            y=0
            while (y <7):
                credit= int(input(""))
                credit1.append(credit)
                y = y +1

            while (i < 7):
                first1 += credit1[i] * marks1[i]
                first2 += credit1[i]
                i = i + 1
            tgpa1=first1/first2

            print("")
            y1 = 0
            while (y1 < 7):
                credit = int(input(""))
                credit2.append(credit)
                y1 = y1 + 1
            print("")

            while (i1 < 7):
                second1 += credit2[i1] * marks2[i1]
                second2 += credit2[i1]
                i1 = i1 + 1
            tgpa2=second1/second2

            my_label.config(text=f"T {int(tgpa1)}")
            my_label2.config(text=f"T {int(tgpa2)}")

            tmsg.askyesno(title="",message="")
            cgpa=(tgpa1+tgpa2)//2
            grade=''
            if int(cgpa) == 10:
                grade='O'
            elif int(cgpa) ==  9:
                grade = 'A+'
            elif int(cgpa) ==  8:
                grade = 'A'
            elif int(cgpa) ==  7:
                grade = 'B+'
            elif int(cgpa) ==  6:
                grade = 'B'
            elif int(cgpa) ==  5:
                grade = 'C+'
            elif int(cgpa) ==  4:
                grade=""
            else:
                grade=""
            tmsg.showinfo("",f"C {cgpa}  {grade}")

        Label(f4,text="Enter Grades of math Sience and Literacy",fg="wheat3",bg="black",font="helvatica 20 bold italic").grid(row=0,column=1)
        Label(f4,text="grades",fg="wheat3",bg="black").grid(row=1,column=1)
        Label(f4,text="",fg="wheat3",bg="black").grid(row=1,column=2)
        sub1=Label(f4,text="math",fg="wheat3",bg="black")
        sub2=Label(f4,text="Sience",fg="wheat3",bg="black")
        sub3=Label(f4,text="Literacy",fg="wheat3",bg="black")
        sub4=Label(f4,text="",fg="wheat3",bg="black")
        sub5=Label(f4,text="",fg="wheat3",bg="black")
        sub6=Label(f4,text="",fg="wheat3",bg="black")
        sub7=Label(f4,text="",fg="wheat3",bg="black")
        sub1.grid(row=2,column=0)
        sub2.grid(row=3,column=0)
        sub3.grid(row=4,column=0)
        sub4.grid(row=5,column=0)
        sub5.grid(row=6,column=0)
        sub6.grid(row=7,column=0)
        sub7.grid(row=8,column=0)

        sub1val=StringVar()
        sub2val=StringVar()
        sub3val=StringVar()
        sub4val=StringVar()
        sub5val=StringVar()
        sub6val=StringVar()
        sub7val=StringVar()

        sub1ent=Entry(f4,textvariable=sub1val,fg="wheat3",bg="black",insertbackground='wheat3')
        sub2ent=Entry(f4,textvariable=sub2val,fg="wheat3",bg="black",insertbackground='wheat3')
        sub3ent=Entry(f4,textvariable=sub3val,fg="wheat3",bg="black",insertbackground='wheat3')

        sub1ent.grid(row=2,column=1)
        sub2ent.grid(row=3,column=1)
        sub3ent.grid(row=4,column=1)

        my_label = Label(f4,text="",bg="black",fg="wheat3")
        my_label2 = Label(f4,text="",bg="black",fg="wheat3")
        my_label.grid(row=9,column=1)
        my_label2.grid(row=9,column=2)

        root.mainloop()

    Button(frm2,text='next form to see chart', command=form3).place(x=10, y=400)
    Button(frm2,text='calculating average : ',command=avg,bg='blue',fg='white').place(x=10, y=250)
    t=Label(frm2,textvariable=s1)
    t.place(x=150,y=250)

    frm2.mainloop()

#----------------------------------------------------main form
frm=Tk(className='Esmat school')
frm.geometry('700x400')
frm.resizable(width=False,height=False)
frm.configure(bg='white')
Label(frm,text='Welcome to the Esmat school site',font=('Impact',20),fg='indigo').place(x=170,y=10)
Label(frm,text=('1.click on First button to exist'+
                '\n2.click on second button and write the information'+
                '\n3.click on third button in the second button to see the chart'),bg='white',font=13,fg='purple').place(x=160,y=80)
#-------------------------------------buttons of main form
Button(frm,text='exist',command=exist).place(x=30,y=200)
Button(frm,text='button 2',command=form2).place(x=30,y=250)
frm.mainloop()
