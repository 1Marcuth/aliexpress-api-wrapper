from aliexpress_api import AliExpress
import json

def main():
    ali = AliExpress(
        currency = "BRL",
        language = "pt"
    )

    ali.fetch_product(url="https://pt.aliexpress.com/item/1005004336772445.html")
    data = ali.search_products("Batatas")

    print(json.dumps(data))

if __name__ == "__main__":
    main()