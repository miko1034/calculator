import re

test = "5+5"

# aint working
def eval(statement):
    result = re.split("+-*/", statement)
    return result


print(eval(test))