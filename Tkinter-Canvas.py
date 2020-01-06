from tkinter import *

root=Tk()

cv=Canvas(root,bg='white')
rt=cv.create_rectangle(10,10,110,110,outline="red",tags='r1')
cv.pack()

print(cv.gettags(rt))
cv.itemconfig(rt,tags=('r2','r3','r4'))
print(cv.gettags(rt))

root.mainloop()
