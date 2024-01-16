extension = input('What is your file name? ').strip().lower()

if extension.endswith('.gif'):
    print('image/gif')
elif extension.endswith('.jpg'):
    print('image/jpeg')
elif extension.endswith('.jpeg'):
    print('image/jpeg')
elif extension.endswith('.png'):
    print('image/png')
elif extension.endswith('.pdf'):
   print('application/pdf') 
elif extension.endswith('.txt'):
    print('text/plain')
elif extension.endswith('.zip'):
    print('application/zip')
else:
    print('can not identify the MIME type of your file')
