import fetch_data
import mysql.connector

def update_colmns():

    db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "itt_league_2025_2026"
    )

    mycursor = db.cursor()

    mycursor.execute("UPDATE itt SET possession=%s,expected_goals=%s,total_shots=%s,shots_on_target=%s," \
    "big_chances_created=%s,corners=%s,passes_completed=%s,attacks=%s,hit_woodwork=%s," \
    "expected_Goals_on_target=%s,shots_inside_the_box=%s,shots_outside_the_box=%s," \
    "expected_assists=%s,passes_own_half=%s,passes_opposition_half=%s," \
    "key_passes=%s,passes_into_final_third=%s,interceptions=%s," \
    "expected_goals_conceded=%s,goalkeeper_saves=%s,clearances=%s," \
    "duels_won=%s,was_dribbled_past=%s," \
    "final_third_possession_won=%s,possession_lost=%s,red_cards=%s,yellow_cards=%s WHERE round_number=3",
                     
                    (fetch_data.Possession,fetch_data.expected_goals,fetch_data.Total_Shots,
                     fetch_data.Shots_On_Target,fetch_data.Big_Chances_Created,
                     fetch_data.Corners,fetch_data.Passes_Completed,fetch_data.Attacks,
                     fetch_data.Hit_Woodwork,fetch_data.Expected_Goals_On_Target,fetch_data.Shots_Inside_The_Box,
                     fetch_data.Shots_Outside_Box,fetch_data.Expected_Assists,
                     fetch_data.Passes_Own_Half,fetch_data.Passes_Opposition_Half,
                     fetch_data.Key_Passes,fetch_data.Passes_Into_Final_Third,fetch_data.Interceptions,
                     fetch_data.Expected_Goals_Conceded,fetch_data.Goalkeeper_Saves,
                     fetch_data.Clearances,
                     fetch_data.Duels_Won,fetch_data.Was_Dribbled_Past,fetch_data.Final_Third_Possession_Won,
                     fetch_data.Possession_Lost,fetch_data.red_cards,fetch_data.yellow_cards,))
    db.commit() 

update_colmns()