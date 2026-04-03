medical_cause = input("Do you have a medical cause for not taking the exam? (Y/N): ").strip().upper()

if medical_cause == "Y":
    print("You are allowed")
else:
    attendance = int(input("Enter the attendance of the student: "))

    if attendance >= 75:
        print("You are allowed")
    else:
        print("You are not allowed")