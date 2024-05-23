from dining import api_call, get_menu
from DiningHall import DiningHall
from create_client import initialize_supabase_client
from sms import send_mms_via_email, send_sms_via_email
from emailing import send_email
from dotenv import load_dotenv
import random
import time
import os
from datetime import date


load_dotenv()

response_data = api_call()

def update():
    response_data = api_call()
    if response_data is None:
        # dont update
        return

    #! GET THE DATE
    global dining_halls
    dining_halls = {
        "Bursley": DiningHall("Burlsey Dining Hall", str(date.today()), response_data=response_data),
        "East Quad": DiningHall(
            "East Quad Dining Hall", str(date.today()), response_data=response_data
        ),
        "Markley": DiningHall("Markley Dining Hall", date.today(), response_data=response_data),
        "Mosher-Jordan": DiningHall(
            "Mosher-Jordan Hall", str(date.today()), response_data=response_data
        ),
        "North Quad": DiningHall(
            "North Quad Dining Hall", str(date.today()), response_data=response_data
        ),
        "South Quad": DiningHall(
            "South Quad Dining Hall", str(date.today()), response_data=response_data
        ),
        "Twigs": DiningHall("Twigs At Oxford", str(date.today()), response_data=response_data),
    }


def string_parse(input_string):
    dining_halls_list = input_string.split(", ")
    return dining_halls_list


update()

# ? SUPABASE
supabase = initialize_supabase_client()
response = supabase.table("client_info").select("*").execute()
sender_credentials = (os.environ.get("GMAIL"), os.environ.get("GMAIL_PASSWORD"))

def send_data_to_users(meal):
    for row in response.data:
        receiver_email = str(row["email"]).strip()
        dining_hall_selected = row["dining_preferences"]
        dining_list = string_parse(dining_hall_selected)
        print(dining_list)
        for dining_hall in dining_list:
            subject = dining_hall + " " + meal
            meal_info = dining_halls[dining_hall].get_meal(meal)
            if not meal_info:
                dining_message = dining_hall + " is currently closed"
            else:
                dining_message = "\n" + meal_info

            send_email(subject, dining_message, receiver_email)

send_data_to_users("Lunch")

