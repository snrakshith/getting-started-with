def calculate_total(order):
    if "amount" not in order:
        raise TypeError("Missing amount field")
    return order["amount"] * 2

order = {"amont": 100}
print(calculate_total(order))