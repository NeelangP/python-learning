import customtkinter as ctk
import requests

def update_price():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']

        price_label.configure(text=f"${price:,}")

        print("Price updated")
    except Exception as e:
        price_label.configure(text="Error")
        print(e)

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('blue')

app = ctk.CTk()
app.geometry("500x300")
app.title("Crypto Tracker")

title_label = ctk.CTkLabel(app, text = "Bitcoin price tracker", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

price_label = ctk.CTkLabel(app, text="Press Refresh...", font=("Arial", 30), text_color="#00FF00")
price_label.pack(pady=20)

refresh_btn = ctk.CTkButton(app, text="Refresh Price", command=update_price)
refresh_btn.pack(pady=20)

app.mainloop()