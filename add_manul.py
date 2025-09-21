import mysql.connector

def add__manul(round_number,match_name,match_date,
               home_away,match_result,referee,gf,ga,
               actual,crosses_completed,long_passes_completed,tackles_won,
               aerial_duels_won,ground_duels_won,successful_dribbles,
               headed_goals,penalty_goals,free_kick_goals,
               set_piece_goals,hat_trick,super_hat_trick,referee_rating,best_player):

    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "itt_league_2025_2026"
    )

    mycursor = db.cursor()

    mycursor.execute("INSERT INTO itt (round_number,match_name,match_date," \
    "home_away,match_result,referee,gf,ga,actual,crosses_completed,long_passes_completed,tackles_won," \
    "aerial_duels_won,ground_duels_won,successful_dribbles," \
    "headed_goals,penalty_goals," \
    "free_kick_goals,set_piece_goals," \
    "hat_trick,super_hat_trick,referee_rating,best_player) VALUES"

    " (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",

                      (round_number,match_name,match_date,
                        home_away,match_result,
                        referee,gf,ga,actual,crosses_completed,
                        long_passes_completed,tackles_won,
                        aerial_duels_won,ground_duels_won,
                        successful_dribbles,
                        headed_goals,penalty_goals,
                        free_kick_goals,set_piece_goals,
                        hat_trick,super_hat_trick,referee_rating,best_player,))
    db.commit() 

add__manul(3,'AL-Ittihad vs AL-Najma','2025-09-20','A','W','Mohammed Al Haoaish',
           1,0,57,5,24,13,12,37,11,0,0,0,0,0,0,6.0,'kante')










