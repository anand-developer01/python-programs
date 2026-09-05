"""Complete beginner-friendly examples of Python sets."""


# 1. A set stores unique values, so duplicates are removed automatically.
skills = {"Python", "SQL", "Python", "Git"}

print("1. Unique skills:")
print(skills)
# Expected output:
# 1. Unique skills:
# {'Python', 'SQL', 'Git'}
# Note: set order can be different when printed.


# 2. Convert a list to a set to remove duplicate values.
customer_emails = [
	"maya@example.com",
	"anu@example.com",
	"maya@example.com",
]
unique_emails = set(customer_emails)

print("\n2. Unique customer emails:")
print(sorted(unique_emails))
# Expected output:
# 2. Unique customer emails:
# ['anu@example.com', 'maya@example.com']


# 3. Add one item and several items to a set.
team_members = {"Maya", "Raman"}
team_members.add("Anu")
team_members.update(["John", "Sara"])

print("\n3. Team members:")
print(sorted(team_members))
# Expected output:
# 3. Team members:
# ['Anu', 'John', 'Maya', 'Raman', 'Sara']


# 4. remove() raises an error if the item does not exist.
# discard() safely does nothing when the item is missing.
active_users = {"maya", "raman", "anu"}
active_users.remove("raman")
active_users.discard("unknown_user")

print("\n4. Active users after updates:")
print(sorted(active_users))
# Expected output:
# 4. Active users after updates:
# ['anu', 'maya']


# 5. Union combines all values from two sets.
python_learners = {"Maya", "Anu", "Raman"}
java_learners = {"Raman", "John", "Sara"}
all_learners = python_learners | java_learners

print("\n5. Learners in either course:")
print(sorted(all_learners))
# Expected output:
# 5. Learners in either course:
# ['Anu', 'John', 'Maya', 'Raman', 'Sara']


# 6. Intersection finds values shared by both sets.
common_learners = python_learners & java_learners

print("\n6. Learners in both courses:")
print(sorted(common_learners))
# Expected output:
# 6. Learners in both courses:
# ['Raman']


# 7. Difference finds values present in the first set but not the second.
only_python_learners = python_learners - java_learners

print("\n7. Learners only in Python:")
print(sorted(only_python_learners))
# Expected output:
# 7. Learners only in Python:
# ['Anu', 'Maya']


# 8. Symmetric difference finds values that belong to only one set.
different_learners = python_learners ^ java_learners

print("\n8. Learners in only one course:")
print(sorted(different_learners))
# Expected output:
# 8. Learners in only one course:
# ['Anu', 'John', 'Maya', 'Sara']


# 9. Check whether a user has every required permission.
required_permissions = {"read", "write"}
user_permissions = {"read", "write", "delete"}
has_required_permissions = required_permissions.issubset(user_permissions)

print("\n9. User has required permissions:")
print(has_required_permissions)
# Expected output:
# 9. User has required permissions:
# True


# 10. A set is useful for checking membership quickly.
blocked_ips = {"192.168.1.10", "192.168.1.25"}
incoming_ip = "192.168.1.25"

print("\n10. Is the incoming IP blocked?")
print(incoming_ip in blocked_ips)
# Expected output:
# 10. Is the incoming IP blocked?
# True


# 11. A frozenset is an immutable set and can be used as a dictionary key.
role_permissions = {
	frozenset({"admin", "editor"}): "content management access",
}

print("\n11. Permission group description:")
print(role_permissions[frozenset({"admin", "editor"})])
# Expected output:
# 11. Permission group description:
# content management access


# 12. AI development example: find unique words in user prompts.
prompt = "python helps developers build AI applications with python"
unique_words = set(prompt.lower().split())

print("\n12. Unique words in the prompt:")
print(sorted(unique_words))
# Expected output:
# 12. Unique words in the prompt:
# ['ai', 'applications', 'build', 'developers', 'helps', 'with', 'python']


# 13. AI development example: compare words in two documents.
document_a_words = {"python", "code", "data", "model"}
document_b_words = {"python", "data", "api", "model"}
shared_words = document_a_words & document_b_words

print("\n13. Words shared by both documents:")
print(sorted(shared_words))
# Expected output:
# 13. Words shared by both documents:
# ['data', 'model', 'python']
