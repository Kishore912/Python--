n = int(input())
integer_list = map(int, input().split())
jo = tuple(integer_list)
print(hash(jo))