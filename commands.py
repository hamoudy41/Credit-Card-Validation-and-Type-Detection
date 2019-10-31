commands = {
'To Ban a card': 'python ban.py',
'To Remove Ban': 'python RemoveBan.py',
'To Enter credit card number': 'python User.py'
}

for command, action  in commands.items():
    print(command, ': ', action)