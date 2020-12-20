guest_list = ['bono', 'edge', 'adam', 'larry']
byeguest1 = guest_list.pop(2)
byeguest2 = guest_list.pop(2)
print(f"We ran out of room. Goodbye {byeguest1.title()} and {byeguest2.title()}.")
print(f"Welcome to the resturaunt {guest_list[0].title()}.")
print(f"Welcome to the resturaunt {guest_list[1].title()}.")
