''' Bài 00: Viết chương trình sinh list mới bằng cách lấy ngẫu nhiên 5 phần tử từ list gốc.
import random
list1 = random.sample(range(1, 1001), 100)
list2 = [random.choice(list1) for i in range(5)]
print(list2)
'''

''' Viết chương trình tính tổng, tích của các phần tử trong một list.
import random
my_list = random.sample(range(1, 101), 10)
print(my_list)
print('Tổng = ',sum(my_list))
tich = 1
for i in range(len(my_list)):
    tich*=my_list[i]
print('Tích = ',tich)
'''

''' Bài 02: Viết chương trình tìm số lớn nhất, nhỏ nhất trong một list.
import random
my_list = random.sample(range(1, 10001), 10)
print(my_list)
print('Max = ',max(my_list))
print('Min = ',min(my_list))
'''

''' Bài 03: Viết chương trình tạo ra list mới bằng cách ghép một chuỗi s vào các phần tử list cũ.
list1 = ['Hello','Hi',3456,78910,3.42]
s = input('Nhập chuỗi s: ')
list2 = [s+str(list1[i]) for i in range(len(list1))]
print(list1)
print(list2)
'''

''' Bài 04: Viết chương trình chia một list thành 2 phần với độ dài phần đầu được nhập vào từ bàn phím.
import random
my_list = random.sample(range(1,1001),10)
print(my_list)
if not len(my_list):
    print('List rỗng không thể chia thành 2 phần')
else:
    while True:
        n = int(input('Nhập độ dài phẩn đầu: '))
        if 0 <= n <= len(my_list):
            list1 = my_list[:n]
            list2 = my_list[n:]
            print(list1)
            print(list2)
            break
        print('Không thể chia, nhập lại: ')
'''

''' Bài 05: Viết chương trình in ra phần tử có số lần xuất hiện nhiều nhất trong một list.
        Nếu có nhiều phần tử có cùng số lần xuất hiện nhiều nhất thì in ra 1 trong số chúng.
import random
my_list = [random.randint(1,10) for i in range(30)]
print(my_list)
my_list.sort()
count = 0
new_list = []
for i in range(len(my_list)):
    if count == 0:
        count+=1
    elif my_list[i] == my_list[i-1]:
        count+=1
        if i == len(my_list)-1:
            new_list.append((my_list[i], count))
    else:
        new_list.append((my_list[i-1], count))
        if i == len(my_list) - 1:
            new_list.append((my_list[i],1))
        count = 1

def takeSecond(lst):
    return lst[1]

new_list.sort(key=takeSecond,reverse=True)
print('Các phần tử có số lần xuất nhiều nhất: ',end=' ')
for i in range(len(new_list)):
    if i==0:
        print(new_list[i][0],end=' ')
        max = new_list[i][1]
    elif new_list[i][1] == new_list[i-1][1]:
        print(new_list[i][0],end=' ')
    else:
        break
print('\nSố lần xuất hiên nhiều nhất là: ',max)
'''

''' 
Bài 06: Viết chương trình đếm các chuỗi trong một list thỏa mãn:
        + Độ dài từ 2 trở lên
        + Ký tự đầu tiên và cuối cùng của chuỗi đó giống nhau
count = 0
my_list = ['abcda','abcdb','a','2332','0','13531','bb']
for i in range(len(my_list)):
    if len(my_list[i]) >=2 and my_list[i][0] == my_list[i][-1]:
        count+=1
print(count)
'''

''' Bài 07: Viết chương trình kiểm tra 2 list có phần tử chung hay không.
import random
list1 = random.sample(range(1, 21),10)
list2 = random.sample(range(18, 41),10)
print(list1)
print(list2)
kt = 'Không có phần tử trùng nhau'
for i in range(len(list1)):
    if kt == 'Có phần tử trùng nhau':
        break
    for j in range(len(list2)):
        if list1[i] == list2[i]:
            kt = 'Có phần tử trùng nhau'
            break
print(kt)
'''

''' Bài 08: Cho list các số nguyên dương A.
        Xây dựng chương trình đếm số lượng tập gồm 2 phần tử A[i] và A[j] thỏa mãn A[i] > A[j] và i < j.
import random
my_list = random.sample(range(1,101),20)
print(my_list)
count = 0
for i in range(len(my_list)-1):
    for j in range(i+1,len(my_list)):
        if (my_list[i] > my_list[j]):
            count+=1
print(count)
'''

''' Bài 09: Viết chương trình tính tích của 2 ma trận vuông cấp 3 (Gợi ý: dùng list chứa list).
import random
my_list = []
new_list = []
for i in range(3):
    my_list.append(random.sample(range(1,11),3))
    new_list.append([0,0,0])
for i in range(3):
    for j in range(3):
        sum = 0
        for k in range(3):
            sum = sum + my_list[i][k]*my_list[k][j]
        new_list[i][j] = sum
print(my_list)
print('Kết quả: ')
print(new_list)
'''

'''Bài 10:
Mô tả: Bạn được cung cấp một danh sách N bài hát đã từng được nghe của một người dùng ứng dụng ZingMp3.
       Bạn cần xây dựng từ danh sách trên một chuỗi dài nhất các bài hát liên tiếp trong đó không có bài hát nào được lặp lại
Input: A - mảng chứa id của mỗi bài hát
Output: Độ dài cần tìm

n = int(input('Nhập số lượng bài hát: '))
list_music = set()
for i in range(n):
    list_music.add(input('Nhập id bài hát: '))
print(len(list_music))
'''