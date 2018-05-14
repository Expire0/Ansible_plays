
# parse log into list and search by date. 
#library for csa 

log = open('csa_log.log' , 'r')


t = []
range1 = input("Enter year and month ex: 2018-03: " )
with log as dipp:
    data = dipp.read().splitlines()

for view in data:
    if range1 in view:
        print(view)
        t.append(view)

count = len(t)
print("Total transactions for the month %d" %  (count))
