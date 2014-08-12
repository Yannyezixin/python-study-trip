import datetime

now =  datetime.datetime.now()

print now
print now.year
print now.month
print now.day
print str(now.hour) + ':' + str(now.minute) + ':' + str(now.second)
#you can do it in anthor way
print ' %s:%s:%s' % (now.hour, now.minute, now.second)
