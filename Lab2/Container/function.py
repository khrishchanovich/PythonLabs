from container import Container


def user_input():
    command_input = input('Enter the command: ').split(maxsplit=1)
    command = command_input[0]
    elements = str()

    if len(command_input) > 1:
        elements = command_input[1]

    return command, elements


def current_command(command, elements, storage: Container):
    if command == 'add':
        element = elements.split()
        for i in element:
            storage.add(i)
    elif command == 'remove':
        storage.remove(elements)
    elif command == 'find':
        pass
    elif command == 'list':
        print(storage.list())
    elif command == 'grep':
        pass
    elif command == 'save':
        pass
    elif command == 'load':
        pass
    elif command == 'switch':
        pass
    else:
        print(f'There is no such command: {command}')
