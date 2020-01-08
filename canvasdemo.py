from tkinter import *
from tkinter import font


root=Tk()

cv=Canvas(root,bg='white')

# rt1=cv.create_oval(10,10,110,110,tags=('r1','r2','r3'))
# rt2=cv.create_rectangle(20,20,80,80,tags=('s1','s2','s3'))
# line = cv.create_line(20,20,80,80)
text='hello'
text_font=font.Font(family='Helvetica',size=20,weight='bold',slant='italic')
cv.create_text(200,200,fill='red',font=text_font,text=text)
cv.pack()

root.mainloop()