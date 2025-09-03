CREATE DATABASE itt_league_2025_2026;

USE itt_league_2025_2026;
CREATE TABLE itt(
round_number INT PRIMARY KEY,
match_name VARCHAR(50),
match_date DATE,
home_away VARCHAR(1),
match_result VARCHAR(1),
referee VARCHAR(50),
gf INT,
ga INT,
actual INT,
possession DECIMAL(5,2),
expected_goals FLOAT,
total_shots INT,
shots_on_target INT,
big_chances_created INT,
corners INT,
passes_completed INT,
attacks INT,
hit_woodwork INT,
expected_Goals_on_target FLOAT,
shots_inside_the_box INT,
shots_outside_the_box INT,
big_chances_missed INT,
expected_assists FLOAT,
crosses_completed INT,
passes_own_half INT,
passes_opposition_half INT,
long_passes_completed INT,
key_passes INT,
passes_into_final_third INT,
interceptions INT,
expected_goals_conceded FLOAT,
goalkeeper_saves INT,
tackles_won INT,
clearances INT,
error_led_to_goal INT,
duels_won INT,
aerial_duels_won INT,
ground_duels_won INT,
successful_dribbles INT,
was_dribbled_past INT,
final_third_possession_won INT,
possession_lost INT,
red_cards INT,
yellow_cards INT,
headed_goals INT,
penalty_goals INT,
free_kick_goals INT,
set_piece_goals INT,
hat_trick BOOLEAN,
super_hat_trick BOOLEAN,
referee_rating DECIMAL(3,1),
best_player VARCHAR(50)
);

USE itt_league_2025_2026;
INSERT INTO itt
VALUES
(1,'Al-Aittihad vs Al-Akhdoud','2025-08-30','A','W','Mohammed Al Haoaish',
5,2,56,67.00,2.4,16,10,5,7,608,83,0,2.94,12,4,4,2.7,3,331,332,26,12,128,
5,0.74,1,9,12,0,35,9,26,7,13,8,84,0,1,1,0,1,1,TRUE,FALSE,9.0,'K-Benzema'
);









