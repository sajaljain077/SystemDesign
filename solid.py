from abc import ABC, abstractmethod

# TODO: in the starting 
# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total
#     def pay(self, payment_type, security_code):
#         if payment_type == "debit":
#             print("Processing debit payment type")
#             print(f"Verifying security code: {security_code}")
#             self.status = "paid"
#         elif payment_type == "credit":
#             print("Processing credit payment type")
#             print(f"Verifying security code: {security_code}")
#             self.status = "paid"
#         else:
#             raise Exception(f"Unknown payment type: {payment_type}")

# order = Order()

# order.add_item()



# This is after Single responsibility 
# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):

#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class PaymentProcessor:

#     def pay_debit(self, order, security_code):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
#     def pay_credit(self, order, security_code):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"


# This is after open and close principle
# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):

#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order, security_code):
#         print(security_code)
#         pass
# class DebitPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
# class CreditPaymentProcessor(PaymentProcessor):
#     def pay(self, order, security_code):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {security_code}")
#         order.status = "paid"
# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# print(order.total_price())
# processor = CreditPaymentProcessor()
# processor.not_pay(order, "0372846")




# this is after liskov principal


# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):

#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)

#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass
# class DebitPaymentProcessor(PaymentProcessor):

#     def __init__(self, security_code):
#         self.security_code = security_code
#     def pay(self, order):
#         print("Processing debit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"

# class CreditPaymentProcessor(PaymentProcessor):

#     def __init__(self, security_code):
#         self.security_code = security_code
#     def pay(self, order):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"

# class PaypalPaymentProcessor(PaymentProcessor):
#     def __init__(self, email):
#         self.email = email
#     def pay(self, order):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {self.email}")
#         order.status = "paid"


# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# print(order.total_price())
# processor = PaypalPaymentProcessor("hi@arjancodes.com")
# processor.pay(order)




# # This is after Interface segrigation, using class, subclasses
# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass


# class PaymentProcessor_SMS(PaymentProcessor):
#     @abstractmethod
#     def auth_sms(self, code):
#         pass


# class DebitPaymentProcessor(PaymentProcessor_SMS):
#     def __init__(self, security_code):
#         self.security_code = security_code
#         self.verified = False
#     def auth_sms(self, code):
#         print(f"Verifying SMS code {code}")
#         self.verified = True
    
#     def pay(self, order):
#         if not self.verified:
#             raise Exception("Not authorized")
#         print("Processing debit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code
#     def pay(self, order):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"


# class PaypalPaymentProcessor(PaymentProcessor_SMS):
#     def __init__(self, email_address):
#         self.email_address = email_address
#         self.verified = False
#     def auth_sms(self, code):
#         print(f"Verifying SMS code {code}")
#         self.verified = True
#     def pay(self, order):
#         if not self.verified:
#             raise Exception("Not authorized")
#         print("Processing paypal payment type")
#         print(f"Using email address: {self.email_address}")
#         order.status = "paid"




# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# print(order.total_price())
# processor = PaypalPaymentProcessor("hi@arjancodes.com")
# processor.auth_sms(465839)
# processor.pay(order)

# This is after Interface segrigation, using composition
# class Order:
#     def __init__(self):
#         self.items = []
#         self.quantities = []
#         self.prices = []
#         self.status = "open"

#     def add_item(self, name, quantity, price):
#         self.items.append(name)
#         self.quantities.append(quantity)
#         self.prices.append(price)
#     def total_price(self):
#         total = 0
#         for i in range(len(self.prices)):
#             total += self.quantities[i] * self.prices[i]
#         return total


# class PaymentProcessor(ABC):
#     @abstractmethod
#     def pay(self, order):
#         pass


# class SMSAuth:
#     authorized = False
#     def verify_code(self, code):
#         print(f"verifying code {code}")
#         self.authorized = True

#     def is_authorized(self)->bool:
#         return self.authorized


# class DebitPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code, authorizer:SMSAuth):
#         self.security_code = security_code
#         self.authorizer = authorizer
    
#     def pay(self, order):
#         if not self.authorizer.is_authorized:
#             raise Exception("Not authorized")
#         print("Processing debit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"


# class CreditPaymentProcessor(PaymentProcessor):
#     def __init__(self, security_code):
#         self.security_code = security_code
#     def pay(self, order):
#         print("Processing credit payment type")
#         print(f"Verifying security code: {self.security_code}")
#         order.status = "paid"


# class PaypalPaymentProcessor(PaymentProcessor):
#     def __init__(self, email_address, authorizer:SMSAuth):
#         self.authorizer = authorizer
#         self.email_address = email_address

#     def pay(self, order):
#         if not self.authorizer.is_authorized:
#             raise Exception("Not authorized")
#         print("Processing paypal payment type")
#         print(f"Using email address: {self.email_address}")
#         order.status = "paid"




# order = Order()
# order.add_item("Keyboard", 1, 50)
# order.add_item("SSD", 1, 150)
# order.add_item("USB cable", 2, 5)
# print(order.total_price())
# authorizer = SMSAuth()
# authorizer.verify_code(465839)
# processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
# processor.pay(order)


# this is after dependecy Inversion
class Order:
    def __init__(self):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)
    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total


class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, order):
        pass


class Authorizer(ABC):

    @abstractmethod
    def is_authorized(self)->bool:
        return self.authorized

class SMSAuth(Authorizer):
    def __init__(self):
        self.authorized = False

    def verify_code(self, code):
        print(f"verifying code {code}")
        self.authorized = True

    def is_authorized(self)->bool:
        return self.authorized


class RobotAuth(Authorizer):
    def __init__(self):
        self.authorized = False

    def is_robot(self):
        self.authorized = False
        print("Are you robot.... Naaaaaa")


    def is_authorized(self)->bool:
        return self.authorized

class DebitPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code, authorizer:Authorizer):
        self.security_code = security_code
        self.authorizer = authorizer
    
    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class CreditPaymentProcessor(PaymentProcessor):
    def __init__(self, security_code):
        self.security_code = security_code
    def pay(self, order):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        order.status = "paid"


class PaypalPaymentProcessor(PaymentProcessor):
    def __init__(self, email_address, authorizer:Authorizer):
        self.authorizer = authorizer
        self.email_address = email_address

    def pay(self, order):
        if not self.authorizer.is_authorized():
            raise Exception("Not authorized")
        print("Processing paypal payment type")
        print(f"Using email address: {self.email_address}")
        order.status = "paid"




order = Order()
order.add_item("Keyboard", 1, 50)
order.add_item("SSD", 1, 150)
order.add_item("USB cable", 2, 5)
print(order.total_price())
authorizer = RobotAuth()
authorizer.is_robot()
processor = PaypalPaymentProcessor("hi@arjancodes.com", authorizer)
processor.pay(order)