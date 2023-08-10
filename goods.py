class Goods:
    def __init__(self, name, price, category, gst_rate):
        self.name = name
        self.price = price
        self.category = category
        self.gst_rate = gst_rate

    def calculate_gst(self):
        gst_amount = (self.price * self.gst_rate) / 100
        return gst_amount

    def display_info(self):
        print("Goods Name:", self.name)
        print("Price: $", self.price)
        print("Category:", self.category)
        print("GST Rate:", self.gst_rate, "%")
        print("GST Amount: $", self.calculate_gst())


# Example usage
if __name__ == "__main__":
    goods1 = Goods("Electronics", 1000, "Electronics", 18)
    goods2 = Goods("Clothing", 500, "Apparel", 12)

    print("Goods Information:")
    print("------------------")
    goods1.display_info()
    print("------------------")
    goods2.display_info()
