import requests
import json
import pandas as pd


# url = "https://webws.365scores.com/web/game/stats/?appTypeId=5&langId=&timezoneName=Asia/Riyadh&userCountryId=22&games=4522760&lastUpdateId=5400607635"

# payload = {}
# headers = {
#   'User-Agent': 'Mozilla/5.0 (Windows NT 0.0; Win64; x64; rv:43.0) Gecko/20000 Firefox/43.0',
#   'Accept': '*/*',
#   'Accept-Language': 'en-US,en;q=0.5',
#   'Accept-Encoding': 'gzip, deflate, br, zstd',
#   'Referer': 'https://www.365scores.com/',
#   'Origin': 'https://www.365scores.com',
#   'Connection': 'keep-alive',
#   'Sec-Fetch-Dest': 'empty',
#   'Sec-Fetch-Mode': 'cors',
#   'Sec-Fetch-Site': 'same-site',
#   'Priority': 'u=4',
#   'TE': 'trailers'
# }
# r= requests.get( url, headers=headers)
# dd=r.json()
# df = pd.json_normalize(dd['statistics'],sep="_")
# df.to_csv('iti3.csv',index=False)
df = pd.read_csv(r'C:\Users\hb\Desktop\PD\iti3.csv')
# #---------------------------------------------------






P_ossession = df.loc[df['id'] == 10] # Possession
P_o_ssession = (P_ossession.iloc[1,4]).replace('%','')
Possession = float(P_o_ssession)


egg = df.loc[df['id'] == 76] # Expected Goals
eg = float(egg.iloc[1,4]) 
expected_goals = eg

tss = df.loc[df['id'] == 3] # Total Shots
ts = int(tss.iloc[1,4])
Total_Shots = ts

sott = df.loc[df['id'] == 4] # Shots On Target
sot = int(sott.iloc[1,4])
Shots_On_Target = sot

bc =df.loc[df['id'] == 24] # Big Chances Created
bcc = int(bc.iloc[1,4])
Big_Chances_Created = bcc

cr=df.loc[df['id'] == 8] # Corners
cor = int(cr.iloc[1,4])
Corners = cor

pac = df.loc[df['id'] == 19] # Passes Completed 
pc = int(pac.iloc[1,4])
Passes_Completed = pc

at = df.loc[df['id'] == 11] # Attacks
att = int(at.iloc[1,4])
Attacks = att

hiw = df.loc[df['id'] == 25] # Hit Woodwork
hw = int(hiw.iloc[1,4])
Hit_Woodwork = hw

ex = df.loc[df['id'] == 79] # Expected Goals On Target
egot = float(ex.iloc[1,4])
Expected_Goals_On_Target = egot

sh = df.loc[df['id'] == 46] # Shots Inside The Box
sitb = int(sh.iloc[1,4])
Shots_Inside_The_Box = sitb

so = df.loc[df['id'] == 147] # Shots Outside The Box
sob = int(so.iloc[1,4])
Shots_Outside_Box = sob


# bc = df.loc[df['id'] == 36] # Big Chances Misse
# bcm = int(bc.iloc[1,4])
# Big_Chances_Missed = bcm

exa = df.loc[df['id'] == 78] # Expected Assists
ea = float(exa.iloc[1,4])
Expected_Assists = ea

po = df.loc[df['id'] == 148] # Passes Own Half
poh = int(po.iloc[1,4])
Passes_Own_Half = poh

pooh = df.loc[df['id'] == 149] # Passes Opposition Half
pph = int(pooh.iloc[1,4])
Passes_Opposition_Half = pph
  
kpp = df.loc[df['id'] == 46] # Key Passes
kp = int(kpp.iloc[1,4])
Key_Passes = kp

pi = df.loc[df['id'] == 80] # Passes Into Final Third
pift = int(pi.iloc[1,4])
Passes_Into_Final_Third = pift

i_nn = df.loc[df['id'] == 40] # Interceptions
i_n = int(i_nn.iloc[1,4])
Interceptions = i_n

e_g = df.loc[df['id'] == 77] # Expected Goals Conceded
egc = float(e_g.iloc[1,4])
Expected_Goals_Conceded = egc

gos = df.loc[df['id'] == 23] # Goalkeeper Saves
gs = int(gos.iloc[1,4])
Goalkeeper_Saves = gs

cl = df.loc[df['id'] == 40] # Clearances
c_l = int(cl.iloc[1,4])
Clearances = c_l

# erlg = df.loc[df['id'] == 66] # Error Led To Goal
# erg = int(erlg.iloc[1,4])
# Error_Led_To_Goal = erg

dww = df.loc[df['id'] == 150] # Duels Won
dw = int(dww.iloc[1,4])
Duels_Won = dw


wd = df.loc[df['id'] == 60] # Was Dribbled Past
wdp = int(wd.iloc[1,4])
Was_Dribbled_Past = wdp

ftw = df.loc[df['id'] == 84] # Final Third Possession Won
ftpw = int(ftw.iloc[1,4]) 
Final_Third_Possession_Won = ftpw

pp = df.loc[df['id'] == 73] # Possession Lost
pl = int(pp.iloc[1,4]) 
Possession_Lost = pl

ycs = df.loc[df['id'] == 1] # Yellow Cards
yc = int(ycs.iloc[1,4])
yellow_cards = yc

rcs = df.loc[df['id'] == 2] # Red Cards
rc = int(rcs.iloc[1,4])
red_cards = rc
