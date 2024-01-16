greet = input('What is your greetings? ').strip().lower()

if greet.startswith('hello'): 
    print('$0')
elif greet.startswith('h') and not greet.startswith('hello'):
    print('$20')
else: 
    print('$100')