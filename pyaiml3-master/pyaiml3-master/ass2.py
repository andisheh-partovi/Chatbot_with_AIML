import sys
sys.path.append('./aiml')

import aiml
k = aiml.Kernel()
k.learn('consultant.aiml')
while True: 
    response = k.respond(input("consultant> "))
    print(response)