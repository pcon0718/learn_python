guest_list = ['bono', 'edge', 'adam', 'larry']
noshow = "adam"
guest_list.remove(noshow)
guest_list.append('bootsy')
guest1 = guest_list.pop(0)
guest2 = guest_list.pop(0)
guest3 = guest_list.pop(0)
guest4 = guest_list.pop(0)
print(f"Unfortunately, {noshow.title()} could not make it.")
print(f"Hello {guest1.title()}. Welcome.")
print(f"Hello {guest2.title()}. Welcome.")
print(f"Hello {guest3.title()}. Welcome.")
print(f"Hello {guest4.title()}. Welcome.")
