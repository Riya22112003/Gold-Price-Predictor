import tkinter as ttk
import pandas as pd
model=pd.read_pickle('gld_price_prediction.pkl')

app=ttk.Tk()
app.geometry('500x300')
app.title('Gold Price Predictor')

# silver
ttk.Label(app,text='Enter SLV',padx=20,pady=10).grid(row=1,column=0)
silvervar=ttk.DoubleVar(app)
silvervar.set(0.0)
ttk.Spinbox(app,from_=0,to=48,textvariable=silvervar,width=10).grid(row=1,column=1)

# USO
ttk.Label(app,text='Enter USO',padx=20,pady=10).grid(row=2,column=0)
USOvar=ttk.DoubleVar(app)
USOvar.set(0.0)
ttk.Spinbox(app,from_=0,to=118,textvariable=USOvar,width=10).grid(row=2,column=1)

# spx
ttk.Label(app,text='Enter SPX',padx=20,pady=10).grid(row=3,column=0)
SPXvar=ttk.DoubleVar(app)
SPXvar.set(0.0)
ttk.Spinbox(app,from_=0,to=2900,textvariable=SPXvar,width=10).grid(row=3,column=1)

# currency
ttk.Label(app,text='Enter currency (EUR/USD)',padx=20,pady=10).grid(row=4,column=0)
currencyvar=ttk.DoubleVar(app)
currencyvar.set(0.0)
ttk.Spinbox(app,from_=0,to=2,textvariable=currencyvar,width=10).grid(row=4,column=1)

# prediction button 
def find_gld_price():
    global model
    values=[[silvervar.get()],[USOvar.get()],[SPXvar.get()],[currencyvar.get()]]
    cols=model.feature_names_in_
    query_df=pd.DataFrame(dict(zip(cols,values)))
    pred=round(model.predict(query_df)[0],1)
    resultVar.set(pred)

ttk.Button(app,text='Check',command=find_gld_price,padx=20,pady=2).grid(row=5,column=0,columnspan=2)
#result
resultVar=ttk.Variable(app)
resultVar.set(0.0)
ttk.Label(app,textvariable=resultVar,font=('Times New Roman',20)).grid(row=6,column=0,columnspan=2)


app.mainloop()