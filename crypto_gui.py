import customtkinter as ctk
import requests

previous_price = 0 #global variable

def update_price():
    global previous_price
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        current_price = data['bitcoin']['usd']

        if current_price > previous_price:
            colour = "#00FF00"
            arrow = "▲"
        elif current_price < previous_price:
            colour = "#FF0000"
            arrow = "▼"
        else:
            colour = "#FFFFFF"
            arrow = "="
        
        price_label.configure(text=f"${arrow} ${current_price:,}", text_color = colour)
        previous_price = current_price
        print(f"Updated: ${current_price}")

    except Exception as e:
        price_label.configure(text="Error")
        print(e)
    app.after(10000, update_price)

#GUI Setup
ctk.set_appearance_mode('dark')
app = ctk.CTk()

app.title("BTC Tracker")
app.geometry("200x70")

app.attributes('-topmost', True)

price_label = ctk.CTkLabel(app, text="Loading....", font=("Arial", 32 , "bold"))
price_label.pack(pady=20)

update_price()
app.mainloop()