import tkinter as tk
import requests
import json
HEIGHT=500
WIDTH=500

def func(entry,entry_1,entry_2,label_0,label_1):
	amount_entered=entry
	currency_code=entry_1
	convereted_code=entry_2
	url='https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={}&to_currency={}&apikey=AUFSF50DIXVQWX6X'.format(entry_1,entry_2)
	r=requests.get(url)
	data=json.loads(r.text)
	m=data['Realtime Currency Exchange Rate']["5. Exchange Rate"]
	m=float(m)
	final_amount=round(m*int(amount_entered),3)
	final_amount_1=round(m*1,3)
	label_0['text']=final_amount
	label_1['text']='1 {}={} {}'.format(currency_code,final_amount_1,convereted_code)


root=tk.Tk()
canvas=tk.Canvas(root,height=HEIGHT,width=WIDTH,bg='black',bd='10')
canvas.pack()

frame=tk.Frame(canvas,bg='#98F01A')
frame.place(x=12,y=12,height=500,width=500)


button=tk.Button(frame,text="CONVERT",command=lambda:func(entry.get(),entry_1.get(),entry_2.get(),label_0,label_1))
button.place(x=200,y=260,width=100,height=30)


label=tk.Label(frame,text='CURRENCY CONVERTER',font=('Courier',30),bg='#98F01A',fg='black')
label.place(x=40,y=100)



label_0=tk.Label(frame,font=('Courier',14))
label_0.place(x=280,y=200,width=165,height=27)

label_1=tk.Label(frame,font=('Courier',18),bg='#98F01A',fg='black')
label_1.place(x=60,y=300)

label_2=tk.Label(frame,text='Amount:',font=('Courier',15),bg='#98F01A',fg='black')
label_2.place(x=60,y=170)

label_3=tk.Label(frame,text='Converted:',font=('Courier',15),bg='#98F01A',fg='black')
label_3.place(x=276,y=170)

entry=tk.Entry(frame,font=('Courier',15))
entry.place(x=60,y=200,width=165,height=27)#To give Amount

entry_1=tk.Entry(frame,font=('Courier',15))#For Amount near the Label 
entry_1.place(x=150,y=170,height=28,width=50)

entry_2=tk.Entry(frame,font=('Courier',15))#For to be converted 
entry_2.place(x=400,y=170,height=28,width=45)
root.mainloop()
#relwidth=0.5,relheight=0.5,relx=0.25,rely=0.25