# services/item_service.py
from mock_db import ITEMS

def get_items():
    return ITEMS

def get_item(item_id):
    return next((item for item in ITEMS if item["id"] == item_id), None)

def create_item(name):
    new_item = {"id": len(ITEMS) + 1, "name": name}
    ITEMS.append(new_item)
    return new_item

def update_item(item_id, name):
    item = get_item(item_id)
    if item:
        item["name"] = name
        return item
    return None

def delete_item(item_id):
    global ITEMS
    ITEMS = [item for item in ITEMS if item["id"] != item_id]
    return True
