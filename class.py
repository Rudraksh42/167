from tkinter import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("600x600")
root.title("Canvas")

color_name = Label(root , text = "Color Name:")
color_name.place(relx = 0.6 , rely = 0.7)

insert_box = Entry(root)
insert_box.insert(0, "black")
insert_box.place(relx =  0.72 , rely = 0.9)

canvas_1 = Canvas(root , width = 530 , height = 530 , highlightbackground="grey")
canvas_1.pack()

height = width = 530
x1 = y1 = width/2

img = ImageTk.PhotoImage(Image.open("start_point1.png"))
image1 = canvas_1.create_image(20,20 , anchor = NW , image = img)

direction = ""
oldx = 50
oldy = 50   
newx = 50   
newy = 50
i_oldx = 20
i_oldy = 20   
i_newx = 20   
i_newy = 20

color = ""

def direction_right(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    
    oldx = newx
    oldy = newy
    newx = newx + 5
    direction = "right"
    
    draw(direction,oldx,oldy,newx,newy)
    canvas_1.move(image1, 5, 0)
    
def direction_left(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    
    oldx = newx
    oldy = newy
    newx = newx - 5
    direction = "left"
    draw(direction,oldx,oldy,newx,newy)
    
    global x1 , y1 
    
    canvas_1.move(image1, -5, 0)
    
def direction_down(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    
    oldx = newx
    oldy = newy
    newy = newy + 5
    direction = "down"
    draw(direction,oldx,oldy,newx,newy)
    canvas_1.move(image1, 0, 5)
    
    
   
    
def direction_up(event):
    global oldx
    global oldy
    global newx
    global newy
    global direction 
    
    oldx = newx
    oldy = newy
    newy = newy - 5
    direction = "up"
    draw(direction,oldx,oldy,newx,newy)
    canvas_1.move(image1, 0, -5)
    
    

   
    
def draw(direction,oldx,oldy,newx,newy):
    global color
    color = insert_box.get()
    
    if direction == "right":
        right_line = canvas_1.create_line(oldx,oldy,newx,newy , width = 3 , fill = color)
    if direction == "left":
        left_line = canvas_1.create_line(oldx,oldy,newx,newy , width = 3 , fill = color)
    if direction == "up":
        up_line = canvas_1.create_line(oldx,oldy,newx,newy , width = 3 , fill = color)
    if direction == "down":
        down_line = canvas_1.create_line(oldx,oldy,newx,newy , width = 3 , fill = color)
    
canvas_1.pack()
root.bind("<Right>" , direction_right)
root.bind("<Left>" , direction_left)
root.bind("<Up>" , direction_up)
root.bind("<Down>" , direction_down)
   
root.mainloop()