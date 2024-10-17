import random
first_field = random.randint(3, 20)
print('Первая вставка:', first_field)
password = ""
for i in range (1, first_field):
    for j in range (i+1, first_field):
        if first_field % (i + j) == 0:
            password += str(i)+str(j)
print('Вторая вставка', password)