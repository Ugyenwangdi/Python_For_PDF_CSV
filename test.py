a = ['1', 'baga', 'c', 'd']

b = [['j', 'l'], ['m', 'k']]

data = []
s = 0
for i in b:
    item = i + [a[s]] 
    print(item)

    data.append(item)
    s += 1
# print(data)