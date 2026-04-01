def even_numbers():
    for i in range(1,11):
        yield i*2

Gen = even_numbers()

for num in Gen:
    print(num)