"""Understanding **kwargs in function definitions and calls."""
# `**kwargs` in a function definition collects named arguments into a dictionary.
# `**user` in a function call unpacks dictionary values into keyword arguments.
# Added an AI model configuration example using **model_settings.


# ------------------------------------
# 1. **kwargs in a function definition collects keyword arguments.
def show_user(**user_details):
	print(user_details)


show_user(name="Maya", role="developer", active=True)
# Expected output:
# {'name': 'Maya', 'role': 'developer', 'active': True}


# ------------------------------------
# 2. **dict in a function call unpacks a dictionary into keyword arguments.
def introduce_user(name, role, active):
	print(f"Name: {name}")
	print(f"Role: {role}")
	print(f"Active: {active}")


user = {
	"name": "Maya",
	"role": "developer",
	"active": True,
}

introduce_user(**user)
# Expected output:
# Name: Maya
# Role: developer
# Active: True


# ------------------------------------
# 3. AI development example: pass model settings from a dictionary.
def generate_text(prompt, model, temperature, max_tokens):
	print("Prompt:", prompt)
	print("Model:", model)
	print("Temperature:", temperature)
	print("Maximum tokens:", max_tokens)


model_settings = {
	"model": "text-model-v1",
	"temperature": 0.2,
	"max_tokens": 200,
}

generate_text("Summarize this document.", **model_settings)
# Expected output:
# Prompt: Summarize this document.
# Model: text-model-v1
# Temperature: 0.2
# Maximum tokens: 200
