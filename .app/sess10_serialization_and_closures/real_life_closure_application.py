# Python script to demonstrate the real life use/application of closures

# closure to calculate discount at a store
def discount_calculator(discount_percentage):
    def calculate(price):
        return price * (1 - discount_percentage/100) # or price - (price * discount_perc/100)
    return calculate

black_friday = discount_calculator(20)
christmas_sale = discount_calculator(30)

print(f"Normal price: Kes. 1000\nBlack Friday deal. Kes. {black_friday(1000)}")
print(f"Normal price: Kes. 1000\nChristmas deal. Kes. {christmas_sale(1000)}")

# Closure for an email template generator
def email_template(name):
    greetings = f"Dear {name},\n"
    def format_message(body):
        return f"{greetings}\n{body}\n\nBest Regards,\n\nEdulink International College Nairobi."
    return format_message

# Use the email template to notify students to collect their transcripts
student_result = email_template("Chris")
print(f"{student_result('Please come for your Data Science transcript.')}")
print("-"*42)

# Use the email template closure to request a supplier to deliver a product
supplier_reminder = email_template("Nextgen Computers")
print(f"{supplier_reminder("Please update us on the status of the 8 GB RAM modules you were to deliver.")}")

# inspect the above for __closure__
print(student_result.__closure__)
print(student_result.__closure__[0].cell_contents)
print(supplier_reminder.__closure__)
print(supplier_reminder.__closure__[0].cell_contents)
