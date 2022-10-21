import random
def creat(n,n_min,n_max):
    lst_random = list()
    for i in range(0,n):
        lst_random.append(random.uniform(n_min,n_max))
    return lst_random
n = int(input("Введите количество элементов в списке \n"))
while True:
    n_min = float(input("Введите минимальной порог \n"))
    n_max = float(input("Введите максимальный порог \n"))
    if n_min >= n_max :
        print("Условия введены не коректно, попробуйте ещё раз")
    else:
        break
lst_random = creat(n,n_min,n_max)
print(lst_random)
