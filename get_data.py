import requests

def get_from_web():
    pages = []
    for i in range(1,4):
        url = 'https://shopicruit.myshopify.com/admin/orders.json?page=' + str(i) +'&access_token=c32313df0d0ef512ca64d5b336a0d7c6'
        content = requests.get(url)
        content = content.json()
        pages.append(content)
        #print(content)

    return pages

def get_total_values(pages):
    total_paid = 0
    total_tax = 0

    for i in pages:
        for j in i['orders']:
            total_paid += float(j['total_price'])
            total_tax += float(j['total_tax'])
            #print(str(total_paid))

    return (total_paid+total_tax, round(total_paid,2), total_tax)


pages = get_from_web()
values = get_total_values(pages)

print('TOTAL REVENUE: $', values[1])

