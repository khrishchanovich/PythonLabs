from container import Container

user = input('Enter your username: ')
storage = Container(user)

command = input('Enter the command: ')

if command == 'add':
    storage.add(elem)
elif command == 'remove':
    storage.remove(elem)
elif command == 'find':
