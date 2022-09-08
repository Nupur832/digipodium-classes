email = input("Enter ur email=> ")

if '@' in email and len(email) >= 11 and ('.com' in email or 'org' in email):
    print('badhiya email hai')
else:
    print('ye email to nhi lag rha')