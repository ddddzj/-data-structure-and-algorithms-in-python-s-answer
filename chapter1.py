from random import randint
import string

def is_multiple(n, m):
    if n % m == 0:
        return True
    else:
        return False

def is_even(k):
    if k&1:
        return True
    else:
        return False

def minmax(data):
    a = data
    a.sort()
    return (a[0],a[-1])


def maxmin2(data):
    if data:
        m = n = data[0]
        for i in data:
            if i > m:
                m = i
            if i < n:
                n = i
        return (m,n)
    else:
        print("序列为空！")

def square_sum(n):
    result = 0
    for i in range(n+1):
        result = m + i*i
    return result

def square_sum2(n):
    return sum([k*k for k in range(n+1)])

def odd_square_sum(n):
    result = 0
    for i in range(1, n, 2):
        result += i*i
    return result

def odd_square_sum2(n):
    return sum([i*i for i in range(n+1) if i&1 == 1])

def my_choice(data):
    return data[random.randrange(len(data))]

def nizhi(data):
    a = []
    for i in range(len(data)):
        a.append(data[len(data) - i - 1])
    return a

def fun14(data):
    num = 0
    for i in range(len(data)):
        if i&1 == 1:
            num += 1
            if num >= 2:
                return True
    return False

def fun15(data):
    n = len(data)
    m = len(set(data))
    if n == m:
        return True
    else:
        return False

def myshuffle(data):
    new = []
    for i in range(len(data)):
        a = randint(0,len(data)-1)
        new.append(data[a])
        data.pop(a)
    return new

def fun21():
    a = []
    while True:
        try:
            response = input("Please input:")
            a.append(response)
        except EOFError:
            for val in a[::-1]:
                print(val)

def dot_product(data1,data2):
    for i in data1:
        if not isinstance(i,int):
            raise TypeError("element must be numeric")
    for j in data2:
        if not isinstance(j,int):
            raise TypeError("element must be numeric")
    if len(data1) != len(data2):
        raise KeyError("Their must have same length!")
    new = [data1[i] * data2[i] for i in range(len(data1))]
    return new

def fun24(data):
    num = 0
    a = ['a','e','i','o','u']
    for i in data:
        if i in a:
           num += 1
    return num

def remove_mark():
    pieces = []
    reply = input("Please input something:")
    for k in reply:
        pieces.append(k)
    punctuation = string.punctuation
    for i in pieces:
        if i in punctuation:
            pieces.remove(i)
    a = ''.join(pieces)
    return a

def threeIntegers():
    a = int(input("Please input three integers: "))
    b = int(input("b:"))
    c = int(input("c:"))
    print('a+b=c 成立') if a+b ==c else print('a+b=c 不成立')

def norm(v,p=2):
    i,temp = 0,0
    while i < len(v):
        temp += pow(v[i],p)
        i += 1
    result = pow(temp,1/p)
    return result

def fun29():
    dic = ['c','a','t','d','o','g']
    for a in range(6):
        for b in range(6):
                for c in range(6):
                    for d in range(6):
                        for e in range(6):
                            for f in range(6):
                                g = [a,b,c,d,e,f]
                                if len(set(g)) == 6:
                                    print (dic[a],dic[b],dic[c],dic[d],dic[e],dic[f])


def Perm_k(arrs, k):
    # 若输入 [1,2,3]，则先取出1这个元素，将剩余的 [2,3]中取出另一个元素得到 [[1,2],[1,3]]
    # 同理，取出2或者3时，得到的分别是 [[2,1],[2,3]]和 [[3,1],[3,2]]
    if len(arrs)==1:
        return [arrs]
    if k==1:
        return list(map(lambda s:[s], arrs))  #  当 k 为 1 时，每(单)个元素都可以被选取
    result = []  # 最终的结果（即全排列的各种情况）
    for i in range(len(arrs)):
        rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
        rest_lists = Perm_k(rest_arrs, k-1)     # 剩余的元素选取 k-1元素
        lists = []
        for term in rest_lists:
            lists.append(arrs[i:i+1]+term)  # 将取出的第 i个元素加到剩余全排列的前面
        result += lists
    return result

def fun30():
    i= 0
    data = int(input('请输入一个正整数:'))
    if data <= 0:
        print('请输入一个正整数')
        return
    while data >= 2:
        data = data // 2
        i += 1
    print(i)

def fun31(m,n): # m:支付钱数，n:给钱数
    if (m == n):
        print("无需找零")
    elif (m > n):
        print("支付金额不足")
    else:
        re = n - m
        num_50 = re // 50
        re = re % 50
        num_20 = re // 20
        re = re % 20
        num_10 = re // 10
        re = re % 10
        print ("需要找零：50元",num_50,"张，20元",num_20,"张，10元",num_10,"张")

def fun31_2(price, pay):
    money = [100, 50, 20, 10, 5, 1, 0.5, 0.1]
    cash = {}
    # 由于python存在舍入误差（rounding errors），所以弄成整数以后再算
    temp = (pay - price) * 10
    if price < pay:
        for i in money:
            quotient = temp // (i*10)
            remainder = round(temp % (i*10))
            cash[i] = quotient
            print(cash)
            if remainder == 0:
                break
            else:
                temp = remainder
        for key, value in cash.items():
            if value != 0:
                print("找零 {} 张 {} 元人民币".format(int(value), key))
    elif price == pay:
        print("刚好支付！")
    else:
        print("请支付足够金额！")
    print(cash)

def calculate():
    a = int(input())
    symbol = input()
    b = int(input())
    if symbol=="+":
        c = a + b
    if symbol=="-":
        c = a - b
    if symbol=="*":
        c = a * b
    if symbol=="÷":
        c = a / b
    equal = input()
    if equal=="=":
        print(c)

def fun35():
    num = 0
    for i in range(100):
        a = []
        for j in range(25):
            a.append(randint(1,366))
        if len(a) != len(set(a)):
            num +=1
    print(num/100.0)

def fun36():
    words = "is a word like it is the the is word banana apple word is apple"
    count = {}
    words_list = words.split(" ")
    for word in words_list:
        count[word] = 1 + count.get(word, 0)
    print(count)


if __name__ == '__main__':
    fun35()
