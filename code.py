# Python program to create a table 
   
from tkinter import *
import requests,threading,time
from bs4 import BeautifulSoup
  
class Table: 
      
    def __init__(self,root): 
        total_rows = len(lst) 
        total_columns = len(lst[0]) 
          
        # code for creating table 
        for i in range(total_rows): 
            for j in range(total_columns): 
                  
                self.e = Frame(root, width=20,bd=2,bg="black") 
                
                self.e.grid(row=i+5, column=j) 
                Label(self.e,text=lst[i][j],fg="red",width=20).pack(side=LEFT)
  
# take the data 
lst = [("stock name","price","volume","market cap")] 

def update():
    while True:
        
        for x in lst:
            try:
                url=f"https://finance.yahoo.com/quote/{x[0].upper()}"
                page=requests.get(url)
                soup = BeautifulSoup(page.content,"html.parser")
                stockprice=soup.find("span",class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
                stockdata1 = soup.find_all("tr")
                # print(stockdata1[6],stockdata1[8])
                stockvolume=stockdata1[6].find("td",class_="Ta(end) Fw(600) Lh(14px)").span.text
                stockmcap=stockdata1[8].find("td",class_="Ta(end) Fw(600) Lh(14px)").span.text
                stockprice = stockprice.text
                
                lst[lst.index(x)] = ((x[0].upper(),stockprice,stockvolume,stockmcap))
                # Button(root,text="delete",command = lambda : lst.remove(x)).grid(row = lst.index(x) + 5,column = len(lst[0])+1)
            except Exception as e:
                pass
            
            Table(root)
        
# find total number of rows and 
# columns in list 

   
# create root window
root = Tk() 
symbol = StringVar()
name = StringVar()
root.title("stock notifier")
Label(root,text="stock symbol:",fg="red").grid(row=0,column=0,padx=5,pady=3)
Entry(root,textvariable=symbol).grid(row=0,column=1,padx=5,pady=3)
Label(root,text="OR",fg="black").grid(row=0,column=2,padx=2)
Label(root,text="stock name:",fg="red").grid(row=0,column=3,padx=5,pady=3)
Entry(root,textvariable=name).grid(row=0,column=4)
def getinfo(x):
    url=f"https://finance.yahoo.com/quote/{x.upper()}"
    page=requests.get(url)
    soup = BeautifulSoup(page.content,"html.parser")
    stockprice=soup.find("span",class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    stockdata1 = soup.find_all("tr")
    stockvolume=stockdata1[6].find("td",class_="Ta(end) Fw(600) Lh(14px)").span.text
    stockmcap=stockdata1[8].find("td",class_="Ta(end) Fw(600) Lh(14px)").span.text
    stockprice = stockprice.text
    lst.append((x.upper(),stockprice,stockvolume,stockmcap))


def bruh():
    x = symbol.get()
    y=name.get()
    if x:
        getinfo(x)
    elif y:
        url = f"https://www.marketwatch.com/tools/quotes/lookup.asp?siteID=mktw&Lookup={y}&Country=all&Type=All"
        page=requests.get(url)
        soup = BeautifulSoup(page.content,"html.parser")
        a = soup.find_all("tr")
        bf=a[1].find("td").a.text
        getinfo(bf)
    Table(root)
        
        
Button(root,text="add to list of stocks",bg="blue",fg="white",command=bruh).grid(row=1,column=2)
threading.Thread(target=update).start()

root.mainloop() 