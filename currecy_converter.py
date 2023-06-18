from tkinter import *
import requests
from PIL import Image, ImageTk

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("800x600+250+50")
        self.resizable(0,0)
        self.title("Currency Convertor")
        Dollar = PhotoImage(file="My project.png")
        self.iconphoto(True,Dollar)
        self.configure(background="pink")
        Background = Image.open("My project.png")
        Background1 = Background.resize((800,600))
        self.Background2 = ImageTk.PhotoImage(Background1)

        my_canvas1 = Canvas(self, width=800, height=600)
        my_canvas1.pack(fill="both", expand=True)

        my_canvas1.create_image(0, 0, image=self.Background2, anchor="nw")

        my_canvas1.create_text(400,40,text="CurrencyConvertor",fill="white",font=("Helvetica",23,"bold"))
        my_canvas1.create_text(200,100,text="Amount :",fill="white",font=("Helvetica",15,"bold"))
        my_canvas1.create_text(200,200,text="From Currency :",fill="white",font=("Helvetica",15,"bold"))
        my_canvas1.create_text(200,300,text="To Currency :",fill="white",font=("Helvetica",15,"bold"))
        my_canvas1.create_text(200,400,text="Converted Amount:",fill="white",font=("Helvetica",15,"bold"))

        self.Amount =Entry(my_canvas1,justify=CENTER,font=("Helvetica",11,"bold"),highlightcolor="red",highlightbackground="green",highlightthickness=2)
        my_canvas1.create_window(600,100,window=self.Amount,height=34,width=200)

        CurrenyCode_list = ["INR","USD","CAD","CNY","DKK","EUR"]
        self.variable1 = StringVar(self)
        self.variable2 = StringVar(self)
        self.variable1.set("Currency")
        self.variable2.set("Currency")

        FromCurrency_option = OptionMenu(self, self.variable1, *CurrenyCode_list)
        ToCurrency_option = OptionMenu(self, self.variable2, *CurrenyCode_list)

        FromCurrency_option.configure(background="white",foreground="black")
        ToCurrency_option.configure(background="white",foreground="black")

        my_canvas1.create_window(600,200,window=FromCurrency_option)
        my_canvas1.create_window(600,300,window=ToCurrency_option)

        self.Cnt_Amount =Entry(my_canvas1,justify=CENTER,font=("Helvetica",11,"bold"),highlightcolor="red",highlightbackground="green",highlightthickness=2)

        my_canvas1.create_window(600,400,window=self.Cnt_Amount,height=34,width=200)

        Convert = Button(self,text="Convert",width=10,pady=5,font="bold",command=self.converted)
        my_canvas1.create_window(300,500,window=Convert)

        Clear = Button(self,text="Clear",width=10,pady=5,font="bold",command=self.clean)
        my_canvas1.create_window(500,500,window=Clear)

    def clean(self):
        self.Amount.delete(0,"end")
        self.Cnt_Amount.delete(0,"end")
    def converted(self):
        from_currency = self.variable1.get()
        to_currency = self.variable2.get()
        api_key = "XZPQNA6R5BF0SGUG"
        base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

        main_url = base_url + "&from_currency=" + from_currency + "&to_currency=" + to_currency +"&apikey=" + api_key
        req_object = requests.get(main_url)
        json_data = req_object.json()
        print(json_data)
        Exchange_rate = float(json_data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
        amount = float(self.Amount.get())
        new_amount = round(amount*Exchange_rate,3)
        self.Cnt_Amount.delete(0,"end")
        self.Cnt_Amount.insert(0,str(new_amount))
if __name__ == "__main__":
    root = GUI()
    root.mainloop()