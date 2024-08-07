import requests
def currency_rates(amount):
    """Fetches latest currency rates and converts rates of different membership types to USD."""
    url = "https://v6.exchangerate-api.com/v6/1e8b8139dd8298f0c8c6ec48/latest/USD"
    response = requests.get(url)
    data = response.json()
    conversion_rates = data["conversion_rates"]
    npr = conversion_rates["NPR"]
    membership_usd_rate = round(amount / npr, 2)
    return membership_usd_rate