"""
/*在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。
"""


def lemon_find_zero(l1):
    five, ten, = 0, 0
    for i in range(len(l1)):
        if l1[i] == 5:
            five += 1
        elif l1[i] == 10:
            ten += 1
            five -= 1
            if five < 0:
                return False
        else:
            if ten >= 1 and five >= 1:
                ten -= 1
                five -= 1
            elif five >= 3:
                five -= 3
            else:
                return False
    return True








