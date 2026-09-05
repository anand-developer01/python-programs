"""Practical lambda function examples."""

from functools import reduce

# ------------------------------
# 1. A lambda is a short function written in one line.
square = lambda number: number * number

print("1. Square:", square(6))
# Expected output:
# 1. Square: 36


# ------------------------------
# 2. Sort employees by salary without changing the original list.
employees = [
	{"name": "Maya", "salary": 72000},
	{"name": "Raman", "salary": 55000},
	{"name": "Anu", "salary": 85000},
]

employees_by_salary = sorted(employees, key=lambda employee: employee["salary"])

print("\n2. Employees sorted by salary:")
for employee in employees_by_salary:
	print(employee["name"], employee["salary"])
# Expected output:
# 2. Employees sorted by salary:
# Raman 55000
# Maya 72000
# Anu 85000


# ------------------------------
# 3. Filter completed orders from an order list.
orders = [
	{"id": 101, "status": "completed"},
	{"id": 102, "status": "pending"},
	{"id": 103, "status": "completed"},
]

completed_orders = list(filter(lambda order: order["status"] == "completed", orders))

print("\n3. Completed order IDs:")
print([order["id"] for order in completed_orders])
# Expected output:
# 3. Completed order IDs:
# [101, 103]


# ------------------------------
# 4. Apply a discount to every product price.
prices = [100, 250, 500]
discounted_prices = list(map(lambda price: price * 0.90, prices))

print("\n4. Prices after a 10% discount:")
print(discounted_prices)
# Expected output:
# 4. Prices after a 10% discount:
# [90.0, 225.0, 450.0]


# ------------------------------
# 5. Find the cheapest product using min() and a lambda key.
products = [
	{"name": "Keyboard", "price": 1200},
	{"name": "Mouse", "price": 700},
	{"name": "Monitor", "price": 9500},
]

cheapest_product = min(products, key=lambda product: product["price"])

print("\n5. Cheapest product:")
print(cheapest_product["name"], cheapest_product["price"])
# Expected output:
# 5. Cheapest product:
# Mouse 700


# ------------------------------
# 6. Convert API-like user data into display names.
users = [
	{"first_name": "Maya", "last_name": "Sharma"},
	{"first_name": "Raman", "last_name": "Kumar"},
]

display_names = list(
	map(lambda user: f"{user['first_name']} {user['last_name']}", users)
)

print("\n6. Display names:")
print(display_names)
# Expected output:
# 6. Display names:
# ['Maya Sharma', 'Raman Kumar']


# ------------------------------
# 7. AI development example: rank model responses by evaluation score.
responses = [
	{"model": "model-a", "score": 0.82},
	{"model": "model-b", "score": 0.94},
	{"model": "model-c", "score": 0.88},
]

ranked_responses = sorted(
	responses,
	key=lambda response: response["score"],
	reverse=True,
)

print("\n7. AI models ranked by score:")
for response in ranked_responses:
	print(response["model"], response["score"])
# Expected output:
# 7. AI models ranked by score:
# model-b 0.94
# model-c 0.88
# model-a 0.82


# ------------------------------
# 8. AI development example: keep only safe responses for review.
model_outputs = [
	{"text": "Answer accepted", "is_safe": True},
	{"text": "Needs review", "is_safe": False},
	{"text": "Answer accepted", "is_safe": True},
]

safe_outputs = list(filter(lambda output: output["is_safe"], model_outputs))

print("\n8. Safe AI responses:")
print([output["text"] for output in safe_outputs])
# Expected output:
# 8. Safe AI responses:
# ['Answer accepted', 'Answer accepted']


# ------------------------------
# 9. map() applies a lambda to every item and returns transformed values.
token_counts = [100, 250, 400]
estimated_costs_in_cents = list(map(lambda tokens: tokens * 2, token_counts))

print("\n9. Estimated AI request costs in cents:")
print(estimated_costs_in_cents)
# Expected output:
# 9. Estimated AI request costs in cents:
# [200, 500, 800]


# ------------------------------
# 10. reduce() combines all items into one final value.
request_costs_in_cents = [200, 500, 800]
total_cost_in_cents = reduce(
	lambda total, cost: total + cost,
	request_costs_in_cents,
	0,
)

print("\n10. Total AI request cost in cents:")
print(total_cost_in_cents)
# Expected output:
# 10. Total AI request cost in cents:
# 1500
