# game_score.py

player_name = input("Enter player's name: ")

games_played = int(input("Enter number of games played: "))
total_score = int(input("Enter total score: "))

if games_played == 0:
    average_score = 0
else:
    average_score = total_score / games_played

print("\nPlayer:", player_name)
print("Games Played:", games_played)
print("Total Score:", total_score)
print("Average Score:", format(average_score, ".2f"))