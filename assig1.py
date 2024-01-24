tbl = [["161E90","Ramu",35,59000],
       ["171E22","Tejas",30,82100],
       ["171G55","Abhi",25,100000],
       ["152K46","Jaya",32,85000]]

ch = int(input("""Choose your sorting parameter:
             1. Age
             2. Name
             3. Salary \n"""))

if ch == 1:
    print(sorted(tbl, key=lambda x:x[2]))
elif ch == 2:
    print(sorted(tbl, key=lambda x:x[1]))
elif ch == 3:
    print(sorted(tbl, key=lambda x:x[3]))


