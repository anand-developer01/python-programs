"""Practical Python iterator examples."""


# 1. iter() creates an iterator, and next() reads one item at a time.
colors = ["red", "green", "blue"]
color_iterator = iter(colors)

print("1. Reading items with next():")
print(next(color_iterator))
print(next(color_iterator))
print(next(color_iterator))
# Expected output:
# 1. Reading items with next():
# red
# green
# blue


# 2. A for loop automatically calls next() until the iterator is exhausted.
shopping_cart = iter(["Laptop", "Mouse", "Keyboard"])

print("\n2. Processing a shopping cart:")
for item in shopping_cart:
	print("Packing:", item)
# Expected output:
# 2. Processing a shopping cart:
# Packing: Laptop
# Packing: Mouse
# Packing: Keyboard


# 3. Use next(iterator, default) when the iterator may be empty.
support_tickets = iter(["TICKET-101"])

print("\n3. Reading support tickets safely:")
print(next(support_tickets, "No ticket available"))
print(next(support_tickets, "No ticket available"))
# Expected output:
# 3. Reading support tickets safely:
# TICKET-101
# No ticket available


# 4. Custom iterator: deliver orders one by one from a queue.
class DeliveryQueue:
	def __init__(self, orders):
		self.orders = orders
		self.position = 0

	def __iter__(self):
		return self

	def __next__(self):
		if self.position >= len(self.orders):
			raise StopIteration

		order = self.orders[self.position]
		self.position += 1
		return order


print("\n4. Processing a delivery queue:")
for order in DeliveryQueue(["ORDER-1", "ORDER-2", "ORDER-3"]):
	print("Delivering:", order)
# Expected output:
# 4. Processing a delivery queue:
# Delivering: ORDER-1
# Delivering: ORDER-2
# Delivering: ORDER-3


# 5. Real-time style example: process API pages one record at a time.
api_pages = [
	["user-101", "user-102"],
	["user-103", "user-104"],
]
user_iterator = iter(api_pages)

print("\n5. Processing paginated API data:")
while True:
	page = next(user_iterator, None)
	if page is None:
		break

	for user_id in page:
		print("Processing:", user_id)
# Expected output:
# 5. Processing paginated API data:
# Processing: user-101
# Processing: user-102
# Processing: user-103
# Processing: user-104


# 6. AI development example: stream model response chunks one at a time.
response_chunks = iter(["Python ", "iterators ", "save ", "memory."])

print("\n6. Streaming an AI response:")
complete_response = ""
for chunk in response_chunks:
	print("Received chunk:", repr(chunk))
	complete_response += chunk

print("Complete response:", complete_response)
# Expected output:
# 6. Streaming an AI response:
# Received chunk: 'Python '
# Received chunk: 'iterators '
# Received chunk: 'save '
# Received chunk: 'memory.'
# Complete response: Python iterators save memory.
