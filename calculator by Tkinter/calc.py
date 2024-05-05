# %%
from tkinter import * 
from dataclasses import dataclass
import ast


root = Tk()

root.title("YAYA Calculator")

i=0

def get_num(num) :
    global i 
    display.insert(i,num)
    i+=1

def get_operation(operator) :
    global i 
    length = len(operator)
    display.insert(i,operator)
    i+=length


def clear_all() :
    display.delete(0,END)


def undo () : 
    entire_string =display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert (0 , new_string)
    else : 
        clear_all()
        display.insert(0,"")

def get_result ():
 try : 
        result = display.get()
        node = ast.parse(result,mode="eval")
        final_res= eval(compile(node,'<string>' ,'eval'))
        clear_all()
        display.insert(0,final_res)
 except Exception :
        clear_all()
        display.insert(0,"Mathmatical error")
        

      
    
    
display =Entry(root)
display.grid(row=1 ,columnspan=6 )


numbers=[1,2,3,4,5,6,7,8,9]
counter = 0
for x in  range (3) :
    for y in range (3) :
        button_text = numbers[counter]
        button = Button ( root , text=button_text ,width=3 ,height= 2, command= lambda text=button_text : get_num(text) )
        button.grid ( row =x+2 , column= y )
        counter +=1 

button = Button ( root , text="0" ,width=3 ,height= 2 ,command=lambda text=0 : get_num(text))
button.grid ( row = 5 ,column=1  )

count=0
operations = ['+' ,"-","*",'/',"*3.14",'%','(',')','**','**2']
for x in range (4) : 
    for y in range (3) :
        if count < len(operations) :
            button_text = operations[count]
            button = Button(root ,text=operations[count] , width=3 ,height=2 ,command= lambda text=button_text : get_operation(text))
            count +=1
            button.grid(row= x+2, column= y+3 )



Button(root ,text="AC" , width=3 ,height=2 ,command= clear_all).grid(row=5 , column= 0)
Button(root ,text="=" , width=3 ,height=2 ,command= get_result).grid(row=5 , column= 2)
Button(root ,text="DEL" , width=3 ,height=2 ,command= undo ).grid(row=5 , column=4)




root.geometry("250x200")

root.mainloop()



