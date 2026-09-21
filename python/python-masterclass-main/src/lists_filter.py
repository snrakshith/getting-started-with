orders = [
    {"order_id":1, "country":"US"},
    {"order_id":2, "country":"IN"},
    {"order_id":3, "country":"IN"},
]

in_order = []

for orders in orders:
    if orders["country"] == "IN":
        in_order.append(orders)

print(in_order)
