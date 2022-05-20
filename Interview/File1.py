word ="Error"
path = r""
with open(path) as file:
    for i in file:
        if i.split():
            if i== word:
                print(i)
        else:
            pass

