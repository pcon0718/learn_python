prompt = "\nEnter a pizza topping."
prompt += "\nType 'quit' to finish. "



while True:
    topping = input(prompt)
    
    if topping == 'quit':
        break
    else:
        print(f'You are adding {topping} to your pizza.')

    
