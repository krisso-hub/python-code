list_num = [2,4,6,8, 10]
iter_obj = iter(list_num)
while True:
    try:
        ele = next(iter_obj)
        print(ele)
    except StopIteration:
        break
