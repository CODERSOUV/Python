from tkinter import *
root1=Tk()
root1.geometry("600x200")
root1.title("First gui")
root2=Label(text='''Modern electronic calculators vary from cheap, give-away, \ncredit-card-sized models to sturdy desktop models with built-in printers. They \nbecame popular in the mid-1970s as the incorporation of integrated circuits \nreduced their size and cost. By the end of that decade, prices had dropped to \nthe point where a basic calculator was affordable to most and they became \ncommon in schools.''',bg="blue",fg="yellow",padx="23",pady="34",font=("comicsansms",16,"bold"),relief=SUNKEN
 )
root2.pack(side=LEFT,anchor="nw",fill=Y,padx=34,pady=45)
root1.mainloop()
# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE
