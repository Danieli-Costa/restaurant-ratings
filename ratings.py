"""Restaurant rating lister."""

# put your code here

restaurant_ratings = {}



def users_choice():
    while True:
      instructions = """
        (S)ee all the ratings
        (A)dd a new restaurant and rating
        (Q)uit
         """

      print(instructions)

      user_input = input("What do you desire? : ")
      user_input = user_input.upper()

      if user_input == "S":
        reading_ratings()
        organize_ratings()
      elif user_input == "A":
        restaurant_input()
      elif user_input == "Q":
         print("Goodbye!")
         break
          


def restaurant_input():
    
    input_restaurant = input("Enter a restaurant: ")
    input_rating = input("Enter restaurants rating: ")

    # input_rating = int(input_rating)
    digit_check = input_rating.isdigit()
    if digit_check == False:
        input_rating = input("Enter a valid number: ")
    else:
        input_rating = int(input_rating)

        if input_rating > 5:
            input_rating = input("Enter a rating from 1 to 5: ")
     
   
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
        


users_choice()   


        

