import tkinter as tk
from tkinter import messagebox as m
from tkinter import simpledialog as sd
from collections import deque
import random
dire=((1,1),(1,-1),(1,0),(-1,1),(-1,-1),(-1,0),(0,1),(0,-1))
bb='\ud83d\udca3'
lvl={'EASY':10,'MEDIUM':15,'HARD':30,'EXIT':0}
def gen(n):
        base=[[0]*n for _ in range(n)]
        to=random.randrange(n*2-10,n*2)
        tot=to
        ans=[]
        while tot:
                a,b=random.randrange(n),random.randrange(n)
                if not base[a][b]:
                        base[a][b]=1
                        ans.append([a,b])
                        tot-=1
        return base,ans,to

def expand(x,y):
        global vic
        global num
        if base[x][y]:
                app.buttons[x][y].button['bg']='white'
                bomb(window)
        elif app.buttons[x][y].button['bg']!='white':
                arr=deque()
                arr.append([x,y])
                app.buttons[x][y].button['bg']='white'
                vic+=1
                while arr:
                        e,s=arr.popleft()
                        stop=0
                        count=0
                        for h,v in dire:
                                a,b=e+h,s+v
                                if a>-1 and b>-1 and a<n and b<n:
                                        if base[a][b]:
                                                count+=1
                                                stop=1              
                        if not stop: # no such bomb around
                                for h,v in dire:
                                        a,b=e+h,s+v
                                        if a>-1 and b>-1 and a<n and b<n and app.buttons[a][b].button['bg']!='white':
                                                app.buttons[a][b].button['bg']='white'
                                                vic+=1
                                                arr.append([a,b])
                                        
                        else:
                                app.buttons[e][s].change(str(count))
                if vic==n*n-num:
                        m.showinfo(bb*10, 'Congrats, all bombs been detected!')
class button:
        def __init__(self, master, w,h,i,j):
                self.text=tk.StringVar()
                self.button=tk.Button(master,textvariable=self.text,width=4,height=2,command=lambda i=i,j=j: expand(i,j))
        def change(self,txt):
                self.text.set(txt)

class buttons:
        def __init__(self, master, grid):
                frame=tk.Frame(master)
                self.grid=grid
                self.buttons=check
                for i in range(n):
                        for j in range(n):
                                self.buttons[i][j]=button(window,4,2,i,j)
                                self.buttons[i][j].button.grid(row=i+1,column=j)
def bomb(master):
        for x,y in bom:
                app.buttons[x][y].change('@')
        m.showinfo(bb*10, 'Bomb exploded!')
        master.destroy()

def lv(inp,window):
        global go
        go=inp
        window.destroy()
def con():
        global go
        window=tk.Tk()
        window.title(bb*2+' Minesweeper '+bb*2)
        window.geometry('200x120')
        lb=tk.Label(window,text='Click the level you want to play')
        lb.place(x=10,y=8)
        button1=tk.Button(window,text='EASY',command=lambda :lv('EASY',window))
        button1.place(x=20,y=40)
        button2=tk.Button(window,text='MEDIUM',command=lambda :lv('MEDIUM',window))
        button2.place(x=70,y=40)
        button3=tk.Button(window,text='HARD',command=lambda :lv('HARD',window))
        button3.place(x=140,y=40)
        button4=tk.Button(window,text='EXIT',command=lambda :lv('EXIT',window),bg='black', fg='white')
        button4.place(x=80,y=80)
        window.mainloop()
        return lvl[go]
go=1
while go:
        go=con()
        n=int(go)
        if not n:
                break
        vic=0
        check=[[0]*n for _ in range(n)]
        base, bom, num=gen(go)
        window=tk.Tk()
        window.title(bb*2+' Minesweeper '+bb*2)
        app=buttons(window, check)
        window.mainloop()

