"""Beginner examples for *args and **kwargs."""

# ---------------------------
# 1. Purpose: use *args when a function should accept any number of values.
def add_numbers(*args):
	total = 0

	for number in args:
		total += number

	return total


print("1. *args example:")
print(add_numbers(10, 20))
print(add_numbers(1, 2, 3, 4, 5))
# Expected output:
# 1. *args example:
# 30
# 15


# -----------------------------
# 2. Purpose: understand that *args stores positional values in a tuple.
def show_items(*items):
	print(items)


print("\n2. *args is a tuple:")
show_items("apple", "banana", "orange")
# Expected output:
# 2. *args is a tuple:
# ('apple', 'banana', 'orange')


# --------------------------------
# 3. Purpose: calculate a shopping bill when the number of products can vary.
def calculate_bill(*prices):
	return sum(prices)

print("\n3. Shopping bill with *args:")
print(calculate_bill(100, 250, 50))
# Expected output:
# 3. Shopping bill with *args:
# 400


# --------------------------
# 4. Purpose: use **kwargs when a function should accept named options.
def show_profile(**details):
	for key, value in details.items():
		print(key, ":", value)

print("\n4. **kwargs example:")
show_profile(name="Rahul", age=25, city="Hyderabad")
# Expected output:
# 4. **kwargs example:
# name : Rahul
# age : 25
# city : Hyderabad


# -------------------------------
# 5. Purpose: understand that **kwargs stores named values in a dictionary.
def show_settings(**settings):
	print(settings)

print("\n5. **kwargs is a dictionary:")
show_settings(theme="dark", notifications=True, language="English")
# Expected output:
# 5. **kwargs is a dictionary:
# {'theme': 'dark', 'notifications': True, 'language': 'English'}


# ------------------------------
# 6. Purpose: create a user from flexible named details.
def create_user(**user_details):
	print("New user:")

	for key, value in user_details.items():
		print(f"{key}: {value}")


print("\n6. Creating a user with **kwargs:")
create_user(username="srihas", email="srihas@example.com", role="admin")
# Expected output:
# 6. Creating a user with **kwargs:
# New user:
# username: srihas
# email: srihas@example.com
# role: admin


# -------------------------
# 7. Purpose: combine a required value, many items, and extra named options.
def order_summary(customer_name, *items, **order_details):
	print("Customer:", customer_name)
	print("Items:", items)
	print("Order details:", order_details)

print("\n7. Using all argument types together:")
order_summary(
	"Anu",
	"Laptop",
	"Mouse",
	"Keyboard",
	delivery="Express",
	payment="Card",
)
# Expected output:
# 7. Using all argument types together:
# Customer: Anu
# Items: ('Laptop', 'Mouse', 'Keyboard')
# Order details: {'delivery': 'Express', 'payment': 'Card'}


# -------------------------
# 8. Purpose: create a receipt for any number of purchased products.
def create_receipt(customer_name, *products, tax=0.05, **customer_details):
	print("\n8. Receipt for:", customer_name)
	print("Products:")

	subtotal = 0
	for product_name, price in products:
		print(f"- {product_name}: ${price:.2f}")
		subtotal += price

	tax_amount = subtotal * tax
	print(f"Subtotal: ${subtotal:.2f}")
	print(f"Tax: ${tax_amount:.2f}")
	print(f"Total: ${(subtotal + tax_amount):.2f}")
	print("Customer details:", customer_details)


create_receipt(
	"Maya",
	("Notebook", 5.50),
	("Pen", 1.25),
	("Backpack", 30.00),
	tax=0.05,
	email="maya@example.com",
	member=True,
)
# Expected output:
# 8. Receipt for: Maya
# Products:
# - Notebook: $5.50
# - Pen: $1.25
# - Backpack: $30.00
# Subtotal: $36.75
# Tax: $1.84
# Total: $38.59
# Customer details: {'email': 'maya@example.com', 'member': True}


# -------------------------
# 9. Purpose: build an API request with flexible query and header options.
def make_api_request(endpoint, *path_parts, **options):
	url = endpoint + "/" + "/".join(path_parts)
	method = options.get("method", "GET")
	params = options.get("params", {})
	headers = options.get("headers", {})

	print("\n9. API request:")
	print("Method:", method)
	print("URL:", url)
	print("Parameters:", params)
	print("Headers:", headers)


make_api_request(
	"https://api.example.com",
	"users",
	"42",
	method="GET",
	params={"include": "orders"},
	headers={"Authorization": "Bearer demo-token"},
)
# Expected output:
# 9. API request:
# Method: GET
# URL: https://api.example.com/users/42
# Parameters: {'include': 'orders'}
# Headers: {'Authorization': 'Bearer demo-token'}


# -------------------------
# 10. Purpose: send one notification to many users with optional settings.
def send_notification(message, *users, **settings):
	channel = settings.get("channel", "email")
	urgent = settings.get("urgent", False)

	for user in users:
		priority = "URGENT" if urgent else "Normal"
		print(f"\n10. Sending {priority} {channel} notification to {user}")
		print("Message:", message)


send_notification(
	"Your order has shipped.",
	"maya@example.com",
	"anu@example.com",
	channel="SMS",
	urgent=True,
)
# Expected output:
# 10. Sending URGENT SMS notification to maya@example.com
# Message: Your order has shipped.
# 10. Sending URGENT SMS notification to anu@example.com
# Message: Your order has shipped.


# -------------------------
# 11. AI development: build a prompt from many instruction parts.
def build_prompt(*instructions, **context):
	prompt = "\n".join(instructions)

	if context:
		prompt += "\nContext: " + str(context)

	return prompt


print("\n11. AI prompt builder:")
print(build_prompt(
	"Explain this Python code.",
	"Use beginner-friendly language.",
	language="Python",
	level="beginner",
))
# Expected output:
# 11. AI prompt builder:
# Explain this Python code.
# Use beginner-friendly language.
# Context: {'language': 'Python', 'level': 'beginner'}

# -------------------------
# 12. AI development: collect flexible model-generation settings.
def generate_response(prompt, **generation_settings):
	model = generation_settings.get("model", "demo-model")
	temperature = generation_settings.get("temperature", 0.7)
	max_tokens = generation_settings.get("max_tokens", 100)

	print("Model:", model)
	print("Prompt:", prompt)
	print("Temperature:", temperature)
	print("Maximum tokens:", max_tokens)


print("\n12. AI model settings:")
generate_response(
	"Summarize this document.",
	model="text-model-v1",
	temperature=0.2,
	max_tokens=200,
)
# Expected output:
# 12. AI model settings:
# Model: text-model-v1
# Prompt: Summarize this document.
# Temperature: 0.2
# Maximum tokens: 200


# -------------------------
# 13. AI development: evaluate several test cases with one reusable function.
def evaluate_model(model_name, *test_cases, **evaluation_options):
	metric = evaluation_options.get("metric", "accuracy")
	print("Model:", model_name)
	print("Metric:", metric)
	print("Test cases:", len(test_cases))

	for test_case in test_cases:
		print("Evaluating:", test_case)


print("\n13. AI model evaluation:")
evaluate_model(
		"text-model-v1",
		"summarization test",
		"question-answering test",
		metric="exact_match",
)
# Expected output:
# 13. AI model evaluation:
# Model: text-model-v1
# Metric: exact_match
# Test cases: 2
# Evaluating: summarization test
# Evaluating: question-answering test
