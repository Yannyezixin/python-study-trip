

def getValue(value, message):
    while True:
        try:
            value = raw_input(message)
            if type(value) == 'int' or 'float':
                return float(value)
        except ValueError:
            print "This is not a valid number.It must be Integer or float"

hours = getValue('hours','Enter hours:');
rate = getValue('rate', 'Enter rate:');
overHours = 0;

if hours > 40:
    overHours = hours - 40
    hours = 40

pay = (hours  + overHours) * rate

print pay
