from move import Move
from request import Request
from shop import Shop
from store import Store

store = Store(items={
    "печенька": 6,
})

shop = Shop(items={
    "печенька": 1,
})

stocks = {
    "магазин": shop,
    "склад": store
}


def main():
    print("Hello")

    while True:
        for storage_name in stocks:
            print(f"Сейчас в {storage_name}:\n {stocks[storage_name].get_items()}")

        user_input = input('Введите запрос: "Курьер забирает 3 печенька из склад в магазин"\n')
        request = Request(request=user_input, stocks=stocks)
        move = Move(request=request, stocks=stocks)
        move.go()


if __name__ == "__main__":
    main()
