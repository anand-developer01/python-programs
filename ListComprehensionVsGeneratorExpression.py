# 1. Reading User IDs from a Database
# ❌ List Comprehension
user_ids = [user.id for user in users]
# When to use:
# The database returns only 100 or 1000 users.
# You need random access:
print(user_ids[0])
print(user_ids[-1])

# ✅ Generator Expression
user_ids = (user.id for user in users)
for user_id in user_ids:
    send_email(user_id)

# Why?
# Imagine 10 million users.
# A list:
[user.id for user in users]

# stores all 10 million IDs in memory.
# A generator:
(user.id for user in users)
# generates one ID, sends the email, then moves to the next one.
# This saves a lot of memory.




# --------------------------------------------------
# 1. List Comprehension: Formatting UI/API Data
# -------------------------------------------
# Scenario: You are building a web app and just fetched a list of 50 user profiles from your database. You need to extract their email addresses, count how many there are, and display them on the screen.

# Why use []? You are dealing with a small, manageable dataset. More importantly, you need to use the data multiple times (to get the length, and to render the UI).

# Raw data from database
users = [
    {"name": "Alice", "email": " ALICE@example.com ", "active": True},
    {"name": "Bob", "email": "bob@example.com", "active": False},
    {"name": "Charlie", "email": " CHARLIE@test.com", "active": True}
]

# Eagerly build the list so we can use it multiple times
active_emails = [user["email"].strip().lower() for user in users if user["active"]]

# We can safely use len() and access the data repeatedly
print(f"Sending newsletter to {len(active_emails)} users.")
for email in active_emails:
    print(f"Queued: {email}")

# Output:
# Sending newsletter to 2 users.
# Queued: alice@example.com
# Queued: charlie@test.com

  # -----------------------------------------
#   2. Generator Expression: Parsing Massive Log Files
# ------------------------------------------
# Scenario: You are investigating a bug on your server. You need to scan a 50GB server log file to find if there are any "CRITICAL" errors, or to sum up the total number of errors.
# Why use ()? If you use a list comprehension here, Python will try to load all 50GB of text into your server's RAM at once, causing it to instantly crash. A generator expression safely streams the file one line at a time.
# Python

# Generator expression: reads one line, checks it, then throws it away
# Memory usage stays near 0MB, even for a 50GB file.
log_lines = open("server.log", "r")
critical_errors = (line for line in log_lines if "CRITICAL" in line)

# Using next() stops the moment it finds the FIRST match.
# It doesn't even bother reading the rest of the 50GB file!
first_critical_error = next(critical_errors, "No critical errors found.")

print(first_critical_error)
