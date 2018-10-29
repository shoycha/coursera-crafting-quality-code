from collections import *

"""
name_to_rating = {'Georgie Porgie': 87,
'Queen St. Cafe': 82,
'Dumplings R Us': 71,
'Mexican Grill': 85,
'Deep Fried Everything': 52}

price_to_names = {'$': ['Queen St. Cafe', 'Dumplings R Us', 'Deep Fried Everything'],
'$$': ['Mexican Grill'],
'$$$': ['Georgie Porgie'],
'$$$$': []}

cuisine_to_name = {'Canadian': ['Georgie Porgie'],
'Pub Food': ['Georgie Porgie', Deep Fried Everything'],
'Malaysian': ['Queen St. Cafe'],
'Thai': ['Queen St. Cafe'],
'Chinese': ['Dumplings R Us'],
'Mexican': ['Mexican Grill']}

"""
FILENAME = 'restaurants_small.txt'

def recommend(file, price, cuisines_list):
    """
 (file open for reading, str, list of str) -> list of [int, str] list

Find restaurants in file that are priced according to price and that are tagged with any of the items in cuisines_list. 
Return a list of lists of the form [rating%, restaurant name], sorted by rating%.
    """
    name_to_rating, price_to_names, cuisine_to_names = read_restaurant(file)
    recommendation_list = []
    names_matching_price = price_to_names[price]
    names_final = filter_by_cuisine(names_matching_price,cuisine_to_names, cuisines_list)
    result = build_rating_list(name_to_rating, names_final)
    
    return result

def filter_by_cuisine(names_matching_price,cuisine_to_names, cuisines_list):
    names_final = []
    for c in cuisines_list:
        names_final.extend(list(set(cuisine_to_names[c]).intersection(names_matching_price)))
    return names_final

def read_restaurant(file):

    name_to_rating = {}
    price_to_names = {'$': [], '$$': [], '$$$': [], '$$$$': []}
    cuisine_to_names = defaultdict(list)

    contents = open(file, "r").readlines()
    for i in range(0,len(contents), 5):
    
        name_to_rating[contents[i].rstrip()] = int(contents[i+1].rstrip().rstrip('%'))
        price_to_names[contents[i+2].rstrip()].append(contents[i].rstrip())
        list_cuisines = contents[i+3].rstrip().split(',')
    
        for each in list_cuisines:
            cuisine_to_names[each].append(contents[i].rstrip())
    
    return name_to_rating, price_to_names, cuisine_to_names

def build_rating_list(name_to_rating, names_final):
    recommendation_list = []
    for n in names_final:    
        recommendation_list.append([name_to_rating[n], n])
        recommendation_list.sort(reverse=True)

    return recommendation_list




        
        
