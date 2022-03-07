shopping_list = [
    ("Bib Shorts",          "Clothing",      92.50),
    ("Roubaix",             "Bicycle",     3599.99),
    ("Cycling Computer",    "Accessories",  394.99),
    ("Helmet",              "Accessories",  299.99),
    ("Road Shoes",          "Shoes",        144.99),
    ("700c presta tube",    "Accessories",    5.25),
    ("Jersey",              "Clothing",      25.99),
    ("Multi-Function Tool", "Accessories",   22.99),
    ("Gloves",              "Accessories",    8.99),
    ("Cleats",              "Shoes",         15.99),
    ("Power Pedals",        "Accessories",  999.99),
    ("Socks",               "Clothing",       8.50)
]

import locale
locale.setlocale(locale.LC_ALL, '')

def print_list(shopping):
    ''' Print out the list in a user-friendly way '''
    for item in shopping:
        print(item[0], "costs: ", 
              locale.currency(item[2], grouping=True))
def compute_total_cost(shopping):
    '''compute the total cost of the shopping list'''
    sum = 0
    for item in shopping:
        sum += item[2]
    return sum

def find_min_max(shopping):
    '''find the cheapest and mst expensive'''
    cheapest = None
    most_expensive = None
    for item in shopping:
        if cheapest == None or item[2] < cheapest:
            cheapest = item[2]
        if most_expensive == None or item[2] > most_expensive:
            most_expensive = item[2]

print_list(shopping_list)
print(f'The total cost is: {locale.currency(compute_total_cost(shopping_list), grouping = True)} ')
extremes = find_min_max(shopping_list)
print(f'The cheapest item cost {locale.currency(extremes[0], grouping = True)}')
print(f'The most expensive item cost {locale.currency(extremes[1], grouping = True)}')