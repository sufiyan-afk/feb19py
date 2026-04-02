k = [(10,"python"),(20,"java"),(30,"php"),(40,"android")]

l = zip(*k)
print(next(l))
print(next(l))

lst = ["name","city","course"]
tup = ("Sufiyan","Navapur","python full stack")

l = zip (lst,tup)
print(dict(l))

