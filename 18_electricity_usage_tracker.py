class ElectricityUsage:
    def __init__(self, name, cost_per_unit):
        self.name = name
        self.cost_per_unit = cost_per_unit
        self.units = []

    def add_usage(self, unit):
        self.units.append(unit)

    def calculate_total(self):
        return sum(self.units)

    def calculate_average(self):
        return self.calculate_total() / len(self.units)

    def calculate_bill(self):
        return self.calculate_total() * self.cost_per_unit

    def check_usage(self):
        if self.calculate_average() > 6:
            return "⚠️ High electricity usage!"
        else:
            return "✅ Usage is normal."

    def show_report(self):
        total = self.calculate_total()
        average = self.calculate_average()
        bill = self.calculate_bill()

        print("\n📊 ELECTRICITY REPORT")
        print("=" * 30)
        print("Consumer     :", self.name)
        print("Total Units  :", total)
        print("Average/Day  :", round(average, 2))
        print("Estimated Bill : ₹", bill)
        print(self.check_usage())


# User Input
print("="*45)
print("       ⚡ ELECTRICITY USAGE")
print("       TRACKER")
print("=" * 45)

name = input("Enter consumer name: ")
days = int(input("Enter number of days: "))
cost = float(input("Enter cost per unit: "))

usage = ElectricityUsage(name, cost)

for day in range(1, days + 1):
    unit = float(input(f"Day {day} units: "))
    usage.add_usage(unit)

usage.show_report()
