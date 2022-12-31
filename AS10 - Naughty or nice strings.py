filename = "santastring.txt"

#Uses a textfile called santastring.txt
vowellist = ["a","e","i","o","u"]

validitycount = 0

with open (filename, "r") as filevar:
  for line in filevar:
    print(line)
    stringvalid = True
    string = line

    #Check 1: at least 3 vowels
    vowels = 0
    for i in range(0,len(string)):
      if string[i] in vowellist:
        vowels += 1

    #print("Number of vowels = ",vowels)
    if vowels < 3:
      stringvalid = False

    #Check 2: at least one letter twice in a row i.e. xx
    twiceinarow = False
    for i in range(0,len(string)-1):
      if string[i] == string[i+1]:
        twiceinarow = True
    if twiceinarow == False:
      stringvalid = False

    #Check 3: Does not contain ab, cd, pq, or xy
    containsphrases = False
    for i in range(0,len(string)-1):
      couple = string[i]+string[i+1]
      if couple in ("ab","cd","pq","xy"):
        containsphrases = True
    if containsphrases == True:
      stringvalid = False


    if stringvalid == True:
      validitycount += 1


print(validitycount)
