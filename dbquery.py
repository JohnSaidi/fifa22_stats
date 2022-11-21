from cs50 import SQL


db = SQL("sqlite:///fifa22data.db")

def get_all_playernames():
    return db.execute("SELECT short_name, long_name, club_joined, club_name, overall, player_face_url FROM fifa22data")

def get_info_by_playername(playername):
    return db.execute("SELECT * FROM fifa22data WHERE short_name = :short_name", short_name=playername)

def get_players_by_teamName(team_name):
    return db.execute(f"SELECT * FROM fifa22data WHERE club_name = '{team_name}'")

#filter players by team and player names
def get_players_by_tName_pName(team_name, playername):
    return db.execute(f"SELECT * FROM fifa22data WHERE club_name = '{team_name}'AND short_name= '{playername}'")

#filter players by club_name and nationality_name
def get_players_by_clubName_nationality(clubname, nationality):
    return db.execute(f"SELECT * FROM fifa22data WHERE club_name = '{clubname}'AND nationality_name= '{nationality}'")

def get_all_nation_names():
    return db.execute("SELECT DISTINCT nationality_name FROM fifa22data ORDER BY nationality_name ASC")


def get_players_by_nationalTeam(team_name):
    return db.execute(f"SELECT * FROM fifa22data WHERE nationality_name = '{team_name}'")

def get_player_stats(playername):
    return db.execute(f"SELECT short_name, pace, shooting, passing, dribbling, defending, physic FROM fifa22data WHERE short_name = '{playername}'")

# def get_stats_by_playername(playername):
#     return db.execute("SELECT short_name, overall, pace, shooting, passing, }dribbling, defending, physic  FROM fifa22data WHERE short_name = :short_name", short_name=playername)

# def get_playernames_by_clubTeamn(clubTeam):
#     return db.execute("SELECT short_name FROM fifa22data WHERE club_name = :club_name", club_name=clubTeam)

# def get_playernames_by_nationalTeam(nationalTeam):
#     return db.execute("SELECT short_name FROM fifa22data WHERE nationality_name = :nationality_name", nationality_name=nationalTeam)




