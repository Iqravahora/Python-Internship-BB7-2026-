subscribers = {"a@gmail.com", "b@gmail.com", "c@gmail.com"}
customers ={"b@gmail.com", "d@gmail.com"}

never_purchased = subscribers - customers
never_subscribed = customers - subscribers

print("Subscribed but never purchased:", never_purchased)
print("purchased but never subscribed:", never_subscribed)
