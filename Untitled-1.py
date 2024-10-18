def change(money):
    coins = [500, 100, 50, 10]
    result = {}
    for coin in coins:
        result[coin] = money // coin
        money %= coin
    return result

x = int(input("お支払い金額: "))
y = int(input("商品価格: "))
change_money = x - y

print("お釣り")
for coin, count in change(change_money).items():
    print(f"{coin}円硬貨: {count}枚")
