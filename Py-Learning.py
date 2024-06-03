print("Hello World 世界你好!!")    #print 可以打印多个变量到屏幕上，中间用 , 隔开
    # 字面量：代码中被写下来的固定值。
    # Python 常见有6种数据类型：数字（Number），字符串（String），列表（List），元组（Tuple），集合（Set），字典（Dictionary）
        # 其中数字（Number）分为：
            # 整数（int）：比如 2，3，10，-4
            # 浮点数（float）：比如 1.45，-44.2
            # 复数（complex）: 比如 2+1j,复数以j结尾
            # 布尔（bool）: 表示现实生活中的真与假，True为真记作1，False为假记作0
        # 字符串（String）是由任意数量的字符组成，比如："5df454fg", "%$^#", "的算法对"------字符串要加""
        # 列表（List）是有序的可变序列，可以有序记录一堆数据，最常用
        # 元组（Tuple）是有序的不可变序列
        # 集合（Set）是无序不重复的数据集合
        # 字典（Dictionary）可以无序记录一堆 Key-Value型的Python数据集合

"""
    注释分为单行注释和多行注释
    单行注释 在语句前加 #，快捷键 Ctrl + /
    多行注释 在语句块前后加 三个双引号
"""

    # 变量：在程序运行中，用来记录数据，让我们能重复使用它
    # 变量格式：变量名 = 变量值
        # 变量名就是变量本身，它的代号
        # “=”是赋值，表示把 = 右侧的值赋予给左侧的变量，注意！！！ 右侧赋予左侧
        # 变量值就是变量储存的内容
# Money = 100
# print("钱包里有",Money,"元")
# Money = Money - 10
# print("买东西花了1 0元")
# print("钱包里还有",Money,"元")

# a = type("dgfadgag")    #type 语句用来查看字面量和变量存储的数据的类型,有结果（返回值）

# print(type(Money))
# print(a)

    # 变量没有类型，我们说的字符串变量并不是说这个变量是字符串，而是这个变量储存了字符串

    # 转换语句：有结果（返回值）
        # int(x) 将x转换成一个整数
        # float(x) 将x转换成一个浮点数
        # str(x) 将x对象转换成字符串

    # 标识符 是名字，只允许英文，数字和下划线。数字不可用在开头，大小写要区分且不可使用关键字

    # 运算符：
        # + 加
        # - 减
        # * 乘
        # / 除
        # // 取整除，结果为向下取整的整数
        # %  取余数，
        # ** 计算乘方，比如 2**9 就是2的9次方
    # a += b 是 a = a + b, 同理 -=, *=, /=, %=, **=, //=

# a = 2
# b = 3
# print("ragagafga234*/-ds\"jgjjhgjghj")

    # 字符串的三种定义方法：
        # 单引号 a = 'ragagafga234*/-ds'
        # 双引号 a = "ragagafga234*/-ds"
        # 三引号 a = """ragagafga234*/-ds""" ，也可以用作多行注释
    # 如果字符串里含有引号，可能会引发混淆，可以用 转义字符\ 放在符号前可以解除引号作用
    # 字符串的拼接：可以用 + 拼接，只能与字符串拼接
        # 字面量和字面量直接可以拼接
# print("123" + "abc")
        # 字面量和变量直接可以拼接
# name = "Klaus"
# print("123" + name)

    # 字符串格式化，"%占位符" %变量
# year = 2024
# month =5
# sum = "现在是%s年，%s月" %(year,month)
# print(sum)
    # 用%s来占位。其中 % 表示我要占位， s 表示将内容变成字符串放入应该占位的地方
    # 用%d来占位。其中 % 表示我要占位， d 表示将内容变成整数放入应该占位的地方
    # 用%f来占位。其中 % 表示我要占位， f 表示将内容变成浮点数放入应该占位的地方

    # 数字精度控制，可以用辅助符号 m.n 来控制数据的宽带和精度
        # %5d 说明将整数的宽度控制在5位。如果是12，控制后变成 [][][]12, 在前面用三个空格补足宽度
        # %7.2f 说明将浮点数宽度控制在7位，小数点精度在2位。如果是11.345，控制后变成 [][]11.35。
            # 为什么只有两个空格，因为小数点和小数部分都算入宽度计算，小数部分四舍五入
            # m 部分比数字本身宽度小的话，则没反应不生效

    # 第二种字符串格式化的方法，用 f"{变量} {变量}" 进行快速格式化
# name = "Klaus"
# age = 24
# bir = 5.23
# print(f"我叫{name}，我今年{age}岁，生日是{bir}。")
        # 这种方法适用于任何数据类型，但是不会控制精度

    # 表达式就是一个有明确结果的代码语句，适用于格式化

# 小练习：
# name = 'Samsumg'
# s_price = 19.99
# s_code = "003032"
# s_p_d_g_f = 1.2
# growth_day = 7
#
# print(f"公司名称：{name}，股票代码：{s_code}，当前股价{s_price}元。")
# s_price *= s_p_d_g_f ** growth_day
# print("每日增长系数是：%.1f,经过 %d 天的增长后，股价为%.2f" %(s_p_d_g_f, growth_day,s_price))

    # input() 输入语句 () 中可以直接打印出来
# you = input("你的代号是？")
# print("代号为%s" %you)
    # 无论键盘输入什么类型的数据，获得到的数据都是字符串

# 小练习：
# name = input("您的用户名是？")
# user_type = input("您的会员等级是？")
# print(f"{name}您好，你是尊贵的{user_type}级会员，欢迎光临！")

    # 布尔运算，只有两个字面量：True(1) 和 False(0),还可以通过比较运算来得到布尔结果
    # == 判断是否相等，!= 判断是否不相等
# bl1 = True
# bl2 = False
# print(bl1 != bl2)

    # 判断语句，if 语句格式为: （注意缩进 和 ：）
"""
    if (要判断的条件):
        条件成立，则执行此条1
        条件成立，则执行此条2
        ...
"""

    # if else 语句
"""
    if (要判断的条件):
        条件成立，则执行此条1
        条件成立，则执行此条2
    else:
        条件不成立，则执行此条1
        条件不成立，则执行此条2
        ...
"""


# if elif else 语句
"""
    if (要判断的条件1):
        条件成立，则执行此条1
        条件成立，则执行此条2
    elif (条件2):   
        条件2成立，则执行此条1
        条件2成立，则执行此条2
    elif (条件3):   
        条件3成立，则执行此条1
        条件3成立，则执行此条2
    
    ...
    
    else:
        所有条件不成立，则执行此条1
        所有条件不成立，则执行此条2
"""

# age = int(input("欢迎来到这里，你的年龄是"))
# if (age >18):
#     print("很好，你可以进去了")
# elif (age == 18):
#     print("刚好成年，你可以进去了")
# else:
#     print("未成年，不允许进入")

# 小练习
# a = 3
# num = input("1，2，3，4，5三个数字，猜猜我心里的数字是多少")
# num = int(num)
# if (num == 3):
#     print("厉害，一次就猜对了")
# elif (int(input("不对，再猜一次") ) == 3):
#     print("猜对了")
# elif (int(input("不对，再猜一次") ) == 3):
#     print("猜对了")
# else:
#     print("机会用完，数字是3")

# 小练习
# age = int(input("请输入你的年龄："))
# if (age < 18):
#     print("年龄太小了，不可以领取礼物！")
# else :
#     if (age < 30) :
#         t = int(input("请输入你的入职时间："))
#         r = int(input("请输入你的级别："))
#         if (t > 2) :
#             print("年龄达标，入职时间达标，可以领取礼物")
#         elif (r > 3) :
#             print("年龄达标，级别达标，可以领取礼物")
#         else :
#             print("必须要入职时间大于2年或者等级大于3，你不满足不可以领取礼物！")
#     else :
#         print("年龄太大了，不可以领取礼物！")

# 小练习
# import random
# num = random.randint(1,10)  #用来产生一个可以储存随机数的变量
# print(num)
# print("你有3次机会，从1 - 10之中猜一个数字")
# g = int(input("你猜的是："))
# if (g < num) :
#     g = int(input("这个数有点小，再猜一次："))
#     if (g > num) :
#         g = int(input("这个数有点大，再猜一次："))
#         if (g != num ) :
#             print("三次都没有猜对，这个数是%d" %num)
#         else :
#             print("猜对了，这个数是%d" %num)
#     elif (g < num) :
#         g = int(input("这个数有点小，再猜一次："))
#         if (g != num):
#             print("三次都没有猜对，这个数是%d" % num)
#         else:
#             print("猜对了，这个数是%d" % num)
#     else :
#             print("猜对了，这个数是%d" % num)
#
# if (g > num) :
#     g = int(input("这个数有点大，再猜一次："))
#     if (g > num) :
#         g = int(input("这个数有点大，再猜一次："))
#         if (g != num ) :
#             print("三次都没有猜对，这个数是%d" %num)
#         else :
#             print("猜对了，这个数是%d" %num)
#     elif (g < num) :
#         g = int(input("这个数有点小，再猜一次："))
#         if (g != num):
#             print("三次都没有猜对，这个数是%d" % num)
#         else:
#             print("猜对了，这个数是%d" % num)
#     else :
#             print("猜对了，这个数是%d" % num)
#
# else:
#     print("猜对了，这个数是%d" % num)

    # while 循环语句,只有条件满足就会无限循环执行,可以嵌套
"""
    while (条件) :
        条件满足时，做的事情1
        条件满足时，做的事情2
        条件满足时，做的事情3
        ...
"""
# 小练习
# i = 1
# sum = 0
# while (i <= 100) :
#     sum = sum + i
#     print(sum)
#     i += 1
# print(sum)

# 小练习
# import random
# r_num = random.randint(1,100)
# # print("请从1 - 100 之中猜一个数字%d" %r_num)
# g = int(input("请输入你猜的数字"))
# i = 0
# while (g != r_num) :
#     i += 1
#     if (g > r_num) :
#         print("猜大了")
#     else :
#         print("猜小了")
#     print("这是你猜的第%d次" %i)
#     g = int(input("再猜一次："))
# print("猜中了，你一共猜了%d次" %i)

    # print 语句输出默认换行，使用 end = '',即可使输出不换行
    # 制表符： \t,可以使我们的字符串在多行之间对其，相当于按下tab键

# 小练习
# r = 1
# while ( r <= 9 ) :
#     i = 1
#     while (i < r):
#         print(f"{i} * {r} = {i * r} \t", end= '')
#         i += 1
#     print(f"{r} * {i} = {i * r}")
#     r += 1

    # for 循环语句，把被处理数据集里的数据拿出来依次的执行,无法定义循环条件
    # 待处理数据集就是序列：字符串，列表，元组等
    # for 循环中的临时变量，其作用域限定在循环内
"""
for 临时变量 in (待处理数据集) :
    执行的语句
"""
# 小练习
# name = 'fhfkadytuh54jaa'
# i = 0
# for x in (name) :
#     if (x == 'a'):
#         i += 1
# print(i)

    # range(num) 获取一个从0 开始，到 num 结束的数字序列
    # range(num1, num2) 获取一个从 num1 开始，到 num2 结束的数字序列,且不包含 num2 本身100
    # range(num1, num2, step) 获取一个从 num1 开始，到 num2 结束的数字序列,且不包含 num2 本身，其中 step 是步长（间隔）
        # 比如 range(1, 10, 2)就是从 1 开始每隔 2 取一个数，结果是 1 3 5 7 9
# 小练习
# num = int(input("请输入一个数"))
# i = 0
# for x in range(1, num) :
#     print(x, end=' ')
#     if (x % 2 == 0) :
#         i += 1
# print()
# print("有%d个偶数" %i)

    # continue 关键字，可以用于中断本次循环直接进入下一次循环，可用与 for 和 while
    # break 直接结束所在的循环
    # 在嵌套循环中， break 和 continue 无法对上层循环作用

    # 函数是组织好的可重复使用的代码段
    # 函数语句：没有传入参数和返回值也可以，但是传入参数的位置必须有括号
    # 函数定义好后必须要调用才能使用，调用直接用: 函数名(传入参数)
"""
    def 函数名 (传入参数) :
        函数体
        ...
        return 返回值
"""

# 小练习
# def str_lent(data) :
#     i = 0
#     for x in data:
#         i += 1
#     print(i)
#
# str1 = '6tshtzfhzhz'
# str2 = '6'
# str3 = '6tshthzzhz'
#
# str_lent(str1)
# str_lent(str2)
# str_lent(str3)
# print(type(str_lent(str1)))

    # 函数定义中的参数是形式参数,函数调用中的参数是实际参数，参数数量不限用逗号隔开
# 小练习
# def tem_test (t) :
#     """
#     函数要有说明文档，方便阅读。在Pycharm环境下，用3引号会自动补全注释
#     :param t:
#     :return:
#     """
#     if (t > 37.5) :
#         print(f"您的体温是{t}度，体温过高，需要隔离！")
#     elif (t <= 36) :
#         print(f"您的体温是{t}度，体温过低，不正常！")
#     else :
#         print(f"您的体温是{t}度，体温正常，请进")
#     return t
#
# while (1 != 0) :
#     t = int(input("请输入您的体温："))
#     t = tem_test(t)
#     if ( t>37.5 ) :
#         print("你发烧了")
#     else :
#         print("ok")
    # 返回值，return 一个 返回值 之后在函数调用是就可以用一个变量接受这个数据，return 代表函数结束
    # 当函数没有 return 时，也有返回值：None ，类型是 NoneType

    # 局部变量只存在函数内部，不可以在外部调用
    # 全局变量是在函数内外都可以使用的，定义在函数外面即可



