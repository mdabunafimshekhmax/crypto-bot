import requests
import time

TOKEN = '8651926915:AAEAjc2mRSeQGF_Mt6ejySE7nx1Yt0W_C20'
CHAT_ID = '@crypto_live_price_world'

def get_crypto_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    data = requests.get(url).json()
    price = round(float(data['price']), 2)
    return f"🚀 BTC Current Price: ${price}"

def send_telegram_msg(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

if __name__ == "__main__":
    while True: # এটি বটটিকে বারবার চালাবে
        msg = get_crypto_price()
        send_telegram_msg(msg)
        time.sleep(600) # ৬০০ সেকেন্ড বা ১০ মিনিট বিরতি
