#a-z ajaylakhara@gmail.com
#0-9
#. _time 1
# @ time 1

import re
email_condition="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\W{2,3}$"
user_email=input(' Enter your Email: ')

if re.search(email_condition,user_email):
    print(" Right email ")
else:
    print(" Wrong email ")
    
