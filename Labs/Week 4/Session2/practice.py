email = "student@example.com"
# Extract the username from the email
username = email.split('@')[0]
# Extract the domain from the email
domain = email.split('@')[1].split('.')[0]
# Extract the extension from the email
extension = email.split('.')[-1]

# Print the results
print("Username:", username)
print("Domain:", domain)
print("Extension:", extension)