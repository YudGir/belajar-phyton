def evaluate_grade(grade):
    if grade < 75:
        message = "Sorry, you're not passed it!"
    elif grade > 100:
        message = "Wrong input!"
    else:
        message = "You're passed it!"
    return message


print (evaluate_grade(101))
