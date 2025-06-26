import time
import random

def check_signals():
    pairs = ["EURUSD", "USDJPY", "XAUUSD", "GBPJPY", "EURJPY", "AUDUSD", "USDCAD", "GBPUSD", "XAGUSD"]
    for pair in pairs:
        signal = random.choice(["קנייה", "מכירה"])
        price = round(random.uniform(1.0, 2000.0), 4)
        print(f"📊 {pair} – איתות {signal} במחיר {price}")

while True:
    check_signals()
    time.sleep(10)
