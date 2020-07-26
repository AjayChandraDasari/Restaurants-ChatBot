## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search

## interactive_story_2
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_price
* restaurant_search{"price": "more than 700"}
    - slot{"price": "more than 700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad", "price": "More than 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "sandeepmidde@gmail.com"}
    - slot{"email": "sandeepmidde@gmail.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad", "price": "More than 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_need_mail
* affirm{"affirm": "Y"}
    - utter_ask_mail
* restaurant_search{"email": "sandeepmidde@gmail.com"}
    - slot{"email": "sandeepmidde@gmail.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad", "price": "More than 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_need_mail
* affirm{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "Hyderabad", "price": "More than 700"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Hyderabad"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "Hyderabad"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - utter_ask_need_mail
* affirm{"deny": "No"}
    - utter_goodbye
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Srinagar"}
    - slot{"location": "Srinagar"}
    - action_check_city
    - slot{"location": "Srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Srinagar"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "sandeepmidde@gmail.com"}
    - slot{"email": "sandeepmidde@gmail.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Thrissur"}
    - slot{"location": "Thrissur"}
    - action_check_city
    - slot{"location": "Thrissur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Thrissur"}
    - utter_ask_need_mail
* negation{"deny": "no"}
    - utter_goodbye 

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian", "location": "adascsc"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "adascsc"}
    - action_check_city
    - slot{"location": null}
    - slot{"location_found": "We do not operate in that area yet"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": null}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* affirm{"email": "abcd@adsa.com"}
    - slot{"email": "abcd@adsa.com"}
    - action_send_mail

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - action_check_city
    - slot{"location": "Jaipur"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - utter_ask_need_mail
* negation{"deny": "no"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Salem"}
    - slot{"location": "Salem"}
    - action_check_city
    - slot{"location": "Salem"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Salem"}
    - utter_ask_need_mail
* negation{"deny": "no"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Guntur"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Guntur"}
    - action_check_city
    - slot{"location": "Guntur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Guntur"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Noida"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Noida"}
    - action_check_city
    - slot{"location": "Noida"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "Shimla"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "Shimla"}
    - action_check_city
    - slot{"location": "Shimla"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Shimla"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail


## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Guntur"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Guntur"}
    - action_check_city
    - slot{"location": "Guntur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Guntur"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Noida"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Noida"}
    - action_check_city
    - slot{"location": "Noida"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail
    
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Shimla"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Shimla"}
    - action_check_city
    - slot{"location": "Shimla"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Shimla"}
    - utter_ask_need_mail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - slot{"email": "akjdk.121.ekjdnc@asj.edu.in"}
    - action_send_mail

## interactive_story_1
* restaurant_search{"location": "Mangalore", "cuisine": "south indian", "price": "Rs 300 to 700", "email": "asdb@asdasd.com"}
    - slot{"cuisine": "south indian"}
    - slot{"email": "asdb@asdasd.com"}
    - slot{"location": "Mangalore"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_city
    - slot{"location": "Mangalore"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"location": "patna", "cuisine": "south indian", "price": "Rs 300 to 700", "email": "asdb@asdasd.com"}
    - slot{"cuisine": "south indian"}
    - slot{"email": "asdb@asdasd.com"}
    - slot{"location": "patna"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_city
    - slot{"location": "patna"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "patna"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"location": "Vadodara", "cuisine": "south indian", "price": "Rs 300 to 700", "email": "asdb@asdasd.com"}
    - slot{"cuisine": "south indian"}
    - slot{"email": "asdb@asdasd.com"}
    - slot{"location": "Vadodara"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_city
    - slot{"location": "Vadodara"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - utter_ask_need_mail
* affirm
    - action_send_mail
    
## interactive_story_1
* restaurant_search{"location": "Ujjain", "cuisine": "south indian", "price": "Rs 300 to 700", "email": "asdb@asdasd.com"}
    - slot{"cuisine": "south indian"}
    - slot{"email": "asdb@asdasd.com"}
    - slot{"location": "Ujjain"}
    - slot{"price": "Rs 300 to 700"}
    - action_check_city
    - slot{"location": "Ujjain"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "Ujjain"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "price": "More than 700", "email": "asdasd@asdasd.com", "location": "rajkot"}
    - slot{"cuisine": "South Indian"}
    - slot{"email": "asdasd@asdasd.com"}
    - slot{"location": "rajkot"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "rajkot"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "rajkot"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "price": "More than 700", "email": "asdasd@asdasd.com", "location": "nagpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"email": "asdasd@asdasd.com"}
    - slot{"location": "nagpur"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "nagpur"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "nagpur"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "price": "More than 700", "email": "asdasd@asdasd.com", "location": "bhopal"}
    - slot{"cuisine": "South Indian"}
    - slot{"email": "asdasd@asdasd.com"}
    - slot{"location": "bhopal"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "bhopal"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "bhopal"}
    - utter_ask_need_mail
* affirm
    - action_send_mail


## interactive_story_1
* restaurant_search{"cuisine": "South Indian", "price": "More than 700", "email": "asdasd@asdasd.com", "location": "mysore"}
    - slot{"cuisine": "South Indian"}
    - slot{"email": "asdasd@asdasd.com"}
    - slot{"location": "mysore"}
    - slot{"price": "More than 700"}
    - action_check_city
    - slot{"location": "mysore"}
    - slot{"location_found": "found"}
    - action_search_restaurants
    - slot{"location": "mysore"}
    - utter_ask_need_mail
* affirm
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - action_check_city
    - slot{"location": "kolkata"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 300"}
    - slot{"price": "Lesser than 300"}
    - action_search_restaurants
    - slot{"location": "kolkata"}
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail


## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "tirupati"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 300"}
    - slot{"price": "Lesser than 300"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kochi"}
    - action_check_city
    - slot{"location": "kochi"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 300"}
    - slot{"price": "Lesser than 300"}
    - action_search_restaurants
    - slot{"location": "kochi"}
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "location": "kannur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kannur"}
    - action_check_city
    - slot{"location": "kannur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Lesser than 300"}
    - slot{"price": "Lesser than 300"}
    - action_search_restaurants
    - slot{"location": "kannur"}
* affirm
    - utter_ask_mail
* restaurant_search{"email": "abc@yah.com"}
    - slot{"email": "abc@yah.com"}
    - action_send_mail

## interactive_story_1
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - action_check_city
    - slot{"location": "Mumbai"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Firozabad"}
    - slot{"location": "Firozabad"}
    - action_check_city
    - slot{"location": "Firozabad"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Firozabad"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - action_check_city
    - slot{"location": "Jabalpur"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jabalpur"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - action_check_city
    - slot{"location": "Ahmedabad"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Kollam"}
    - slot{"location": "Kollam"}
    - action_check_city
    - slot{"location": "Kollam"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Kollam"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Jhansi"}
    - slot{"location": "Jhansi"}
    - action_check_city
    - slot{"location": "Jhansi"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jhansi"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "Gulbarga"}
    - slot{"location": "Gulbarga"}
    - action_check_city
    - slot{"location": "Gulbarga"}
    - slot{"location_found": "found"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Gulbarga"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"location": "tirupati"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "tirupati"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_check_city
    - slot{"location": "srinagar"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "srinagar"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_location
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - action_check_city
    - slot{"location": "Jammu"}
    - slot{"location_found": "found"}
    - utter_ask_price
* restaurant_search{"price": "Rs 300 to 700"}
    - slot{"price": "Rs 300 to 700"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - utter_ask_need_mail
* negation{"deny": "No"}
    - utter_goodbye
