import tkinter as tk
import requests

root = tk.Tk()
root.title("Currency Converter")

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=0, column=0, padx=10, pady=10)

amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1, padx=10, pady=10)

input_currency_label = tk.Label(root, text="Input Currency:")
input_currency_label.grid(row=1, column=0, padx=10, pady=10)

input_currency_options = ["USD", "EUR", "GBP", "JPY", "CAD", "AED", "SAR", "QAR", "IRR"] 
input_currency_var = tk.StringVar(root)
input_currency_var.set(input_currency_options[0])

input_currency_dropdown = tk.OptionMenu(root, input_currency_var, *input_currency_options)
input_currency_dropdown.grid(row=1, column=1, padx=10, pady=10)

output_currency_label = tk.Label(root, text="Output Currency:")
output_currency_label.grid(row=2, column=0, padx=10, pady=10)

output_currency_options = ["USD", "EUR", "GBP", "JPY", "CAD", "AED", "SAR", "QAR", "IRR"] 
output_currency_var = tk.StringVar(root)
output_currency_var.set(output_currency_options[1])

output_currency_dropdown = tk.OptionMenu(root, output_currency_var, *output_currency_options)
output_currency_dropdown.grid(row=2, column=1, padx=10, pady=10)

def convert_currency():
    amount = float(amount_entry.get())
    from_currency = input_currency_var.get()
    to_currency = output_currency_var.get()

    api_key = "API_KEY"
    url = f"http://data.fixer.io/api/latest?access_key={api_key}&symbols={from_currency},{to_currency}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        rates = data["rates"]
        from_rate = rates[from_currency]
        to_rate = rates[to_currency]
        converted_amount = amount * (to_rate / from_rate)

        output_label.config(text=f"{amount:.2f} {from_currency} = {converted_amount:.2f} {to_currency}")
    else:
        output_label.config(text="Error: Could not retrieve exchange rate")

convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

output_label = tk.Label(root, text="")
output_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()