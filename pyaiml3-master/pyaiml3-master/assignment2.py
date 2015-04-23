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
k.setBotPredicate("summerBill", "$30")
k.setBotPredicate("winterBill", "$20")


# open the log file
logfile = open("log.txt", 'a')

#Enter the main input/output loop
print("type exit to quit")
user = input("consultant> ")
while(user != "exit" ):
	logfile.write("U: "+str(user)+"\r")
	agent = k.respond(user)
	print(agent)
	user = input("consultant> ")
	logfile.write("B: "+str(agent)+"\r")
	logfile.flush()
	
logfile.write("------------------------"+"\r\n")
logfile.close()
