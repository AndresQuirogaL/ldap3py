import sys
from ldap3 import Server, Connection, ALL, core

arguments = sys.argv

# Delete first argument (script name)
del arguments[0]

# Help is displayed if there are not arguments.
help_message = """
Python3 script to acces Active Directory LDAP.
==============================================
address           address
dn                dn
password          password
"""

if not arguments:
    print(help_message)
    sys.exit()

valid_arguments = [
    'address',
    'dn',
    'password',
]

#  ----------- Error messages. -----------
sintax_error_message = """#############
Sintax ERROR.
#############
"""

valid_argument_message = 'Valid arguments are:'
for valid_argument in valid_arguments:
    valid_argument_message += ' <{}>'.format(valid_argument)

#  ----------- Error messages end. -----------


arguments_dict = {}

for argument in arguments:
    # Validate "argument_name=argument_value format."
    if '=' not in argument:
        print(sintax_error_message)
        print('Bad argument format for "{}".'.format(argument))
        print('Arguments must be defined in the form '
              '"argument_name=argument_value".')
        print(valid_argument_message)
        sys.exit()

    argument_name, argument_value = argument.split("=", 1)

    # Validate valid argument name.
    if argument_name not in valid_arguments:
        print(sintax_error_message)
        print('"{0}" is not a valid option.'.format(argument_name))
        print(valid_argument_message)
        sys.exit()

    arguments_dict[argument_name] = argument_value


# Validate required arguments.
required_arguments_list = [
    'address',
    'dn',
    'password',
]

for required_argument in required_arguments_list:
    if required_argument not in arguments_dict:
        print(sintax_error_message)
        print('<{0}> is required.'.format(required_argument))
        sys.exit()


# Get required values.
address = arguments_dict['address']
dn = arguments_dict['dn']
password = arguments_dict['password']

print("address: {}".format(address))
print("dn: {}".format(dn))
print("password: {}".format(password))

# Authentication Script
server = Server(address, get_info=ALL)

try:
    conn = Connection(server, dn, password, auto_bind=True)
    print('LDAP Bind Successful.')

    print("WHO AM I ####################")
    print(conn.extend.standard.who_am_i())
    print("WHO AM I ####################")

except core.exceptions.LDAPBindError as e:
    # If the LDAP bind failed for reasons such as authentication failure.
    print('LDAP Bind Failed: ', e)
