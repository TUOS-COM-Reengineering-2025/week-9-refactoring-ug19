class CustomerManager:
    def __init__(self):
        self.customers = {}
        self.tax_rate = 0.2
        self.tax_threshold = 100
        self.discount_threshold = 500

    def add_customer(self, name, purchases):
        if name in self.customers.keys():
            self.customers[name].extend(purchases)
        else:
            self.customers[name] = purchases

    def add_purchase(self, name, purchase):
        self.add_customer(name, [purchase])

  #  def add_purchases(self, name, purchases):
   #     self.add_customer(name, purchases)

    def generate_report(self):
        for y, x in self.customers.items():
            total_price = 0
            for z in x:
                if z['price'] > self.tax_threshold:
                    taxed_price = z['price'] * (1 + self.tax_rate)
                    total_price += taxed_price
                else:
                    total_price += z['price']
            print(y)
            if total_price > self.discount_threshold:
                print("Eligible for discount")
            else:
                if total_price > 300:
                    print("Potential future discount customer")
                else:
                    print("No discount")
            if total_price > 1000:
                print("VIP Customer!")
            else:
                if total_price > 800:
                    print("Priority Customer")

    def calculate_shipping_fee(self, purchases):
        for purchase in purchases:
            if purchase.get('weight', 0) > 20:
                return 50
        return 20

# def calculate_shipping_fee_for_heavy_items(purchases):
#     for purchase in purchases:
#         if purchase.get('weight', 0) > 20:
#             return 50
#     return 20

def calculate_shipping_fee_for_fragile_items(purchases):
    for purchase in purchases:
        if purchase.get('fragile', False):
            return 60
    return 25