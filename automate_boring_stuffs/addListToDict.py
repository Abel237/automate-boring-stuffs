# This statement is just an example inventory in the form of a dictionary
inv = {'gold coin': 42, 'rope': 1}
# This statement is an example of a loot in the form of a list
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']


def add_to_inventory(inventory, dragon_loot):

    for loot in dragon_loot:
        # If the item in the list is not in the dictionary, then add it as a key to the dictionary - with a value of 0
        inventory.setdefault(loot, 0)
        # Increment the value of the key by 1
        inventory[loot] = inventory[loot] + 1

    return inventory


def display_inventory(inventory):

    print('Inventory:')
    total_items = 0

    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        total_items = total_items + 1

    print('Total number of items: ' + str(total_items))


# This function call is to add the items in the loot to the inventory
inv = add_to_inventory(inv, dragon_loot)

# This function call will display the modified dictionary in the prescribed format
display_inventory(inv)
