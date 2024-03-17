import tkinter as tk
import customtkinter
from forex_python.converter import CurrencyRates
import matplotlib.pyplot as plt

root = customtkinter.CTk()
root.config(bg='#202630')
root.geometry('500x500')
root.title("Currency Converter")

variable1 = tk.StringVar()
variable2 = tk.StringVar()
text = tk.StringVar()

image_path = "C:\\Users\\ASUS\\Downloads\\510217-PILGX1-825-ai.png"
image = tk.PhotoImage(file=image_path)
image_label = tk.Label(root, image=image, bg='#202630')
image_label.image = image
image_label.place(relx=0.5, y=120, anchor=tk.CENTER)

def convert():
    from_currency = variable1.get()
    to_currency = variable2.get()
    try:
        amount = float(amount_entry.get())
        c = CurrencyRates()
        amt = c.convert(from_currency, to_currency, amount)
        result = "{:.3f}".format(amt)
        text.set(result)
    except ValueError:
        text.set("Invalid input")

def show_currency_chart():
    currency_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP"]
    c = CurrencyRates()
    
    chart_text = "Currency Exchange Rates:\n\n"
    for currency in currency_list:
        rate = round(c.get_rate("USD", currency), 5)
        chart_text += f"{currency}: {rate}\n"
    
    chart_window = tk.Toplevel()
    chart_window.config(bg='#202630')
    chart_window.geometry('300x300')
    chart_window.title("Currency Chart")
    
    chart_label = customtkinter.CTkLabel(chart_window, text=chart_text, font=('Arial', 12),fg_color="#FFFFFF", text_color="#000000")
    chart_label.pack(padx=20, pady=20)


def reset():
    variable1.set("")
    variable2.set("")
    text.set("")
    amount_entry.delete(0, tk.END)

fromLabel = customtkinter.CTkLabel(root, text='From', font=('Arial', 13, 'bold'), fg_color='#202630', text_color='#FFFFFF', width=1)
fromLabel.place(x=60, y=150)

toLabel = customtkinter.CTkLabel(root, text='To', font=('Arial', 13, 'bold'), fg_color='#202630', text_color='#FFFFFF', width=1)
toLabel.place(x=360, y=150)

currencyList = ["INR", "USD", "CAD", "CNY", "DKK", "EUR", "GBP"]

FromMenu = customtkinter.CTkComboBox(root, variable=variable1, values=currencyList, font=('Arial', 12, 'bold'), fg_color='#FFFFFF', text_color="#000000", button_color="#0074D9", button_hover_color='#001f4d', border_color="#FFFFFF", dropdown_hover_color="#ADD8E6", dropdown_text_color="#000000",dropdown_fg_color="#FFFFFF")
FromMenu.place(x=60,y=180)
ToMenu = customtkinter.CTkComboBox(root, variable=variable2, values=currencyList, font=('Arial', 12, 'bold'), fg_color='#FFFFFF', text_color="#000000", button_color="#0074D9", button_hover_color='#001f4d', border_color="#FFFFFF", dropdown_hover_color="#ADD8E6", dropdown_text_color="#000000",dropdown_fg_color="#FFFFFF")
ToMenu.place(x=290, y=180)

amount_entry = customtkinter.CTkEntry(root, font=('Arial',20,'bold'), text_color="#000000", width=370,fg_color="#FFFFFF",border_color="#FFFFFF")
amount_entry.place(x=60, y=230)

convert_btn = customtkinter.CTkButton(root, text="Convert", font=('Arial',20,'bold'),text_color='#FFFFFF', fg_color='#0074D9', hover_color='#ADD8E6', command=convert)
convert_btn.place(x=100,y=300)

reset_btn = customtkinter.CTkButton(root, text="Reset", font=('Arial',20,'bold'),text_color='#FFFFFF', fg_color='#0074D9', hover_color='#ADD8E6', command=reset)
reset_btn.place(x=250,y=300)

chart_btn = customtkinter.CTkButton(root, text="Currency Chart", font=('Arial', 12, 'bold'),text_color='#FFFFFF', fg_color='#0074D9', hover_color='#ADD8E6',command=show_currency_chart)
chart_btn.place(x=180, y=390)

result_label = customtkinter.CTkButton(root, textvariable=text, font=('Arial',20,'bold'),fg_color="#FFFFFF",text_color="#0074D9")
result_label.place(x=180, y=350)

root.mainloop()
