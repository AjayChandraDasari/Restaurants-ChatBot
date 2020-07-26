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
from Email import send_mail
from filtered_restaurants import results

class ActionSearchRestaurants(Action):
    def name(self):
        return 'action_search_restaurants'
        
    def run(self, dispatcher, tracker, domain):
        config={ "user_key":"7ca0bfd52de5ad3d67707dfcb2c0851c"}
        zomato = zomatopy.initialize_app(config)
        loc = tracker.get_slot('location')
        cuisine = tracker.get_slot('cuisine')
        price = tracker.get_slot('price')
        customer_email = tracker.get_slot('email')
        location_detail=zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        global lat, lon, cusines_dict
        lat=d1["location_suggestions"][0]["latitude"]
        lon=d1["location_suggestions"][0]["longitude"]
        cuisines_dict={'american': 1,'chinese': 25, 'north indian': 50, 'italian': 55, 'mexican': 73, 'south indian': 85}
        
        global restaurants


        restaurants = results(loc, cuisine, price)
        topfive = restaurants.head(5)
        response=""
        if len(topfive) == 0:
            response= "no results"
        else:
                     for index, x in topfive.iterrows():
                            response=response+ "Found "+ x['restaurant_name']+ " in "+ x['restaurant_address']+ " has been rated "+ x['restaurant_rating']+"\n"
        dispatcher.utter_message("-----"+(response))
        return [SlotSet('location',loc)]
    
class send_email(Action):
        def name(self):
                return 'action_send_mail'

        def run(self, dispatcher, tracker, domain):
                customer_email = tracker.get_slot('email')
                loc = tracker.get_slot('location')
                cuisine = tracker.get_slot('cuisine')
                price = tracker.get_slot('price')
                restaurants = results(loc, cuisine, price)
                details = restaurants.head(10)
                #details = details[['restaurant_name','restaurant_address','restaurant_rating']]
                response = ""
                for index, x in details.iterrows():
                        response=response+ "Restaurant: " + x['restaurant_name']+ "    Address: "+ x['restaurant_address']+ "    Budget: "+ str(x['pricefor2_people'])+"    Rating: "+ x['restaurant_rating']+"\n"
                send_mail(customer_email,response)
                dispatcher.utter_message('Have a great day!')


class check_location(Action):
    def name(self):
        return 'action_check_city'
        
    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')
        check = check_city(loc)
        
        return [SlotSet('location',check['location_new']), SlotSet('location_found',check['location_found'])]