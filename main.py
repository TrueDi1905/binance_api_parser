import websockets
import asyncio
import json
from tg_bot import send_message


async def main():
    currency = {"BTC/USDT": "btcusdt@miniTicker",
                "ETH/BTC": "ethusdt@miniTicker",
                "DOT/USDT": "dotusdt@miniTicker",
                "ETH/USDT": "ethbtc@miniTicker"}

    url = f"wss://stream.binance.com:9443/stream?streams=" \
          f"{currency['BTC/USDT']}/{currency['ETH/BTC']}/" \
          f"{currency['DOT/USDT']}/{currency['ETH/USDT']}"

    with open('config.json') as json_file:
        data = json.load(json_file)

    async with websockets.connect(url) as client:
        while True:
            current_data = (json.loads(await client.recv())['data'])
            currency_name = current_data["s"]
            currency_price = current_data["c"][:-6]
            if currency_name == 'BTCUSDT':
                name = "BTC/USDT"
            if currency_name == 'ETHBTC':
                name = "ETH/BTC"
            if currency_name == 'DOTUSDT':
                name = "DOT/USDT"
            if currency_name == 'ETHUSDT':
                name = "ETH/USDT"

            if data[name]['trigger'] == 'more':
                if currency_price > data[name]['price']:
                    await send_message(
                        message=f"Цена {currency_name} "
                                f"изменилась на {currency_price} $")
            if data[name]['trigger'] == 'less':
                if currency_price < data[name]['price']:
                    await send_message(
                        message=f"Цена {currency_name} "
                                f"изменилась на {currency_price} $")
            if data[name]['trigger'] == 'more_eq':
                if currency_price >= data[name]['price']:
                    await send_message(
                        message=f"Цена {currency_name} "
                                f"изменилась на {currency_price} $")
            if data[name]['trigger'] == 'less_eq':
                if currency_price <= data[name]['price']:
                    await send_message(
                        message=f"Цена {currency_name} "
                                f"изменилась на {currency_price} $")

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
