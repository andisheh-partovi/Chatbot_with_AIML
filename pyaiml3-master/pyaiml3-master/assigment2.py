import sys
sys.path.append('./aiml')

import aiml
k = aiml.Kernel()
k.learn('consultant.aiml')

# set a constant
k.setBotPredicate("name", "Mr.White")
k.setBotPredicate("city", "Melbourne")

while True: 
    response = k.respond(input("User> "))
    print(response)