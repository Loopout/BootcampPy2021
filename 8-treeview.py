#8-treeview.py

from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from datetime import datetime
import csv

def WritetoCSV(ep):
	with open('treeview.csv','a',newline='',encoding='utf-8') as file:
		# 'a' = append (เพิ่มได้เรื่อยๆ) , 'w' = replace (ทับไฟล์เดิม)
		fw = csv.writer(file) # fw คือ file writer
		# ep = ['ไก่',300]
		fw.writerow(ep)

	print('Done!')


GUI = Tk() # นี่คือหน้าต่างหลักของโปรแกรม
#GUI.geometry('700x500') #ปรับขนาด
GUI.title('ตัวอย่าง')
########ปรับหน้าจอให้อยู่ตรงกลาง#########
w = 700
h = 500

ws = GUI.winfo_screenwidth()
hs = GUI.winfo_screenheight()
print(ws,hs)

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

GUI.geometry(f'{w}x{h}+{x:.0f}+{y:.0f}')




header = ['วัน-เวลา','รายการ','จำนวนเงิน']

table_expense = ttk.Treeview(GUI,column=header,show='headings',height=20)
table_expense.pack()

table_expense.heading('วัน-เวลา',text='วัน-เวลา')
table_expense.heading('รายการ',text='รายการ')
table_expense.heading('จำนวนเงิน',text='จำนวนเงิน')

def AddList(event=None):
	ep = simpledialog.askstring('กรอกข้อมูล','รายการที่ต้องการบันทึก',parent=GUI)
	price = simpledialog.askstring('กรอกข้อมูล','จำนวนเงิน',parent=GUI)
	dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S') #strftime.org
	data = [dt,ep,price] #ข้อมูลที่จะใส่
	print('DATA:',data)
	if ep != None and price != None and len(ep) != 0 and len(price) != 0:
		table_expense.insert('','end',value=data) #ใส่ค่าเข้าไปในตารางตามข้อมูลด้านบน
		WritetoCSV(data)
	elif ep != None and (price == None or len(price) == 0) and len(ep) != 0:
		data = [dt,ep,'-']
		table_expense.insert('','end',value=data)
		WritetoCSV(data)
	else:
		pass

# GUI.bind('<ชื่อปุ่ม>',ชื่อฟังชั่น) ต้องใส่ event=None ในฟังชั่นด้วย
GUI.bind('<F1>',AddList)

B1 = ttk.Button(GUI,text='เพิ่มรายการ',command=AddList)
B1.pack(pady=10, ipadx=20,ipady=10)

GUI.mainloop() # ทำให้โปรแกรมรันได้ตลอดเวลา
