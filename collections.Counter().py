from collections import Counter

shoes_num = int(input())


shoes_list = input()
shoes_list = list(map(int, shoes_list.split(' ')))
shoes_list = Counter(shoes_list)
cost = 0
customer_no = int(input())
for i in range(customer_no):
    customer_shoes = input()
    customer_shoe = list(map(int, customer_shoes.split(' ')))
    if shoes_list[customer_shoe[0]] > 0:
        cost += customer_shoe[1]
        shoes_list[customer_shoe[0]] = shoes_list[customer_shoe[0]] - 1

print(cost)