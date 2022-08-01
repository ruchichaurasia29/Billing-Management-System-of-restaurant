from tkinter import *
import tkinter.messagebox as tmsg
from datetime import datetime
import pytz
import random
import mysql.connector
root=Tk()
root.geometry("1300x780")
root.title("BILLING MANAGEMENT SYSTEM")


def total():
    try:
        a1=int(a_entry.get())
    except:
        a1=0
    try:
        b1=int(b_entry.get())
    except:
        b1=0
    try:
        c1=int(c_entry.get())
    except:
        c1=0
    try:
        d1=int(d_entry.get())
    except:
        d1=0
    try:
        e1=int(e_entry.get())
    except:
        e1=0
    try:
        f1=int(f_entry.get())
    except:
        f1=0
    try:
        g1=int(g_entry.get())
    except:
        g1=0
    try:
        h1=int(h_entry.get())
    except:
        h1=0
    try:
        i1=int(i_entry.get())
    except:
        i1=0
    try:
        j1=int(j_entry.get())
    except:
        j1=0
    try:
        k1=int(k_entry.get())
    except:
        k1=0
    try:
        l1=int(l_entry.get())
    except:
        l1=0
    try:
        m1=int(m_entry.get())
    except:
        m1=0
    try:
        n1=int(n_entry.get())
    except:
        n1=0
    try:
        o1=int(o_entry.get())
    except:
        o1=0
    try:
        p1=int(p_entry.get())
    except:
        p1=0
    try:
        q1=int(q_entry.get())
    except:
        q1=0
    try:
        r1=int(r_entry.get())
    except:
        r1=0
    try:
        s1=int(s_entry.get())
    except:
        s1=0
    try:
        t1=int(t_entry.get())
    except:
        t1=0
    try:
        u1=int(u_entry.get())
    except:
        u1=0
    try:
        v1=int(v_entry.get())
    except:
        v1=0
    try:
        w1=int(w_entry.get())
    except:
        w1=0
    try:
        x1=int(x_entry.get())
    except:
        x1=0
    try:
        odd11=int(odd1_entry.get())
    except:
        odd11=0
    try:
        odd22=int(odd2_entry.get())
    except:
        odd22=0
    try:
        even11=int(even1_entry.get())
    except:
        even11=0
    try:
        even22=int(even2_entry.get())
    except:
        even22=0

    try:
        odd33=int(odd3_entry.get())
    except:
        odd33=0
    try:
        odd44=int(odd4_entry.get())
    except:
        odd44=0

    try:
        even33=int(even3_entry.get())
    except:
        even33=0
    try:
        even44 = int(even4_entry.get())
    except:
        even44 = 0


    a2=a1*80
    b2=b1*100
    c2=c1*20
    d2=d1*70
    e2=e1*40
    f2=f1*30
    g2=g1*300
    h2=h1*250
    i2=i1*400
    j2=j1*500
    k2=k1*700
    l2=l1*450
    m2=m1*60
    n2=n1*80
    o2=o1*100
    p2=p1*80
    q2=q1*100
    r2=r1*70
    s2=s1*40
    t2=t1*70
    u2=u1*50
    v2=v1*100
    w2=w1*80
    x2=x1*60
    odd111=odd11*100
    odd222=odd22*20
    even111=even11*450
    even222=even22*500
    odd333=odd33*150
    odd444=odd44*200
    even333=even33*60
    even444=even44*50

    bill_no=StringVar()
    x=random.randint(1000,9999)
    bill_no.set(str(x))
    IST=pytz.timezone("Asia/Kolkata")
    data=datetime.now(IST)
    date_now=data.strftime("%d %b %Y")
    time_now=data.strftime("%H:%M:%S %p")
    total_cost=a2+b2+c2+d2+e2+f2+g2+h2+i2+j2+k2+l2+m2+n2+o2+p2+q2+r2+s2+t2+u2+v2+w2+x2+odd111+odd222+even111+even222+odd333+odd444+even333+even444+2.00

    if user_entry.get()=="" and num_entry.get()=="" and email_entry.get()=="":
        tmsg.showerror("Status","Username and Phone Number is required")
    elif (a_entry.get()=="" and b_entry.get()=="" and c_entry.get()=="" and d_entry.get()=="" and
        e_entry.get()=="" and f_entry.get()=="" and g_entry.get()=="" and h_entry.get()=="" and
        i_entry.get()=="" and j_entry.get()=="" and k_entry.get()=="" and l_entry.get()=="" and
        m_entry.get()=="" and n_entry.get()=="" and o_entry.get()=="" and p_entry.get()=="" and
        q_entry.get()=="" and r_entry.get()=="" and s_entry.get()=="" and t_entry.get()=="" and
        u_entry.get()=="" and v_entry.get()=="" and w_entry.get()=="" and x_entry.get()==""
and  odd1_entry.get() == "" and odd2_entry.get() == "" and even1_entry.get() == "" and even2_entry.get() == "" and
odd3_entry.get() == "" and odd4_entry.get() == "" and even3_entry.get() == "" and even4_entry.get() == ""
    ):
        tmsg.showinfo("Status","Please select products")
    else:
        tax1_entry.insert(END,f'Rs. 0.00')
        tax2_entry.insert(END, f'Rs. 0.00')
        tax3_entry.insert(END, f'Rs. 0.00')
        tax4_entry.insert(END, f'Rs. 0.00')
        tax5_entry.insert(END, f'Rs. 2.00')

        text.insert(END,f'\nBill Number:\t{bill_no.get()}')
        text.insert(END,f'\nDate:{date_now}\t\t\tTime:{time_now}')
        text.insert(END,f'\n-----------------------------------------------------------------------------------')
        text.insert(END,f'\nUsername\t\t\t{user_entry.get()}')
        text.insert(END,f'\nPhone Number\t\t\t{num_entry.get()}')
        text.insert(END,f'\nEmail\t\t\t{email_entry.get()}')
        text.insert(END,'\n\nItems\t\tQuantity\t\tCost of Items')
        if a_entry.get()!="":
            text.insert(END,f'\nLassi\t\t{a_entry.get()}\t\t\t{a2}')
        if b_entry.get()!="":
            text.insert(END,f'\nCoffee\t\t{b_entry.get()}\t\t\t{b2}')
        if c_entry.get()!= "":
            text.insert(END, f'\nTea\t\t{c_entry.get()}\t\t\t{c2}')
        if d_entry.get() != "":
            text.insert(END, f'\nBadam Milk\t\t{d_entry.get()}\t\t\t{d2}')
        if e_entry.get()!= "":
            text.insert(END, f'\nCold Drink\t\t{e_entry.get()}\t\t\t{e2}')
        if f_entry.get() != "":
            text.insert(END, f'\nShikanji\t\t{f_entry.get()}\t\t\t{f2}')
        if odd1_entry.get()!= "":
            text.insert(END, f'\nMocktails\t\t{odd1_entry.get()}\t\t\t{odd111}')
        if odd2_entry.get() != "":
            text.insert(END, f'\nWater\t\t{odd2_entry.get()}\t\t\t{odd222}')
        if g_entry.get()!= "":
            text.insert(END, f'\nChocolate\t\t{g_entry.get()}\t\t\t{g2}')
        if h_entry.get() != "":
            text.insert(END, f'\nOreo\t\t{h_entry.get()}\t\t\t{h2}')
        if i_entry.get()!= "":
            text.insert(END, f'\nBlack Forest\t\t{i_entry.get()}\t\t\t{i2}')
        if j_entry.get() != "":
            text.insert(END, f'\nPine Apple\t\t{j_entry.get()}\t\t\t{j2}')
        if k_entry.get()!= "":
            text.insert(END, f'\nBrownie\t\t{k_entry.get()}\t\t\t{k2}')
        if l_entry.get() != "":
            text.insert(END, f'\nVanila\t\t{l_entry.get()}\t\t\t{l2}')
        if even1_entry.get()!= "":
            text.insert(END, f'\nBanana\t\t{even1_entry.get()}\t\t\t{even111}')
        if even2_entry.get() != "":
            text.insert(END, f'\nCoffee\t\t{even2_entry.get()}\t\t\t{even222}')
        if m_entry.get()!= "":
            text.insert(END, f'\nIdli\t\t{m_entry.get()}\t\t\t{ m2}')
        if n_entry.get() != "":
            text.insert(END, f'\nDosa\t\t{n_entry.get()}\t\t\t{n2}')
        if o_entry.get()!= "":
            text.insert(END, f'\nSambhar\t\t{o_entry.get()}\t\t\t{o2}')
        if p_entry.get() != "":
            text.insert(END, f'\nVada\t\t{p_entry.get()}\t\t\t{p2}')
        if q_entry.get()!= "":
            text.insert(END, f'\nAppam\t\t{q_entry.get()}\t\t\t{q2}')
        if r_entry.get() != "":
            text.insert(END, f'\nPuttu\t\t{r_entry.get()}\t\t\t{r2}')
        if odd3_entry.get()!= "":
            text.insert(END, f'\nCuisines\t\t{odd3_entry.get()}\t\t\t{odd333}')
        if odd4_entry.get() != "":
            text.insert(END, f'\nPongal\t\t{odd4_entry.get()}\t\t\t{odd444}')
        if s_entry.get()!= "":
            text.insert(END, f'\nChapati\t\t{s_entry.get()}\t\t\t{s2}')
        if t_entry.get() != "":
            text.insert(END, f'\nDaal\t\t{t_entry.get()}\t\t\t{t2}')
        if u_entry.get()!= "":
            text.insert(END, f'\nRice\t\t{u_entry.get()}\t\t\t{u2}')
        if v_entry.get() != "":
            text.insert(END, f'\nPaneer\t\t{v_entry.get()}\t\t\t{v2}')
        if w_entry.get()!= "":
            text.insert(END, f'\nBiryani\t\t{w_entry.get()}\t\t\t{w2}')
        if x_entry.get() != "":
            text.insert(END, f'\nVeg sabji\t\t{x_entry.get()}\t\t\t{x2}')
        if even3_entry.get()!= "":
            text.insert(END, f'\nSoup\t\t{even3_entry.get()}\t\t\t{even333}')
        if even4_entry.get() != "":
            text.insert(END, f'\nCerels\t\t{even4_entry.get()}\t\t\t{even444}')

        text.insert(END,f'\n\nTax on drinks :\tRs.0.00')
        text.insert(END,f'\nTax on Cakes :\tRs.0.00')
        text.insert(END,f'\nTax on South Indian Food :\tRs.0.00')
        text.insert(END,f'\nTax on Food :\tRs.0.00')
        text.insert(END,f'\nService tax : Rs.2.00')
        text.insert(END,f'\n\nYour Total Amount :\tRs.{total_cost}\n\n')

        con = mysql.connector.connect(host='localhost', user='root', password='', database='bill_record')
        cursor = con.cursor()
        cursor.execute("insert into bill_details values('" + user_entry.get() + "','" + num_entry.get() + "','" +
                       email_entry.get() + "','" + a_entry.get() + "','" + b_entry.get() + "','" +
                       c_entry.get() + "','" + d_entry.get() + "','" + e_entry.get() + "','" +
                       f_entry.get() + "','" + g_entry.get() + "','" + h_entry.get() + "','" + i_entry.get()
                       + "','" + j_entry.get() + "','" + k_entry.get() + "','" + l_entry.get() + "','" +
                       m_entry.get() + "','" + n_entry.get() + "','" + o_entry.get() + "','" + p_entry.get() + "','" +
                       q_entry.get() + "','" + r_entry.get() + "','" + s_entry.get() + "','" + t_entry.get() + "','" +
                       u_entry.get() + "','" + v_entry.get() + "','" + w_entry.get() + "','" + x_entry.get() + "','" +
                       str(total_cost) + "','"+ odd1_entry.get() + "','" + odd2_entry.get() + "','" + even1_entry.get() + "','" + even2_entry.get() + "','" +
                       odd3_entry.get() + "','" + odd4_entry.get() + "','" + even3_entry.get() + "','" + even4_entry.get() + "')")
        cursor.execute("commit")
        tmsg.showinfo("Insert Status", "Inserted Successfully")
        con.close()




def reset():
    user_entry.delete(0,END)
    num_entry.delete(0,END)
    email_entry.delete(0,END)
    a_entry.delete(0,END)
    b_entry.delete(0, END)
    c_entry.delete(0, END)
    d_entry.delete(0, END)
    e_entry.delete(0, END)
    f_entry.delete(0, END)
    g_entry.delete(0, END)
    h_entry.delete(0, END)
    i_entry.delete(0, END)
    j_entry.delete(0, END)
    k_entry.delete(0, END)
    l_entry.delete(0, END)
    m_entry.delete(0, END)
    n_entry.delete(0, END)
    o_entry.delete(0, END)
    p_entry.delete(0, END)
    q_entry.delete(0, END)
    r_entry.delete(0, END)
    s_entry.delete(0, END)
    t_entry.delete(0, END)
    u_entry.delete(0, END)
    v_entry.delete(0, END)
    w_entry.delete(0, END)
    x_entry.delete(0, END)
    text.delete(1.0,END)
    tax1_entry.delete(0,END)
    tax2_entry.delete(0, END)
    tax3_entry.delete(0, END)
    tax4_entry.delete(0, END)
    tax5_entry.delete(0, END)

f=Frame(root,bd=5,width=1265,height=80,relief=RAISED)
Label(f,text="RESTAURANT BILLING SYSTEM",font=("calibri",24,"bold")).place(x=420,y=14)
f.place(x=0,y=0)

f1=Frame(root,bd=5,width=900,height=100,relief=RAISED)
Label(f1,text="CUSTOMER DETAILS",font=("lucida",10,"bold")).place(x=0,y=5)

username=Label(f1,text="Username",font=("lucida",10,"bold"))
username.place(x=10,y=40)
phone_num=Label(f1,text="Phone Number",font=("lucida",10,"bold"))
phone_num.place(x=270,y=40)
email=Label(f1,text="Email",font=("lucida",10,"bold"))
email.place(x=570,y=40)

user_entry=Entry(f1,font=("lucida",10,"bold"),width=22)
user_entry.place(x=100,y=40)
num_entry=Entry(f1,font=("lucida",10,"bold"),width=22)
num_entry.place(x=390,y=40)
email_entry=Entry(f1,font=("lucida",10,"bold"),width=22)
email_entry.place(x=630,y=40)

f1.place(x=0,y=83)

f2=Frame(root,bd=5,width=900,height=330,relief=RAISED)

Label(f2,text="Drinks",font=("lucida",15,"bold")).place(x=60,y=10)
a=Label(f2,text="Lassi",font=("lucida",10,"bold")).place(x=10,y=58)
b=Label(f2,text="Coffee",font=("lucida",10,"bold")).place(x=10,y=88)
c=Label(f2,text="Tea",font=("lucida",10,"bold")).place(x=10,y=118)
d=Label(f2,text="Badam Milk",font=("lucida",10,"bold")).place(x=10,y=148)
e=Label(f2,text="Cold Drink",font=("lucida",10,"bold")).place(x=10,y=178)
f=Label(f2,text="Shikanji",font=("lucida",10,"bold")).place(x=10,y=208)
odd1=Label(f2,text="Mocktails",font=("lucida",10,"bold")).place(x=10,y=238)
odd2=Label(f2,text="Water",font=("lucida",10,"bold")).place(x=10,y=268)

Label(f2,text="Cakes",font=("lucida",15,"bold")).place(x=280,y=10)
g=Label(f2,text="Chocolate",font=("lucida",10,"bold")).place(x=230,y=58)
h=Label(f2,text="Oreo",font=("lucida",10,"bold")).place(x=230,y=88)
i=Label(f2,text="Black Forest",font=("lucida",10,"bold")).place(x=230,y=118)
j=Label(f2,text="Pine Apple",font=("lucida",10,"bold")).place(x=230,y=148)
k=Label(f2,text="Brownie",font=("lucida",10,"bold")).place(x=230,y=178)
l=Label(f2,text="Vanila",font=("lucida",10,"bold")).place(x=230,y=208)
even1=Label(f2,text="Banana",font=("lucida",10,"bold")).place(x=230,y=238)
even2=Label(f2,text="Coffee",font=("lucida",10,"bold")).place(x=230,y=268)


Label(f2,text="South Indian",font=("lucida",15,"bold")).place(x=460,y=10)
m=Label(f2,text="Idli",font=("lucida",10,"bold")).place(x=450,y=58)
n=Label(f2,text="Dosa",font=("lucida",10,"bold")).place(x=450,y=88)
o=Label(f2,text="Sambhar",font=("lucida",10,"bold")).place(x=450,y=118)
p=Label(f2,text="Vada",font=("lucida",10,"bold")).place(x=450,y=148)
q=Label(f2,text="Appam",font=("lucida",10,"bold")).place(x=450,y=178)
r=Label(f2,text="Puttu",font=("lucida",10,"bold")).place(x=450,y=208)
odd3=Label(f2,text="Cuisines",font=("lucida",10,"bold")).place(x=450,y=238)
odd4=Label(f2,text="Pongal",font=("lucida",10,"bold")).place(x=450,y=268)

Label(f2,text="Food",font=("lucida",15,"bold")).place(x=720,y=10)
s=Label(f2,text="Chapati",font=("lucida",10,"bold")).place(x=670,y=58)
t=Label(f2,text="Daal",font=("lucida",10,"bold")).place(x=670,y=88)
u=Label(f2,text="Rice",font=("lucida",10,"bold")).place(x=670,y=118)
v=Label(f2,text="Paneer",font=("lucida",10,"bold")).place(x=670,y=148)
w=Label(f2,text="Biryani",font=("lucida",10,"bold")).place(x=670,y=178)
x=Label(f2,text="Veg Sabji",font=("lucida",10,"bold")).place(x=670,y=208)
even3=Label(f2,text="Soup",font=("lucida",10,"bold")).place(x=670,y=238)
even4=Label(f2,text="Cerels",font=("lucida",10,"bold")).place(x=670,y=268)



a_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
a_entry.place(x=100,y=58)
b_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
b_entry.place(x=100,y=88)
c_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
c_entry.place(x=100,y=118)
d_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
d_entry.place(x=100,y=148)
e_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
e_entry.place(x=100,y=178)
f_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
f_entry.place(x=100,y=208)
odd1_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
odd1_entry.place(x=100,y=238)
odd2_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
odd2_entry.place(x=100,y=268)

g_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
g_entry.place(x=320,y=58)
h_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
h_entry.place(x=320,y=88)
i_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
i_entry.place(x=320,y=118)
j_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
j_entry.place(x=320,y=148)
k_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
k_entry.place(x=320,y=178)
l_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
l_entry.place(x=320,y=208)
even1_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
even1_entry.place(x=320,y=238)
even2_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
even2_entry.place(x=320,y=268)

m_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
m_entry.place(x=540,y=58)
n_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
n_entry.place(x=540,y=88)
o_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
o_entry.place(x=540,y=118)
p_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
p_entry.place(x=540,y=148)
q_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
q_entry.place(x=540,y=178)
r_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
r_entry.place(x=540,y=208)
odd3_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
odd3_entry.place(x=540,y=238)
odd4_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
odd4_entry.place(x=540,y=268)


s_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
s_entry.place(x=760,y=58)
t_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
t_entry.place(x=760,y=88)
u_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
u_entry.place(x=760,y=118)
v_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
v_entry.place(x=760,y=148)
w_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
w_entry.place(x=760,y=178)
x_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
x_entry.place(x=760,y=208)
even3_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
even3_entry.place(x=760,y=238)
even4_entry=Entry(f2,font=("lucida",10,"bold"),width=10)
even4_entry.place(x=760,y=268)



f2.place(x=0,y=186)

f5=Frame(root,bd=5,relief=RAISED,width=900,height=115)
Label(f5,text="TAX DETAILS",font=("lucida",10,"bold")).place(x=0,y=5)
tax1=Label(f5,text="Tax on drinks",font=("lucida",10,"bold")).place(x=10,y=36)
tax2=Label(f5,text="Tax on Cakes",font=("lucida",10,"bold")).place(x=10,y=64)
tax3=Label(f5,text="Tax on South Indian Food",font=("lucida",10,"bold")).place(x=300,y=36)
tax4=Label(f5,text="Tax on Food",font=("lucida",10,"bold")).place(x=300,y=64)
tax5=Label(f5,text="Service Tax",font=("lucida",10,"bold")).place(x=650,y=36)

tax1_entry=Entry(f5,font=("lucida",10,"bold"),width=10)
tax1_entry.place(x=130,y=36)
tax2_entry=Entry(f5,font=("lucida",10,"bold"),width=10)
tax2_entry.place(x=130,y=64)
tax3_entry=Entry(f5,font=("lucida",10,"bold"),width=10)
tax3_entry.place(x=480,y=36)
tax4_entry=Entry(f5,font=("lucida",10,"bold"),width=10)
tax4_entry.place(x=480,y=64)
tax5_entry=Entry(f5,font=("lucida",10,"bold"),width=10)
tax5_entry.place(x=750,y=36)
f5.place(x=0,y=518)



f3=Frame(root,bd=5,relief=RAISED)
Label(f3,text="BILLING DETAILS",font=("lucida",10,"bold")).pack(pady=15)

scrol=Scrollbar(f3,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
text=Text(f3,font=("lucida",10,"bold"),yscrollcommand=scrol.set)
text.pack(fill=BOTH)
scrol.config(command=text.yview)
f3.place(x=900,y=83,width=366,height=470)



f4=Frame(root,bd=5,width=366,height=80,relief=RAISED)
Button(f4, text="Total", width=10, height=2 ,font=("lucida", 12),bd=5,command=total).place(x=7, y=7)
Button(f4, text="Reset", width=10, height=2,font=("lucida", 12),bd=5,command=reset).place(x=127, y=7)
Button(f4, text="Exit", width=10, height=2,font=("lucida", 12),bd=5,command=quit).place(x=247, y=7)
f4.place(x=900,y=553)


root.mainloop()