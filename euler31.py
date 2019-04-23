# In England the currency is made up of pound, £, and pence, p, and there are eight coins
# in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way: 1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p
#
# How many different ways can £2 be made using any number of coins?
#
# Answer: 73682

COINS = [1, 2, 5, 10, 20, 50, 100, 200]

def sum_coin(target, coins):
    if target == 0:
        return 1
    else:
        counter = 0
        for coin in coins:
            if target - coin < 0:
                break
            else:
                counter += sum_coin(target-coin, coins[:coins.index(coin)+1])
    return counter

if __name__ == '__main__':
    print(sum_coin(200, COINS))
