e = float(input("Nhập số epsilon = "))
factorial = 1; sum = 1; n = 1;
while True:
    factorial *= n
    if 1/factorial < e:
        break
    sum+=1/factorial
    n+=1
print("e ~",sum)