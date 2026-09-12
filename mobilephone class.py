class MobilePhone:
    def __init__(self, model, battery):
        self.model = model
        self.battery = battery

    def use_phone(self):
        self.battery = self.battery - 5

phone = MobilePhone("Samsung s23", 100)

phone.use_phone()

print(phone.model)
print(phone.battery)
