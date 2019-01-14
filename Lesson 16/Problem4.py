import time 

print('-'*65)
print('')

response = input('Please input the password!: ')

while response != 'Open Sesame':
	time.sleep(0.2)
	response = input('Please input the password!: ')


if response == 'Open Sesame':
	time.sleep(0.2)
	print('')
	print('Password is valid, welcome! ')

print('-'*65)