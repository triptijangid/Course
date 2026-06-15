names = ["Ram", "Shyam", "Hari"]
iter_obj = iter(names)
while True:
    try:
        name = next(iter_obj)
        print(name)
    except StopIteration:
        break
