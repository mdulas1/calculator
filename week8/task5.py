# restaurant discount system
customer = {
        "name":"godiya",
        "order_amount":5000,
        "loyalty_card":True,
        "is_student":True
        }
customer_discount = 0
final_discount = 0
customer_free_item = None
if customer["order_amount"] > 20000:
    customer_discount += 5
    if customer["loyalty_card"]:
        customer_discount += 10
        if customer["is_student"]:
            customer_discount += 5
if not customer["is_student"]:
    free_item = "soft_drink"
print(customer_discount)
final_discount = customer["order_amount"] * (customer_discount /100)
print(final_discount)
print(customer)

