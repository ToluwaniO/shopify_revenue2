import requests

def get_from_web():
    '''() -> list of dictionaries
    This method returns all the json pages as a list of dictionaries'''
    pages = []
    for i in range(1,4):
        url = 'https://shopicruit.myshopify.com/admin/orders.json?page=' + str(i) +'&access_token=c32313df0d0ef512ca64d5b336a0d7c6'
        content = requests.get(url)
        content = content.json()
        pages.append(content)
        #print(content)

    return pages

def get_total_values(pages):
    '''(list of dictionaries) -> tuple of floats
    This method takes the list of dictinaries with data and returns a tuple with the total made,
    total paid by customers and total tax by customers'''
    total_paid = 0
    total_tax = 0

    for i in pages:
        for j in i['orders']:
            total_paid += float(j['total_price'])
            total_tax += float(j['total_tax'])

    return (total_paid+total_tax, round(total_paid,2), total_tax)


pages = get_from_web()
values = get_total_values(pages)

print('TOTAL REVENUE: $', values[1])

