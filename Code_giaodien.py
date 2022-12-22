#thưviện
from tkinter import *
from PIL import ImageTk, Image
import time
from tkinter import filedialog
from tkinter import ttk
import mysql.connector
from keras.utils import load_img
from keras.utils import img_to_array
from keras.models import load_model
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from functools import partial
import cv2
wd1=Tk()
wd1.geometry('500x400+540+260')
wd1.title('Traditional Instruments')
wd1.iconbitmap('icon.ico')#biểu tượng
wd1.resizable(False,False)
canvas_wd1 = Canvas(wd1, width=500, height=400)
bg_wd1 = ImageTk.PhotoImage(Image.open('bg1.jpg'))#ảnh nền
a=Label(wd1,font=('Arial',18), text='Traditional Instruments Detect',fg='red')
a.place(x= 80,y=120)
b=Label(wd1,font=('Arial',12), text="Click 'Next' to continue",fg='black')
b.place(x= 160,y=190)
canvas_wd1.create_image(0, 0, anchor=NW, image=bg_wd1)
canvas_wd1.pack()
def open_wd2():
 wd1.withdraw()#ẩn wd1
 wd2.deiconify()#mở wd2
button_next=Button(wd1,text='NEXT',command=open_wd2)
button_next.place(x=400, y=350)
#window2
wd2 = Toplevel(wd1)
wd2.title('Traditional Instruments')
wd2.iconbitmap('icon.ico')
wd2.geometry('728x455')
wd2.resizable(False, False)
wd2.withdraw()
canvas_wd2 = Canvas(wd2, width=728, height=455)
bg_wd2 = ImageTk.PhotoImage(Image.open('bg1.jpg'))
canvas_wd2.create_image(0, 0, anchor=NW,image=bg_wd2)
canvas_wd2.pack()
#frame test
frwd2=Frame(wd2,width=20, height=20)
frwd2.place(x=344,y=28)
bgfr2= ImageTk.PhotoImage(Image.open('bg2 (2).jpg'))#ảnh nền wd2
label_frame_wd2=Label(frwd2,image=bgfr2)
label_frame_wd2.pack()
file=0#biền đầu vào fake
def open_file():
 global bgfr2,file,solution
 name=filedialog.askopenfilename(initialdir='', title='Select A File',filetype=(('jpeg files','*.jpg'),('png files','.png'),('All','*.*')))#đọc nơi ở của file ảnh
 file=str(name)
 bgfr2=Image.open(file)#mở file ảnh
 nopen= bgfr2.resize((344,399), Image.Resampling.LANCZOS)
 showfile=ImageTk.PhotoImage(nopen)
 label_frame_wd2.configure(image=showfile)#chèn ảnh vào frame
 button_check.place(x=100,y=350)#có ảnh thì nút check xuất hiện
 solution.configure(text='')#khi chọn ảnh mói thì kết quả ảnh cũ biến mất
 mainloop()
button_choose=ttk.Button(wd2,text='Choose image',command=lambda :open_file())#chọn ảnh
button_choose.place(x=180,y=350)
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
model_h5=load_model('Musical.h5')#file h5
result=''
def check_img():
 global file,result,solution
 img = load_img(file, target_size=(150,150))
 plt.imshow(img)
 img = img_to_array(img)
 img = img.astype('float32')
 img = img / 255
 img = np.expand_dims(img, axis=0)
 result = model_h5.predict(img)
 class_name = ['Sáo trúc','Song loan',"Đàn T'rưng",'Đàn bầu', 'Đàn cò','Đàn nguyệt','Đàn sến','Đàn tranh','Đàn tỳ bà','Đàn đáy']
 result_check_leaf = int(np.argmax(result, axis=1))
 print("This is:", class_name[result_check_leaf])
 time.sleep(1)#đợi 1 giay in ra kết quả
 solution.configure(text='Result\nThis is: {}'.format(class_name[result_check_leaf]))
button_check=ttk.Button(wd2,text='Check',command=check_img)
button_check.place_forget()
#in ra ket qua tren tkinter
solution=Label(wd2,text=result,font=('Arial', 16))
solution.place(x=90,y=150)
wd1.mainloop()


