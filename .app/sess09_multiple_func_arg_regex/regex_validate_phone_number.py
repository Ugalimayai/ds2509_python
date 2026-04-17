# Python script to validate a Kenyan phone number using regular expression(s): regex

# import the regex module
import re

# Function to validate the phone numbers
def validate_phone_number(phone_number):
    """
    Validates whether a given phone number is a valid Kenyan phone number.

    The phone number must:
    - Start with the country code '+254'
    - Optionally include spaces after the country code or carrier code
    - Include a valid 3-digit carrier code starting with digits 1 to 7
    - Be followed by 6 or 7 digits

    Parameters:
        phone_number (str): The phone number to validate. Should be in international format (+254...).

    Returns:
        None: Prints a message indicating whether the phone number is valid or not.

    Example:
        >>> validate_phone_number("+254712345678")
        The phone number +254712345678 is a valid Kenyan phone number.

        >>> validate_phone_number("0712345678")
        The phone number 0712345678 is not a valid Kenyan phone number.
    """
    pattern = r"^\+254\s?([1-7]\d\d)\s?(\d){6,7}"
    # +254 713 771220
    if not phone_number:
        print("Please enter your phone number.")
        return
    # compare the given phone number and the regex pattern and display an apt message
    if re.match(pattern, phone_number):
        print(f"The phone number {phone_number} is a valid Kenyan phone number.")
    else:
        print(f"The phone number {phone_number} is not a valid Kenyan phone number.")

# Run the application
if __name__ == "__main__":
    #prompt user for their phone number
    phone_number = input("Please enter your phone number for validation:\n")
    # Validate the user's phone number
    validate_phone_number(phone_number)
