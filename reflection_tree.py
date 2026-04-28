def daily_reflection():
    print("--- Daily Reflection Tool ---")
    q1 = input("Did you finish your top priority? (yes/no): ").lower()
    
    if q1 == "yes":
        q2 = input("Was it due to (1) Planning or (2) High Energy? (1/2): ")
        if q2 == "1":
            print("Action: Duplicate this planning structure for tomorrow.")
        else:
            print("Action: Identify your energy peak and protect it.")
    else:
        q2 = input("Was the blocker (1) Internal or (2) External? (1/2): ")
        if q2 == "1":
            print("Action: Use a focus app to block distractions tomorrow.")
        else:
            print("Action: Re-prioritize your schedule with your lead.")

daily_reflection()
