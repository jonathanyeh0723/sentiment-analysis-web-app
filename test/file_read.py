my_dir = "aclImdb/train/pos/9065_10.txt"

with open(my_dir, 'r') as f:
    print(f)
    print(type(f))
    print(f.read())
    print(type(f.read()))
