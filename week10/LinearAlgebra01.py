import pandas as pd
import numpy as np


shoppers = {
    "Paula": {"Is": 4, "Juice": 2, "Kakao": 3, "Lagkager": 2},
    "Peter": {"Is": 2, "Juice": 5, "Kakao": 0, "Lagkager": 4},
    "Pandora": {"Is": 5, "Juice": 3, "Kakao": 4, "Lagkager": 5},
    "Pietro": {"Is": 1, "Juice": 8, "Kakao": 9, "Lagkager": 1},
}
shop_prices = {
    "Netto": {"Is": 10.50, "Juice": 2.25, "Kakao": 4.50, "Lagkager": 33.50},
    "Fakta": {"Is": 4.00, "Juice": 4.50, "Kakao": 6.25, "Lagkager": 20.00},
}


df = pd.DataFrame(shoppers).T

print("\ndf\n", df)

P = np.array(df)

print("\nP\n", P)

df = pd.DataFrame(shop_prices).T

print("\ndf\n", df)

Q = np.array(df)

print("\nQ\n", Q)

R = P.dot(Q)

print("\nR\n", R)

