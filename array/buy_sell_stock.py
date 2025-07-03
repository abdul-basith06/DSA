# 🧠 Problem: Best Time to Buy and Sell Stock
# 🔹 Problem Statement:
# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If no profit can be made, return 0.

###

# ✅ Approach:
# - Initialize `min_price` as infinity and `max_profit` as 0.
# - Iterate through the list of prices:
#     - If current price is less than `min_price`, update `min_price`.
#     - Else calculate `profit = price - min_price`
#         - If `profit` is greater than `max_profit`, update `max_profit`, `buy_price`, and `sell_price`.
# - This ensures we always buy before we sell and get the best profit.
# - Time Complexity: O(n), Space Complexity: O(1)


def get_max_profit(prices):
    min_price = float('inf')
    max_profit = 0
    buy_price = sell_price = 0

    for price in prices:
        if price < min_price:
            min_price = price
        else:
            profit = price - min_price
            if profit > max_profit:
                max_profit = profit
                buy_price = min_price
                sell_price = price

    return buy_price, sell_price


if __name__ == "__main__":
    prices = [6, 9, 2, 5, 10, 12]
    buy, sell = get_max_profit(prices)
    profit = sell - buy
    print(f"The best day to buy is {buy} and sell it on {sell}")
    print(f"The profit generated is {profit}")
    