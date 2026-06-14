import hmac
import string 
def check_password_strength(password):
	if len(password) < 8:
		return "REJECTED: password is too short! It must be at least 8 characters."
	has_upper = any(char.isupper() for char in password)
	has_lower = any(char.islower() for char in password)
	has_digit = any(char.isdigit() for char in password)
	has_special = any(char in string.punctuation for char in password)
	if has_upper and has_lower and has_digit and has_special:
		return"STRONG: Excellent password!"
	else:
		return "WEAK: Missing uppercase, lowercase, number, or special character."

while True:
	user_password=input("Enter a password to test: ")
	result=check_password_strength(user_password)
	print(result)
	if "STRONG" in result:
		print("Access Granted. proceeding securely...")
		break
input("Press enter to close the program...")