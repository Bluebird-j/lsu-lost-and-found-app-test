from Core.database import supabase
from datetime import datetime

def get_all_items():
    response = supabase.table("items").select("*").execute()
    print("GET ALL RESPONSE:", response.data)  # just to debug
    return response.data

def get_item_by_id(item_id):
    response = supabase.table("items").select("*").eq("id", item_id).execute()
    print("DEBUG:", response)
    return response.data

def create_item(item_data):

    item_data.setdefault("status", "active")
    item_data.setdefault("created_at", datetime.utcnow().isoformat())

    response = supabase.table("items").insert(item_data).execute()
    print("DEBUG: create_item response:", response)
    return response.data

def update_item(item_id, item_data):
    # Remove any keys that are empty or None
    clean_data = {k: v for k, v in item_data.items() if v not in [None, ""]}
    response = supabase.table("items").update(clean_data).eq("id", item_id).execute()
    print("DEBUG: update_item response:", response)
    return response.data

def delete_item(item_id):
    response = supabase.table("items").delete().eq("id", item_id).execute()
    print("DEBUG: delete_item response:", response)
    return response.data
