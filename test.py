from account import Account
from dining import api_call, get_menu
from DiningHall import DiningHall
from create_client import initialize_supabase_client
from sms import send_mms_via_email

date = "2024-05-02"
meal = "BREAKFAST"
dining_hall = "South Quad Dining Hall"

response_data = api_call()
dining_halls = None

def update(): 
    response_data = api_call(); 
    if response_data is None: 
        # dont update 
        return
    
    #! GET THE DATE
    
    global dining_halls
    dining_halls = {"Bursley" : DiningHall("Burlsey Dining Hall", date, response_data=response_data), 
                "East Quad" : DiningHall("East Quad Dining Hall", date,response_data=response_data),
                "Markley" : DiningHall("Markley Dining Hall", date,response_data=response_data),
                "Mosher-Jordan" : DiningHall("Mosher-Jordan Hall", date,response_data=response_data),
                "North Quad" : DiningHall("North Quad Dining Hall", date,response_data=response_data),
                "South Quad" : DiningHall("South Quad Dining Hall", date,response_data=response_data),
                "Twigs" : DiningHall("Twigs At Oxford", date, response_data=response_data),
                }


def string_parse(input_string):
    dining_halls_list = input_string.split(", ")
    return dining_halls_list

update()

#? SUPABASE
supabase = initialize_supabase_client()
response = supabase.table("phone_numbers").select("*").execute()
sender_credentials = ("yasin.hasan4242@gmail.com", "lkgfhljffdhajdby") #MOVE TO .END FILE

for row in response.data:
    phone_number = str(row['phone'])
    dining_hall_selected = row['dining_halls']
    provider = row['provider']
    dining_list = string_parse(dining_hall_selected)
    
    print(phone_number)
    for dining_hall in dining_list:
        dining_message = dining_halls[dining_hall].get_breakfast() #change for get_lunch()
        # print("START OF MESSAGE")
        # print(dining_hall)
        # print(dining_message)
        # print("END OF MESSAGE")
        # print()
        # print()
        
        # subject = str(dining_hall).strip()
        # print(f"Sending message with subject: {subject}")
        
        send_mms_via_email(phone_number, dining_message, provider, sender_credentials, "TEST")
        # send_mms_via_email(phone_number, dining_message, provider, sender_credentials, dining_hall)
        # print("SENT MESSAGE")
        # print()