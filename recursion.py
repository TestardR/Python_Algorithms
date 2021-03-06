# def get_fib(position):
#     if(position == 0):
#         return 0
#     if(position == 1):
#         return 1

#     first = 0
#     second = 1
#     next = first + second

#     for x in range(2, position):
#         first = second
#         second = next
#         next = first + second
#     return next


def get_fib(position):
    if position == 0 or position == 1:
        return position

    return get_fib(position - 1) + get_fib(position - 2)


print(get_fib(4))
