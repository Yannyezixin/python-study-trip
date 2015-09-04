globval = 0

def set_globval_to_one():
    global globval
    globval = 1

def print_globval():
    print globval

set_globval_to_one()
print_globval()

