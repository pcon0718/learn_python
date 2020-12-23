current_users = ["root", "pconway", "lmccoy", "nuhura", "jkirk"]
new_users = ["kjaneway", "jpicard", "jkirk", "bsisko"]

for new_user in new_users:
    if new_user in current_users:
        print("Please enter a different username!")
    else:
        print("Greetings! That username is available!")