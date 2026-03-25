Frase = input("write a list separated by commas: ")
List_data= Frase.split(",")
lista_limpia = []
for item in List_data:
    item_clean = item.strip(",.!?;:()[]{}\"'").replace(" ", "").capitalize() # delete spaces and punctuation, and capitalize the first letter
    if item_clean: # check if the cleaned item is not empty
        lista_limpia.append(item_clean) # add the cleaned item to the new list
print (lista_limpia)