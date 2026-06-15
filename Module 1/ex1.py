class Product:
    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Category: {self.category}")

    def apply_discount(self, percent):
        discount = (self.price * percent) / 100
        self.price -= discount
        print(f"New price after 10% discount: ₹{self.price}")


class PhysicalProduct(Product):
    def __init__(self, name, price, category, weight_kg):
        super().__init__(name, price, category)
        self.weight_kg = weight_kg

    def get_info(self):
        super().get_info()
        print(f"Shipping Weight: {self.weight_kg} kg")

    def shipping_cost(self):
        return self.weight_kg * 50
    

class DigitalProduct(Product):
    def __init__(self, name, price, category, file_size_mb):
        super().__init__(name, price, category)
        self.file_size_mb = file_size_mb

    def get_info(self):
        super().get_info()
        print(f"File Size: {self.file_size_mb}")
        print("Delivery: Instant Download")

    def shipping_cost(self):
        return 0
    

def checkout(product):
    print("--- Checkout---")
    product.get_info()
    print(f"Shipping Cost: ₹{product.shipping_cost()}")


book = PhysicalProduct("Python Programming Book", 450.0, "Books", 0.8)
print("--- Product Info ---")
book.get_info()

book.apply_discount(10)

checkout(book)

course = DigitalProduct("Data Science Masterclass", 999.0, "Online Course", 1200)



print("\n--- Product Info---")
course.get_info()


checkout(course)