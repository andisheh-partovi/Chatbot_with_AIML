import sys
sys.path.append('./aiml')

import aiml
k = aiml.Kernel()
k.learn('sheldon.aiml')

# set a constant
k.setBotPredicate("name", "Sheldon Cooper")
k.setBotPredicate("city", "Melbourne")
k.setBotPredicate("houseHoldMemberNumbers", "2")
k.setBotPredicate("houseHoldMember", "Leonard")
k.setBotPredicate("age", "30")
k.setBotPredicate("friendAge", "32")
k.setBotPredicate("job", "student")
k.setBotPredicate("weekdaysHours", "14")
k.setBotPredicate("weekendsHours", "24")
k.setBotPredicate("summerBill", "$300")
k.setBotPredicate("winterBill", "$200")

while True: 
    response = k.respond(input("User> "))
    print(response)