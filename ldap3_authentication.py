import sys
from ldap3 import Server, Connection, ALL, NTLM

arguments = sys.argv

# Delete first argument (script name)
del arguments[0]

# Help is displayed if there are not arguments.
help_message = """
Python3 script to acces Active Directory LDAP.
==============================================
servername        servername
user              Domain\\User
password          password
"""

if not arguments:
    print(help_message)
    sys.exit()

valid_arguments = [
    'servername',
    'user',
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

    argument_name, argument_value = argument.split('=')

    # Validate valid argument name.
    if argument_name not in valid_arguments:
        print(sintax_error_message)
        print('"{0}" is not a valid option.'.format(argument_name))
        print(valid_argument_message)
        sys.exit()

    arguments_dict[argument_name] = argument_value


# Validate required arguments.
required_arguments_list = [
    'servername',
    'user',
    'password',
]

for required_argument in required_arguments_list:
    if required_argument not in arguments_dict:
        print(sintax_error_message)
        print('<{0}> is required.'.format(required_argument))
        sys.exit()


# Get required values.
servername = arguments_dict['servername']
user = arguments_dict['user']
password = arguments_dict['password']

# Authentication Script
server = Server(servername, get_info=ALL)
conn = Connection(server, user=user, password=password, authentication=NTLM)

print("WHO AM I ####################")
print(conn.extend.standard.who_am_i())
print("WHO AM I ####################")
