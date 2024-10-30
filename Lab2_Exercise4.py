
def display_main_menu():
    print("display_main_menu")
    print("Enter some number s separated by commas (e.g. 5,67,32)")


def get_user_input():
    print("get_user_input")
    inputstr = input()
    print("Raw Input = " + inputstr)

    # Split the input string in to segments of strings using comma as spliiter
    splitlist = inputstr.split(",")
    print("After splitting = ", splitlist)

    # Next step is to convert each short string in the list into float
    floatlist = []  # define an empty list of float numbers
    for x in splitlist:
        floatnum = float(x)   # Convert string into float
        floatlist.append(floatnum)  # Add the float number to the float list
    print("Float list = ", floatlist)
    return floatlist



def calc_average(input_list):
    print("calc_average")
    total = sum(input_list)
    average = total/len(input_list)
    print("Average = ", average)
    return average


def find_min_max(input_list):
    print("find_min_max")
    input_list.sort()
    resultlist = [input_list[0], input_list[-1]]
    print("Min & Max list = ", resultlist)
    return resultlist


def sort_temperature(input_list):
    print("sort_temperature")


def calc_median_temperature(input_list):
    print("calc_median_temperature")


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Intro to Python")
    display_main_menu()
    floatlist = get_user_input()
    calc_average(floatlist)
    find_min_max(floatlist)


if __name__ == "__main__":
    main()
