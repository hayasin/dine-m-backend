from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env.

import os 
from supabase import create_client as supabase_create_client, Client

def initialize_supabase_client():
    url = os.environ.get("SUPABASE_URL")
    key = os.environ.get("SUPABASE_KEY")
    return supabase_create_client(url, key)





# url : str = os.environ.get("SUPABASE_URL")
# key: str = os.environ.get("SUPABASE_KEY")

# supabase: Client = create_client(url, key)


# data, count = supabase.table('phone_numbers').insert({"phone": "abcdefg"}).execute()
# print(data, count)
# print()
# print()

# response = supabase.table('phone_numbers').select("*").execute()
# print(response)