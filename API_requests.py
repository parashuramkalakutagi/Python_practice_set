import requests
import json
from openpyxl import Workbook


def random_user_request(id):
    try:
        url = f"https://api.freeapi.app/api/v1/public/randomusers/{id}"
        response = requests.get(url=url)
        data = response.json()

    except Exception as e:
        print(e)

    if data['success'] and data['statusCode'] == 200 :
        data = data['data']
        first_name = data['name']['first']
        last_name = data['name']['last']
        email = data['email']
        gender = data['gender']
        location = data['location']['city']
        country = data['location']['country']
        state = data['location']['state']
        return first_name, last_name, email, gender, location, country, state
    else:
        raise Exception("Not able to find data")


def main():
    try:
        data = random_user_request(14)
        print(data)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()





def Men_watches_list():
    url = "https://api.freeapi.app/api/v1/public/randomproducts?page=1&limit=10&inc=category%2Cprice%2Cthumbnail%2Cimages%2Ctitle%2Cid&query=mens-watches"
    request = requests.get(url)
    data = request.json()

    if data['success'] and data['statusCode'] == 200:
        products = []
        for item in data['data']['data']:
            category = item['category']
            images = item['images'][0:]
            price = item['price']
            thumbnail = item['thumbnail']
            title = item['title']

            products.append({'category':category,'images':images,'price':price,'thumbnail':thumbnail,'title':title})
        return products
    else:
        raise Exception("Un available products")


def write_to_excel(data):
    wb = Workbook()
    ws = wb.active
    ws.append(['Category', 'Images', 'Price', 'Thumbnail', 'Title'])

    for item in data:
        images = ', '.join(item['images'])
        ws.append([item['category'],images, item['price'], item['thumbnail'], item['title']])
    wb.save("men_watches.xlsx")

def main():
    data = Men_watches_list()
    write_to_excel(data)
    print("Data written to men_watches.xlsx")

if __name__ == '__main__':
    main()




def random_jokes():
    for i in range(1,10):
        url = f"https://api.freeapi.app/api/v1/public/randomjokes?limit=10&query=science&inc=categories%2Cid%2Ccontent&page={i}"
        response = requests.get(url)
        data = response.json()

        if data['success'] :
            jokes = []
            for item in data['data']['data']:
                try:
                    categories = item['categories'][0]
                except:
                    categories = None
                try:
                    content = item['content']
                except:
                    content = None

                jokes.append({'content ':content,'categories':categories})
            return jokes
        else:
            raise Exception("Invalid response")



random = random_jokes()
print(random)
# def write_in_excel(data):
#     wb = Workbook()
#     ws = wb.active
#     ws.append(['content', 'categories',])
#
#     for item in data:
#         ws.append([item['content'],item['categories']])
#     wb.save("random_jokes.xlsx")
#
#
# def first():
#     data = random_jokes()
#     write_in_excel(data)
#     print("Data written to random_jokes.xlsx")
#
# if __name__ == '__main__':
#     first()
#
