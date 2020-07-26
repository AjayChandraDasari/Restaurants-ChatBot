import zomatopy
import json

city_search = ['Ahmedabad','Bangalore','Chennai','Delhi','Hyderabad','Kolkata','Mumbai','Pune','Agra','Ajmer','Aligarh','Amravati',
             'Amritsar','Asansol','Aurangabad','Bareilly','Belgaum','Bhavnagar','Bhiwandi','Bijapur','Bhopal','Bhubaneswar','Bikaner',
             'Bilaspur','Bhilai','Bokaro Steel City','Chandigarh','Coimbatore','Cuttack','Dehradun','Dhanbad','Durgapur','Erode','Faridabad',
             'Firozabad','Ghaziabad','Gorakhpur','Gulbarga','Guntur','Gurgaon','Guwahati‚ Gwalior','Hubli-Dharwad', 'Hamirpur','Indore','Jabalpur','Jaipur','Jalandhar','Jammu','Jamnagar','Jamshedpur','Jhansi','Jodhpur','Kannur','Kanpur','Kakinada','Kochi','Kottayam','Kolhapur','Kollam','Kozhikode','Kurnool','Lucknow','Ludhiana','Madurai','Malappuram','Mathura','Goa','Mangalore','Meerut','Moradabad','Mysore','Nagpur','Nanded','Nashik','Nellore','Noida','Palakkad','Patna','Perinthalmanna','Pondicherry','Purulia Prayagraj','Raipur','Rajkot','Rajahmundry','Ranchi','Rourkela','Salem','Sangli','Siliguri','Solapur','Srinagar','Shimla','Surat','Thiruvananthapuram','Thrissur','Tiruchirappalli','Tirur','Tirupati''Tirunelveli','Tiruppur','Tiruvannamalai','Ujjain','Vadodara','Varanasi','Vasai-Virar City','Vijayawada','Vellore','Visakhapatnam','Warangal']

city_search = [x.lower() for x in city_search]
def check_city(loc,city_search = city_search):
    if loc.lower() in city_search:
        found = 1
    else:
        found = 0

    if found == 0:
        return {'location_found' : 'We do not operate in that area yet', 'location_new' : None}
    else:
        return {'location_found' : 'found', 'location_new' : loc}
