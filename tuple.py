"""Practical Python tuple examples."""


# 1. A tuple stores related values that should not change.
user_record = (101, "Maya", "maya@example.com")

print("1. User record:")
print(user_record)
# Expected output:
# 1. User record:
# (101, 'Maya', 'maya@example.com')


# 2. Unpack a tuple into separate variables.
product = ("Keyboard", 1200, 5)
product_name, price, stock = product

print("\n2. Product details:")
print("Name:", product_name)
print("Price:", price)
print("Stock:", stock)
# Expected output:
# 2. Product details:
# Name: Keyboard
# Price: 1200
# Stock: 5


# 3. A tuple can represent a fixed GPS location.
office_location = (17.3850, 78.4867)
latitude, longitude = office_location

print("\n3. Office location:")
print("Latitude:", latitude)
print("Longitude:", longitude)
# Expected output:
# 3. Office location:
# Latitude: 17.385
# Longitude: 78.4867


# 4. Return multiple values from a function using a tuple.
def get_order_summary():
	return "ORDER-101", 3, 2499


order_id, item_count, total_amount = get_order_summary()

print("\n4. Order summary:")
print("Order ID:", order_id)
print("Items:", item_count)
print("Total:", total_amount)
# Expected output:
# 4. Order summary:
# Order ID: ORDER-101
# Items: 3
# Total: 2499


# 5. Use a tuple as a dictionary key for a grid coordinate.
warehouse_stock = {
	(1, 1): "Laptop",
	(1, 2): "Monitor",
	(2, 1): "Keyboard",
}

print("\n5. Warehouse item at position (1, 2):")
print(warehouse_stock[(1, 2)])
# Expected output:
# 5. Warehouse item at position (1, 2):
# Monitor


# 6. A list can change, but a tuple protects fixed configuration values.
supported_formats = ("json", "csv", "xml")

print("\n6. Supported file formats:")
for file_format in supported_formats:
	print(file_format)
# Expected output:
# 6. Supported file formats:
# json
# csv
# xml


# 7. AI development example: store fixed model metadata in tuples.
models = (
	("text-model-v1", "text", 8192),
	("vision-model-v2", "vision", 4096),
)

print("\n7. AI model metadata:")
for model_name, model_type, context_window in models:
	print(model_name, "|", model_type, "|", context_window, "tokens")
# Expected output:
# 7. AI model metadata:
# text-model-v1 | text | 8192 tokens
# vision-model-v2 | vision | 4096 tokens


# 8. AI development example: represent one prompt and its evaluation result.
evaluation_result = (
	"Summarize this document.",
	"The document explains Python tuples.",
	0.92,
)
prompt, response, score = evaluation_result

print("\n8. AI evaluation result:")
print("Prompt:", prompt)
print("Response:", response)
print("Score:", score)
# Expected output:
# 8. AI evaluation result:
# Prompt: Summarize this document.
# Response: The document explains Python tuples.
# Score: 0.92
