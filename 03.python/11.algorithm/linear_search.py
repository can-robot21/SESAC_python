# 선형탐색(Linear Searcjh) 


def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return 1
        
    return -1
import random
def number_count(count):
    random.numbers = [random.randint(1, 1_000_000_000) for _ in range(count)]
    return random.numbers

my_list1 = [5, 8, 3, 7, 10]
my_list2 = number_count(5_000_000)
target = 7


start_time = time.time()

result = linear_search(my_list, target)
end_time = time.time()
diff_time = end_time - start_time
print(f'찾는데 걸린 시간: {diff_time} second')

if result != -1:
    prnt("타켓 index:", result)
else:
    print("타켓이 없음")