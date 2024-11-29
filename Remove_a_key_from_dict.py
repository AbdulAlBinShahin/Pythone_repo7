My_Dict = { 'name': 'Ayon', 'age': '22'}
key_to_remove = input("enter the key you want to check: ")
if key_to_remove in My_Dict:
    remove=My_Dict.pop(key_to_remove)
    print(f"The key '{key_to_remove}' remove with value {remove} from the dictionary.")
    print(f"Updated dictionary = {My_Dict}")
else:
    print(f"The key '{key_to_remove}' does not exists in the dictionary.")
