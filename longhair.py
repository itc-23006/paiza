def check_lucky_number(N):
    if N % 7 == 0:
        return "lucky"
    else:
        return "unlucky"


N = int(input())

result = check_lucky_number(N)
print(result)
