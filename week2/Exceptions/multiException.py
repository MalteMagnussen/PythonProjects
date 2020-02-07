try:
    with open('./Not_There.txt') as f_obj:
        contents = f_obj.read()
    print(5/0)
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError as e:
    print(e)
else:
    print("Everything went well...")
