# Currency Converter Project

This Currency Converter project is a Python-based application that allows users to convert between different currencies. Whether you're a traveler, a business owner dealing with international transactions, or simply curious about currency exchange rates, this project provides a simple yet effective solution.

## Features

- **Currency Conversion:** Convert between various currencies accurately.
- **Real-Time Exchange Rates:** Utilizes real-time exchange rate data to ensure accuracy and reliability.
- **User-Friendly GUI:** Intuitive graphical user interface for ease of use.

## Requirements

- Python 3.x
- Dependencies (Refer to `requirements.txt`)

## Installation

1. Clone the repository to your local machine:
   
   git clone https://github.com/siddhi-awari/currency-converter.git

Usage
Run the application:
python currency_converter.py
Follow the on-screen instructions to convert currencies:
Input the amount to convert.
Select the source currency.
Select the target currency.
View the converted amount.

Usage Example
python
from currency_converter import CurrencyConverter
# Create a CurrencyConverter object
converter = CurrencyConverter()

# Convert 100 USD to EUR
amount_usd = 100
amount_eur = converter.convert(amount_usd, 'USD', 'EUR')

print(f"{amount_usd} USD is equal to {amount_eur} EUR")
Troubleshooting
If users encounter any common issues or errors while using your application, you can provide troubleshooting tips or solutions here.

Limitations
As the currency rates are integrated using api, updates may take time.

Contact Information
For any inquiries or support, please contact Siddhi Awari at siddhi.awari@gmail.com.
