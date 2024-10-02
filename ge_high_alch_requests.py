import requests

# Function to get item data
def get_item_data(item_id):
    url = f"https://services.runescape.com/m=itemdb_rs/api/catalogue/detail.json?item={item_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# List of item IDs you want to check (you can expand this list)
item_ids = [4151, 5698, 1712]  # Example item IDs, replace with actual IDs you're interested in

# Loop through the items
for item_id in item_ids:
    item_data = get_item_data(item_id)
    if item_data:
        item_name = item_data['item']['name']
        ge_price = item_data['item']['current']['price']
        high_alch_value = item_data['item']['high_alch']  # You need to get this from another source if not in the response

        if high_alch_value > ge_price:
            print(f"Item: {item_name}, GE Price: {ge_price}, High Alch Value: {high_alch_value}, Profit: {high_alch_value - ge_price}")
