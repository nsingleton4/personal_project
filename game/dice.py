import random

# def function_name( parameters ):
#     "function_docstring"
#     function_suite
#     return [expression]

def roll_dice(d20=False, d10=False, d6=False, number = 1):
    if d20:
        return random.randint(1,20)
    elif d10:
        return random.randint(1,10)
    elif d6:
        return random.randint(1,6)
    else:
        print("No dice chosen")


if __name__ == "__main__":
    print(roll_dice(d20 = True))

# a single d20 roll
# print(roll_dice(d20 = True))

# # 3 individual rolls of a d6 added together
# print(sum([roll_dice(d6 = True),
#           roll_dice(d6 = True),
#           roll_dice(d6 = True)]))
