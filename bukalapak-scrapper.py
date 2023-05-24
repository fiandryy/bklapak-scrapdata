import requests
import csv

url = 'https://api.bukalapak.com/multistrategy-products'
params = {
'keywords': 'tablet',
'limit': 50,
'offset': 50,
'facet': True,
'page': 2,
'shouldUseSeoMultistrategy': False,
'isLoggedIn': False,
'show_search_contexts': True,
'access_token': 'eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjY291bnRzLmp3dC5hY2Nlc3MtdG9rZW4iLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczo'
                'vL2FjY291bnRzLmJ1a2FsYXBhay5jb20vIiwic3ViIjoiMjMxZDRhODY5MDVmMGYyNjJjNWUwM2ZjIiwiYXVkIjpbImh0dHBzOi8vYW'
                'Njb3VudHMuYnVrYWxhcGFrLmNvbSIsImh0dHBzOi8vYXBpLmJ1a2FsYXBhay5jb20iLCJodHRwczovL2FwaS5zZXJ2ZXJtaXRyYS5j'
                'b20iXSwiZXhwIjoxNjg0OTQ0MTc5LCJuYmYiOjE2ODQ5MzM2MTksImlhdCI6MTY4NDkzMzYxOSwianRpIjoibGc3R0djRnkxYXhKY'
                'W5zY1hkaVZydyIsImNsaWVudF9pZCI6IjIzMWQ0YTg2OTA1ZjBmMjYyYzVlMDNmYyIsInNjb3BlIjoicHVibGljIn0.EhabYreUH-'
                '5FIY5_RA3bgv5nPWAfL2GHSUDc6ixXvVPRpX7lGu7e5CXBxplK7mkH1zR5Pb1gLv2Erw4cLSt0-C6yZ1qeeL1lw_vLCPVCXoNpIele'
                'RqOmGLx5-uHfdHpP012_oZId8V0GZc17jVHGGG4YoDV18yBYnP_NdGN4m3j_qDy9kLsqFkea5To3k23ORpHn4HlJALl5JzZV2mNg'
                '4YRnbME6lKRlQM69Dg9IFPvs8S5khwaBXPcKjpVTD9GpIQHDr15uhJE8dDtTabhGZHX19Gu9M_9dGYN6DI22Q_J8Y9g28SzmAo9fKr'
                'C4rxUdbN7iPJ6XCJ2EReB3fRArYQ'
}

r = requests.get(url, params=params).json()

products = r['data']
for p in products:
    name = p['name']
    price = p['price']
    rate = p['rating']
    stock = p['stock']
    url = p['url']

    average_rate = rate.get('average_rate')
    sold = rate.get('user_count')

    print(f'Name: {name}')
    print(f'Price: {price}')
    print(f'Rating: {average_rate}')
    print(f'Qty sold:{sold}')
    print(f'Stock Remaining: {stock}')
    print(f'Url: {url}')





