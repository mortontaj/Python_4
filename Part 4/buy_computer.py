avaliable_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "hdmi cable",
                   "dvd drive"
                   ]
# valid_choices = [str(i) for i in range(1, len(avaliable_parts) + 1)]
valid_choices = []
for i in range(1, len(avaliable_parts) + 1):
    valid_choices.append(str(i))
print(valid_choices)
current_choice = "-"
computer_parts = [] # create an empty list

while current_choice != '0':
    if current_choice in valid_choices:
        #print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = avaliable_parts[index]
        if chosen_part in computer_parts:
            # it's already in, so remove it
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        print("Your list now contains: {}".format(computer_parts))

    else:
        print("Please add options from the list below: ")
        for number, part in enumerate(avaliable_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)
