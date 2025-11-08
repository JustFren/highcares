def difficulty_assessment():

    difficulty = 0

    def ask_mc(prompt, options_map):
       
        while True:
            print(prompt)
            choice = input("Choose: ").strip()
            if choice in options_map:
                return options_map[choice]
            else:
                print("Invalid input — please enter one of the listed option numbers.\n")


    q1 = (
        "Do you have any health issues related to muscle pain or past injuries?\n"
        "1. Yes, serious\n"
        "2. Yes, minor\n"
        "3. No\n"
    )
    difficulty += ask_mc(q1, {"1": 0, "2": 5, "3": 15})


    q2 = (
        "How often do you train your legs and back?\n"
        "1. Regularly (at least twice a week)\n"
        "2. Often (once a week)\n"
        "3. Occasionally (irregularly)\n"
        "4. Never\n"
    )
    difficulty += ask_mc(q2, {"1": 15, "2": 10, "3": 5, "4": 0})


    q3 = (
        "How often do you practice any sport?\n"
        "1. Regularly (at least twice a week)\n"
        "2. Often (once a week)\n"
        "3. Occasionally (irregularly)\n"
        "4. Never\n"
    )
    difficulty += ask_mc(q3, {"1": 10, "2": 6, "3": 3, "4": 0})

 
    q4 = (
        "What type of job do you have?\n"
        "1. Sedentary job\n"
        "2. Physical job\n"
        "3. Mixed (part sitting, part physical)\n"
    )
    difficulty += ask_mc(q4, {"1": 0, "2": 4, "3": 2})

  
    while True:
        print("\nOn a scale from 0 (very poor) to 10 (very good), rate your physical condition.")
        val = input("Enter an integer 0–10: ").strip()
        try:
            n = int(val)
            if 0 <= n <= 10:
                difficulty += n
                break
            else:
                print("Value out of range — please enter an integer between 0 and 10.\n")
        except ValueError:
            print("Invalid input — please enter an integer between 0 and 10.\n")


    q6 = (
        "Do you own high-mountain climbing equipment?\n"
        "1. Yes\n"
        "2. No\n"
    )
    difficulty += ask_mc(q6, {"1": 30, "2": 0})


    q7 = (
        "Do you have any respiratory health issues?\n"
        "1. Yes, serious\n"
        "2. Yes, minor\n"
        "3. No\n"
    )
    difficulty += ask_mc(q7, {"1": 0, "2": 5, "3": 10})


    q8 = (
        "Do you have any mobility-related health issues?\n"
        "1. Yes, serious\n"
        "2. Yes, minor\n"
        "3. No\n"
    )
    difficulty += ask_mc(q8, {"1": 0, "2": 3, "3": 15})

 
    while True:
        print("\nOn a scale from 0 (no experience) to 20 (high experience), rate your mountain climbing experience.")
        val = input("Enter an integer 0–20: ").strip()
        try:
            n = int(val)
            if 0 <= n <= 20:
                difficulty += n
                break
            else:
                print("Value out of range — please enter an integer between 0 and 20.\n")
        except ValueError:
            print("Invalid input — please enter an integer between 0 and 20.\n")

 
    while True:
        print("\nOn a scale from 0 (very easy) to 20 (hardcore), rate how big of a challenge you want.")
        val = input("Enter an integer 0–20: ").strip()
        try:
            n = int(val)
            if 0 <= n <= 20:
                difficulty += n
                break
            else:
                print("Value out of range — please enter an integer between 0 and 20.\n")
        except ValueError:
            print("Invalid input — please enter an integer between 0 and 20.\n")


    q11 = (
        "Do you have any other physical activities planned on the same day as your mountain trip?\n"
        "1. Yes\n"
        "2. No\n"
    )
    difficulty += ask_mc(q11, {"1": 0, "2": 5})




    if 0 <= difficulty <= 39:
        category = "Easy"
    elif 40 <= difficulty <= 79:
        category = "Medium"
    elif 80 <= difficulty <= 119:
        category = "Hard"
    else:
        category = "Very Hard"

    print("Difficulty category:", category)
    return difficulty, category

difficulty_assessment()

