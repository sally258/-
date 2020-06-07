''' BTVN
Bài 1. Viết chương trình thay thế các ký tự giống ký tự đầu tiên của một chuỗi thành $
Bài 2. Viết chương trình để xóa bỏ ký tự thứ m trong chuỗi không rỗng, với m là số không âm nhập từ bàn phím
Bài 3. Viết chương trình để xóa bỏ các ký tự có chỉ số lẻ trong 1 chuỗi
Bài 4. Viết chương trình sinh ra một chuỗi từ 2 ký tự đầu và 2 ký tự cuối trong chuỗi được nhập vào, nếu độ dài chuỗi nhỏ hơn
        2 thì in ra chuỗi rỗng
Bài 5. Viết chương trình tìm ra ký tự lớn nhất và ký tự nhỏ nhất của một chuỗi nhập từ bàn phím
Bài 6. Viết chương trình đảo ngược từ ký tự thường sang ký tự hoa và từ ký tự hoa sang ký tự thường trong 1 chuỗi
'''

class Solve:
    def function1(s):
        str = ""
        for i in range(len(s)):
            if s[i] == s[0]:
                str+='$'
            else:
                str+=s[i]
        return str

    def function2(s, m):
        return s[0:m-1]+s[m:]

    def function3(s):
        str = ""
        for i in range(0, len(s), 2):
            str+=s[i]
        return str

    def function4(s):
        l = len(s)
        list = []
        for m in range(0,4):
            for n in range(0,4):
                for p in range(0,4):
                    for q in range(0,4):
                        if m!=n and m!=p and m!=q and n!=p and n!=q and p!=q:
                            str = ""
                            for i in range(0,4):
                                if i == m:
                                    str+=s[0]
                                elif i == n:
                                    str+=s[1]
                                elif i == p:
                                    str+=s[l-2]
                                else:
                                    str+=s[l-1]
                            list.append(str)
        set(list)
        list.sort()
        return list

    def funtion5(s):
        s = list(s)
        s.sort()
        return (s[0], s[len(s)-1])

    def funtion6(s):
        str = ""
        for i in range(0,len(s)):
            if 'A' <= s[i] <= 'Z':
                str+=chr(ord(s[i])+32)
            elif 'a' <= s[i] <= 'z':
                str+=chr(ord(s[i])-32)
            else:
                str+=s[i]
        return str

class c:
    d = '\033[92m'
print(c.d,end='')
s = input('Nhập vào một chuỗi: ')
while True:
    m = int(input(c.d+'Nhập vào vị trí cần xóa: '))
    if m <= 0 or m > len(s):
        print(c.d+'1 <= Vị trí <= m! Yêu cầu nhập lại')
    else:
        break
print('\nLưu ý: Chương trình chạy các yêu cầu theo chuỗi đầu tiên!!!')
print('\nChuỗi sau khi thay thế các kí tự trong chuỗi giống với kí tự đầu tiên là: ',Solve.function1(s))
print('Chuỗi sau khi xóa bỏ ký tự thứ {} là: '.format(m),Solve.function2(s,m))
print('Chuỗi sau khi xóa bỏ các ký tự có chỉ số lẻ (vị trí bắt đầu là 0): ',Solve.function3(s))
if (len(s)<2):
    print('Chuỗi mới được sinh ra từ 2 ký từ đầu và 2 ký tự cuối la: ',""," Chuỗi rỗng nên không thấy được đâu ^ ^")
else:
    print('Danh sách chuỗi mới được sinh ra từ 2 ký từ đầu và 2 ký tự cuối là:')
    lst = Solve.function4(s)
    for i in lst:
        print('\t',i)
print('Ký tự lớn nhất của chuỗi là: ',Solve.funtion5(s)[1])
print('Ký tự nhỏ nhất của chuỗi là: ',Solve.funtion5(s)[0])
print('Chuỗi sau khi đảo ngược ký tự hoa và thường với nhau: ',Solve.funtion6(s))