"""Restaurant rating lister."""

# put your code here

restaurant_ratings = {}

def restaurant_input():
    
    input_restaurant = input("Enter a restaurant: ")
    input_rating = input("Enter restaurants rating: ")
    restaurant_ratings[input_restaurant] = input_rating   


def reading_ratings():
    file = open("scores.txt")
    for line in file:
        line = line.strip()
        sentences = line.split(":")
        name = sentences[0]
        rating = sentences[1]  

        restaurant_ratings[name] = rating  


def organize_ratings():
    sorted_dic = sorted(restaurant_ratings.items())
    for names, scores in sorted_dic: 
        print(f"{names} is rated at {scores}")
        


     
restaurant_input()
reading_ratings()
organize_ratings()

        

