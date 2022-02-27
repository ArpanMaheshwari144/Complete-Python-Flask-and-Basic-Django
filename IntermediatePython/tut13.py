# users = ['Arpan', 'Adarsh', 'Verma', 'Patra']
# computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']
# for i in range(len(users)):
#     var = "Computer used by "+ users[i]+ " is "+ computer[i]
#     print(var)


# users = ['Arpan', 'Adarsh', 'Verma', 'Patra']
# computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']
# for i in range(len(users)):
#     var = "Computer used by {} is {}"
#     print(var.format(users[i], computer[i]))


users = ['Arpan', 'Adarsh', 'Verma', 'Patra']
computer = ['raspberry pi', 'tuf', '16GB RAM vala', 'sabse mehnga vala']
for i in range(len(users)):
    var = "Computer used by {1} is {0}"
    print(var.format(users[i], computer[i]))