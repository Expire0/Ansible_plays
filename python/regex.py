import re

##match v6 addresses 
mas = open("hosts", "r")
regex = r"\d*:\d+:[a-f]+\d..*\d"


for i in mas:
    hmm=re.search(regex, i).group()
    print hmm
