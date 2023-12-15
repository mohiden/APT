import requests
from bs4 import BeautifulSoup


class AmazonProductTracker:
    def __init__(self, product_url):
        self.product_url = product_url
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/120.0.0.0 Safari/537.36',
            'accept-language': 'en-GB,en;q=0.9',
        }

    def check_product_stock(self) -> bool:
        try:
            response = requests.get(self.product_url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            not_in_stock = soup.find('span', {'class': 'a-size-medium a-color-success'})
            print(not_in_stock.contents)

            if not_in_stock:
                return False
            else:
                return True

        except requests.exceptions.RequestException as e:
            print(f"Error Checking product availability: {e}")
            return False


def main():
    product_url = input("Product Url: ")
    # Product tracking
    out_of_stock_url = (
        'https://www.amazon.com/Apple-Generation-Lightning-Resistant-Headphones/dp/B0BDHB9Y8H/ref=sr_1_2'
        '?crid=2X8C3AMO8W7YB&keywords=apple+airpods&qid=1702602205&sprefix=apple+airp%2Caps%2C296&sr=8-2')
    in_stock_url = ('https://www.amazon.com/Ultra-Game-Vintage-Baseball-Patriots/dp/B076Q82RY6?ref_'
                    '=Oct_DLandingS_D_9080603b_2')

    # Create instances
    tracker = AmazonProductTracker(product_url)
    in_stock = tracker.check_product_stock()

    if in_stock:
        print(f"Product is in stock")
        # Implement further processing or notifications based on the product data
    else:
        print("Product not in stock")


if __name__ == "__main__":
    main()

