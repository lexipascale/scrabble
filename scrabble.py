letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#combines the lists letters and points
letters_to_points = {key:value for key, value in zip(letters, points)}

#adds blank tiles and score
letters_to_points[' '] = 0

#creates a function that will return the total points for a word
def score_word(word):
  point_total = 0
  for letter in word:
    point_total += letters_to_points.get(letter, 0)
  return point_total

#tests the function for the correct output
brownie_points = score_word('BROWNIE')
print(brownie_points)

#Creates a dictionary for each player and their word choices
player_to_words ={'Sophia':['ZOO', 'SOCCER', 'BUBBLES'], 'Madison':['PINK', 'SANTA', 'BARBIE'], 'Lexi':['FLOWER', 'BOOK', 'PUPPY']}

player_to_points = {}
#Adds word score for each player and adds them to a dictionary
for player, words in player_to_words.items():
  player_points = 0
  for word in words:
    player_points += score_word(word)
    player_to_points[player] = player_points

print(player_to_points)




