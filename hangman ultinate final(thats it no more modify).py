
def too(qqq):
    global kl
    if qqq==1:
        w.create_line(20, 20,145, 20,fill='aqua' )
        #
        f3.seek(0)   #label that prints repeated letters(till qqq==6)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))#
    elif qqq==2:
        w.create_line(20, 20,145, 20,fill='aqua' )
        w.create_line(75, 20,75, 50,fill='aqua' )
        f3.seek(0)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))
        
    elif qqq==3:
        w.create_line(20, 20,145, 20,fill='aqua' )
        w.create_line(75, 20,75, 50,fill='aqua' )
        oval = w.create_oval(100,50,50,100, fill="blue")
        f3.seek(0)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))
    elif qqq==4:
        w.create_line(20, 20,145, 20,fill='aqua' )
        w.create_line(75, 20,75, 50,fill='aqua' )
        oval = w.create_oval(100,50,50,100, fill="blue")
        w.create_line(75, 100,75, 170,fill='aqua' )
        f3.seek(0)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))
    elif qqq==5:
        w.create_line(20, 20,145, 20,fill='aqua' )
        w.create_line(75, 20,75, 50,fill='aqua' )
        oval = w.create_oval(100,50,50,100, fill="blue")
        w.create_line(75, 100,75, 170,fill='aqua' )
        w.create_line(75, 170,40, 230,fill='aqua' )
        f3.seek(0)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))
    elif qqq==6:
        w.create_line(20, 20,145, 20,fill='aqua' )
        w.create_line(75, 20,75, 50,fill='aqua' )
        oval = w.create_oval(100,50,50,100, fill="blue")
        w.create_line(75, 100,75, 170,fill='aqua' )
        w.create_line(75, 170,40, 230,fill='aqua' )
        
        w.create_line(75, 170,120, 230,fill='aqua' )
        f3.seek(0)
        lool=f3.read()
        a88=str(lool)
        f3.seek(0,2)
        LOL1=tk.Label(sc1,text="",fg='yellow',bg='purple')
        LOL1.pack()
        LOL1.place(x=60,y=450)
        LOL1.configure(text="repeated letters:{}".format(a88),font=('calibiri',50,'bold'))
        import os
        ss2=os.path.getsize("max.txt")
        if ss2==0:#pure loss. if no correct letters(or just letters) in max
            import tkinter.messagebox
            tk.messagebox.showinfo(title='hello', message='you lost')
            p=tk.messagebox.askyesno(title='hello', message='wanna play again')
            if p==True:
                sc1.destroy()
            
                f3.seek(0)####
                m8=f3.read()
                kl=len(m8)
                rrr=' '*kl
                f3.seek(0)
                f3.write(rrr)
                win2.destroy()
                fo()
            else:
                sc1.destroy()
                win2.destroy()
       
        else:#win loss
            import tkinter.messagebox
            tk.messagebox.showinfo(title='hello', message='you lost')
            p=tk.messagebox.askyesno(title='hello', message='wanna play again')
            if p==True:
                sc1.destroy()
                f.seek(0)
                ddd=' '*len(a)
                f.write(ddd)
                f2.seek(0)
                xxx=' '*len(rt)
                f2.write(xxx)
                f3.seek(0)
                m8=f3.read()
               
                kl=len(m8)
                f3.seek(0)
                rrr=' '*kl
                f3.write(rrr)
                win2.destroy()
                fo()
            else:
                sc1.destroy()
                win2.destroy()



def ji():
    l6.destroy()
    b3.destroy()
def hang():
    global w,canvas,mm,aww
    
    qqq=0
    w=tk.Canvas(sc1,width=150,height=300,bg='magenta')
    w.pack()
    
    w.place(x=800,y=90)
    f3.seek(0)
    aww=f3.read()
    mm=len(aww)
    for d in aww: #counts no of wrong letters (or just letters)(without spaces) present in hang file.
        if d!=' ':
            qqq=qqq+1#no of wrong letters
            too(qqq)
        
    





def prom(s):
    global q1,b7,f,rt,a,l6,b3,mm,kl
    #print(s)
    c=0
    ###
    ####
    
    f=open('ton.txt','r+') #initial first file where letters go to. its the final printing file
    
    
    f2.seek(0)
    w=t.find(s)
    if w==-1:
        f3.write(s) ###was '*' initially.#if wrong letter inputed it goes here.(when s cant be found in the list t it gives output value of -1)
        
        hang()
    elif s in f2.read(): # if s is correct letter and is already there in max file  then it means that this letter has been repeated.   (for repeatation)
        l6=tk.Label(sc1,text="you have repeated this letter!",fg="red",bg="white",font=('times new roman',12,'bold')) #
        l6.pack()
        l6.place(x=320,y=340)
        b3=tk.Button(sc1,text="ok",fg="red",bg="gold",font=("calibiri",11,"bold"),command=ji)
        b3.pack()
        b3.place(x=400,y=380)
        
        
    else:  # if s is correct letter and not there in max file. letter is directly  wriiten to ton.txt
        f2.seek(0,2)
        for j in range(len(t)):
            if t[j]==s:#the letter you have chosen is compared with every letter in the original list t.
                p.append(j)#p is a list that contains the position of the letter you chose.(correct letter that is)
                
                
                
                f2.write(s)
                
                
                    
        
        for m in range(len(p)):
            f.seek(p[m])#p[m] is the position of the letter u chose. we move the cursor pointer to this position in file f.
            f.write(s)#once we moved to that postion in the file we write this ltter in that postion. theerfore the file will contain the letter with apprpriate spaces left to indicate where and how exactly the letter is present in the original word
            f.seek(0)
        #the file now contains the letter thats spaced appropriately in the file just like where it is present in the original word.    
        f.seek(0)
        a=f.read()#reading contents of this file that has this correctly spaced word
        q=str(a)#converting contents of file to string
        q1=tk.Label(sc1,text=q,fg='yellow',bg='orange')# **  --> here we are placing the string in the tkinter window above the dashes by creating a label where the text is this string(q)
        q1.pack()
        q1.place(x=310,y=100)
        q1.configure(text=q,font=('calibiri',50,'bold'))#ps: this actually isnt required at all. you can remove this and stop at ** itself
        p.clear()
        qq=0
        f2.seek(0)
        rt=f2.read()
        for d in rt:  
            if d in t:
                qq=qq+1 # takes count of ONLY LETTERS(NOT SPACES(new game)) in max.txt
        import os
        ss=os.path.getsize("abc.txt")
        
        if qq==x and ss==0: # pure win .#checks wherether the length of correct letters(or just letters only) in max.txt matches the length of x and also checks if hang file is empty for each iteration totally 
            import tkinter.messagebox
            tk.messagebox.showinfo(title="won",message="YOU WON!!")
            hg=tk.messagebox.askyesno(title="continue",message="wanna play again")
            if hg==True:
                sc1.destroy()
                f.seek(0)
                ddd=' '*len(a)
                f.write(ddd)
                f2.seek(0)
                xxx=' '*len(rt)
                f2.write(xxx)
                win2.destroy()
                fo()
            else:
                sc1.destroy()
                win2.destroy()
       
         
        elif qq==x:# loss win. checks for every iteration
            import tkinter.messagebox
            tk.messagebox.showinfo(title="won",message="YOU WON!!")
            hg=tk.messagebox.askyesno(title="continue",message="wanna play again")
            if hg==True:
                sc1.destroy()
                f.seek(0)
                ddd=' '*len(a)
                f.write(ddd)
                f2.seek(0)
                xxx=' '*len(rt)
                f2.write(xxx)
                f3.seek(0)
                m8=f3.read()
                kl=len(m8)
                rrr=' '*kl
                f3.seek(0)
                f3.write(rrr)
                win2.destroy()
                fo()
            else:
                sc1.destroy()
                win2.destroy()
            
        
def ti():
    global s
    
    wy=tk.Canvas(sc1,width=150,height=300,bg='purple')#creating canvas inside sc1.this canvas module is used to create frame inside which i put a-z buttons
    frame=tk.Frame(sc1,bg="red")
    frame.pack()
    frame.place(x=180,y=250)
    l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] #creating the buttons
    for i in range( len(l)//2):
        
        b1=tk.Button(frame,text=l[i],width=3,height=2,bg='pink',command=lambda m=l[i]:prom(m)) #clicking the button(creating button actually)
        b1.grid(row=0,column=i,padx=5, pady=10)
    for j in range( 13,len(l)):
        
        b1=tk.Button(frame,text=l[j],width=3,height=2,bg='pink',command=lambda m=l[j]:prom(m))
        b1.grid(row=6,column=j-13,padx=5, pady=10)
    

    '''
    frame=tk.Frame(sc1,bg="red")
    frame.pack()
    
    button1=tk.Button(frame,text="a",command=lambda m='a':prom(m))#putting button inside canvas
    button1.grid(row=0,column=0)
    
    button2=tk.Button(frame,text="b",command=lambda m='b':prom(m))
    button2.grid(row=0,column=1)
    button3=tk.Button(frame,text="c",command=lambda m='c':prom(m))
    button3.grid(row=0,column=2)
    button4=tk.Button(frame,text="d",command=lambda m='d':prom(m))
    button4.grid(row=0,column=3)
    button5=tk.Button(frame,text="e",command=lambda m='e':prom(m))
    button5.grid(row=0,column=4)
    button6=tk.Button(frame,text="f",command=lambda m='f':prom(m))
    button6.grid(row=0,column=5)
    button7=tk.Button(frame,text="g",command=lambda m='g':prom(m))
    button7.grid(row=0,column=6)
    button8=tk.Button(frame,text="h",command=lambda m='h':prom(m))
    button8.grid(row=0,column=7)
    button9=tk.Button(frame,text="i"command=lambda m='i':prom(m))
    button9.grid(row=0,column=8)
    button10=tk.Button(frame,text="j",command=lambda m='j':prom(m))
    button10.grid(row=0,column=9)
    button11=tk.Button(frame,text="k")
    button11.grid(row=0,column=10)
    button12=tk.Button(frame,text="l")
    button12.grid(row=0,column=11)
    button13=tk.Button(frame,text="m",command=lambda m='m':prom(m))
    button13.grid(row=0,column=12)
    button14=tk.Button(frame,text="n")
    button14.grid(row=0,column=13)
    button15=tk.Button(frame,text="o")
    button15.grid(row=0,column=14)
    button16=tk.Button(frame,text="p",command=lambda m='p':prom(m))
    button16.grid(row=0,column=15)
    button17=tk.Button(frame,text="q")
    button17.grid(row=0,column=16)
    button18=tk.Button(frame,text="r")
    button18.grid(row=0,column=17)
    button19=tk.Button(frame,text="s")
    button19.grid(row=0,column=18)
    button20=tk.Button(frame,text="t")
    button20.grid(row=0,column=19)
    button21=tk.Button(frame,text="u")
    button21.grid(row=0,column=20)
    button22=tk.Button(frame,text="v")
    button22.grid(row=0,column=21)
    button23=tk.Button(frame,text="w")
    button23.grid(row=0,column=22)
    button24=tk.Button(frame,text="x")
    button24.grid(row=0,column=23)
    button25=tk.Button(frame,text="y")
    button25.grid(row=0,column=24)
    button26=tk.Button(frame,text="z")
    button26.grid(row=0,column=25)'''
    
    


def ro(m):
    
    import tkinter as tk
    global win1,s,l,t,p,e1,f2,f3,tk,x,t,sc1
    f3=open('abc.txt','r+') #hang
    f2=open('max.txt','r+') #win

    l=['pamphlet','phone','soldier','queue','corruption','blessing']  
    
    t=l[m-1]
    ans='y'
    p=[]
    x=len(t)
    z='-'*x
    sc1=tk.Toplevel(win2)
    '''win1=tk.Tk()'''
    sc1.geometry('800x500')
    sc1.title("HANGMAN")
    sc1.configure(bg='orange')
    
    
    
    l1=tk.Label(sc1,text="LETS PLAY HANGMAN!", fg='blue',bg='yellow',width=20,height=2, font=('jokerman',20,'italic'))
    l1.pack()
    l2=tk.Label(sc1,text="",bg='silver',fg='maroon', width=7,height=1,relief='raised',font=('calibiri',18,'bold'))
    l2.pack()
    l2.place(x=30,y=100)
    l2.configure(text="Puzzle {}".format(m))
    l3=tk.Label(sc1,text="",fg='#000fff000',bg='orange',font=('calibiri',72))
    l3.pack()
    l3.place(x=310,y=150)
    l3.configure(text=z)
    ti()
   
    '''l4=tk.Label(sc1,text='enter text',bg='purple',fg='yellow', width=7,height=1,font=('calibiri',12,'bold'))

    l4.pack()
    l4.place(x=250,y=245)

    e1=tk.Entry(sc1,bg='red',fg='yellow',relief='raised')
    e1.pack()
    e1.delete(0,'end')
    e1.place(x=350,y=250)
    b1=tk.Button(sc1,text='GO!',bg='blue',fg='aqua',font=('times new roman',12,'bold'),command=prom)
    b1.pack()
    b1.place(x=395,y=280)'''
'''print("welcome to hangman")
print("choose puzzle no")
print("1.puzzle 1")
print("2.puzzle 2")
print("3.puzzle 3")
print("4.puzzle 4")
print("5.puzzle 5")'''
def one():
    m=1
    ro(m)
def two():
    m=2
    ro(m)
def three():
    m=3
    ro(m)
def four():
    m=4
    ro(m)
def five():
    m=5
    ro(m)
def six():
    m=6
    ro(m)

def fo():
    global win2,tk
    import tkinter as tk
    win2=tk.Tk()
    win2.geometry("100x200")
    win2.configure(bg='blue')
    LL1=tk.Label(text="choose puzzle no",fg='yellow',bg='indigo',font=("calibiri",10,"bold"))
    LL1.pack()
    BB1=tk.Checkbutton(text="puzzle 1",bg='red',command=one)
    aa5=BB1.cget('text')
    BB1.pack()
    BB2=tk.Checkbutton(text="puzzle 2",bg='lime',command=two)
    BB2.pack()
    BB3=tk.Checkbutton(text="puzzle 3",bg='red',command=three)
    BB3.pack()
    BB4=tk.Checkbutton(text="puzzle 4",bg='lime',command=four)
    BB4.pack()
    BB5=tk.Checkbutton(text="puzzle 5",bg='red',command=five)
    BB5.pack()
    BB6=tk.Checkbutton(text="puzzle 6",bg='lime',command=six)
    BB6.pack()
  
fo()
