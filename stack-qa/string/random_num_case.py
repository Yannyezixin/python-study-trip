import string, random

print map(lambda x: ''.join(random.choice(string.ascii_uppercase + string.digits)
                            for x in range(10)), range(0, 10))
