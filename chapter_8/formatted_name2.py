# Make the middle name optional. Initialize with a blank variable
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted"""
    if middle_name: # If middle name is not empty
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)