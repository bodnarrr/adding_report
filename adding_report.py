def adding_report(output_type):
    items = ""
    total = 0
    print('Input an integer to add to the total or "Q" to quit')
    while True:
        curr_in = input('Enter an integer or "Q": ')
        if curr_in.isdigit():
            total += int(curr_in)
            items = items + "\n" + curr_in
        elif curr_in == "Quit" or curr_in == "Q":
            break
        else:
            print(curr_in + " is incorrect input")
    if output_type == "A":
        print("Items" + items + "\n" + "Total\n" + str(total))
    elif output_type == "T":
        print("Total\n" + str(total))


while True:
    output_type = input('Choose report type ("A" or "T"): ')
    if output_type == "A" or output_type == "T":
        break
    else:
        print(output_type + " is invalid input")
adding_report(output_type)
