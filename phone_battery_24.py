class Phone:
    def __init__(self, battery):
        self.battery = battery

    def use_phone(self):
        self.battery -= 20
        print("You are using the phone 📱")
        print("Battery:", self.battery, "%")

        if self.battery <= 20:
            print("Low battery! 🔋")
            self.charge_phone()

    def charge_phone(self):
        self.battery = 100
        print("Charging the phone... 🔌")
        print("Battery:", self.battery, "%")


phone = Phone(100)

phone.use_phone()
phone.use_phone()
phone.use_phone()
phone.use_phone()
phone.use_phone()
