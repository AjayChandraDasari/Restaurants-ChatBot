from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals
from operator import itemgetter

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import pandas as pd
from city_search import check_city

def price_range(resto):
    if resto['pricefor2_people'] <300 :
        return 'Lesser than 300'
    elif 300 <= resto['pricefor2_people'] <700 :
        return 'Rs 300 to 700'
    else:
        return 'More than 700'

def results(loc,cuisine,price):
        config={ "user_key":"7ca0bfd52de5ad3d67707dfcb2c0851c"}
        zomato = zomatopy.initialize_app(config)
        location_detail=zomato.get_location(loc, 1)
        location_json = json.loads(location_detail)
        location_results = len(location_json['location_suggestions'])
        lat=location_json["location_suggestions"][0]["latitude"]
        lon=location_json["location_suggestions"][0]["longitude"]
        city_id=location_json["location_suggestions"][0]["city_id"]
        cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
        d = []
        df = pd.DataFrame()
        results = zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)), 11)
        d1 = json.loads(results)
        d = d1['restaurants']
        df1 = pd.DataFrame([{'restaurant_name': resto['restaurant']['name'], 'restaurant_rating': resto['restaurant']['user_rating']['aggregate_rating'],'restaurant_address': resto['restaurant']['location']['address'],'pricefor2_people': resto['restaurant']['average_cost_for_two']} for resto in d])
        df = df.append(df1)
        
        df['budget'] = df.apply(lambda x: price_range(x),axis=1)
        restaurant_df = df[(df.budget == price)]
        restaurant_df = restaurant_df.sort_values(['restaurant_rating'], ascending=0)
        return restaurant_df
