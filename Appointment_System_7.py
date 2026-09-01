appointments = []
next_id = 101

while True:
    print("=" * 11, "APPOINTMENT SYSTEM", "=" * 11)
    print("1. Book Appointment")
    print("2. View Appointments")
    print("3. Search Appointment")
    print("4. Cancel Appointment")
    print("5. Call Next Customer")
    print("6. Complete Appointment")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        customer = input("Enter customer name: ")
        phone = input("Enter phone number: ")
        service = input("Enter service: ")
        date = input("Enter date: ")
        time = input("Enter time: ")

        appointment = {
            "id": next_id,
            "customer": customer,
            "phone": phone,
            "service": service,
            "date": date,
            "time": time,
            "status": "Waiting"
        }

        appointments.append(appointment)

        print("Appointment booked successfully!")
        print("Appointment ID:", next_id)
        next_id += 1

    elif choice == "2":
        for appointment in appointments:
            print("Appointment ID:", appointment["id"])
            print("Customer:", appointment["customer"])
            print("Phone:", appointment["phone"])
            print("Service:", appointment["service"])
            print("Date:", appointment["date"])
            print("Time:", appointment["time"])
            print("Status:", appointment["status"])

    elif choice == "3":
        appointment_id = int(input("Enter appointment ID: "))

        for appointment in appointments:
            if appointment["id"] == appointment_id:
                print("Appointment ID:", appointment["id"])
                print("Customer:", appointment["customer"])
                print("Phone:", appointment["phone"])
                print("Service:", appointment["service"])
                print("Date:", appointment["date"])
                print("Time:", appointment["time"])
                print("Status:", appointment["status"])

    elif choice == "4":
        appointment_id = int(input("Enter appointment ID: "))

        for appointment in appointments:
            if appointment["id"] == appointment_id:
                appointment["status"] = "Cancelled"
                print("Appointment cancelled.")

    elif choice == "5":
        for appointment in appointments:
            if appointment["status"] == "Waiting":
                appointment["status"] = "In Progress"
                print("Now Serving:")
                print("Customer:", appointment["customer"])
                print("Service:", appointment["service"])
                break

    elif choice == "6":
        appointment_id = int(input("Enter appointment ID: "))

        for appointment in appointments:
            if appointment["id"] == appointment_id:
                appointment["status"] = "Completed"
                print("Appointment completed.")

    elif choice == "7":
        print("Thank you for using Appointment System!")
        break

    else:
        print("Invalid choice. Please try again.")
