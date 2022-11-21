from flask import Flask, render_template, request, url_for, redirect
from dbquery import ( 
    get_info_by_playername, get_players_by_teamName, get_players_by_nationalTeam, 
    get_players_by_tName_pName, get_players_by_clubName_nationality, 
    get_all_playernames, get_all_nation_names, get_player_stats
)



app = Flask(__name__)

# implemet player search by nationality, club name and player profile
@app.route('/', methods=['GET','POST'])
def root():
    all_nations = get_all_nation_names()

    if request.method == "POST":
        teamname = request.form.get('search')
        if all_nations:
            for teams in all_nations:
                if teamname in teams['nationality_name']:
                    return redirect(url_for('player_by_country', nation=teamname))
        else:
            # search database for player names
            player_info = get_info_by_playername(teamname)    
            for players in player_info:
                if teamname in players['short_name']:
                    return redirect(url_for('profile', player=teamname))

 
    return render_template('form.html')


@app.route('/compare-players', methods=['GET', 'POST'])
def comparison():
    if request.method == "POST":
        player1 = request.form.get('p1')
        player2 = request.form.get('p2')
        return redirect(url_for('stats_comparison', player1=player1, player2=player2))
    else:
        return render_template('comparison_form.html')



# returns all players players
@app.route('/playerz')
def allplayers():
    all_players = get_all_playernames()
    # if all_players:
    #     if request.method == "POST":
    #         teamname = request.form['search']
    #         # if teamname["nationality_name"] in all_nations:
    #         return render_template(url_for('profile')) 
    return render_template('playertable.html', p_name=all_players)

@app.route('/player_profile/<clubname>/<playername>/')
def profile(clubname, playername):
    player_info = get_players_by_tName_pName(clubname, playername)
    return render_template('index.html', p_name=player_info)

# All countries
@app.route('/countries')
def allcountries():
    all_nations = get_all_nation_names()
    return render_template('nations.html', p_name=all_nations)

# All Club teams
@app.route('/club-teams')
def allclubteams():
    return render_template('clubteams.html')

# players from the same nation
@app.route('/players/nationality/<nation>')
def player_by_country(nation):
    players = get_players_by_nationalTeam(nation)
    return render_template('playertable.html', p_name=players)

# players from the same football club
@app.route('/players/club-name/<clubname>')
def player_by_club(clubname):
    players = get_players_by_teamName(clubname)
    return render_template('playertable.html', p_name=players)

# implement player stats comparison 
@app.route('/compare/<player1>/<player2>')
def stats_comparison(player1, player2):
  
    pl1 = get_player_stats(player1)
    pl2 = get_player_stats(player2)
    pl11 = get_info_by_playername(player1)
    pl22 = get_info_by_playername(player2)
    
    return render_template('comparison.html', p1=pl1, p2=pl2, p_name=pl11, p_name1=pl22)
    
# Dont forget error Handling 
# Update Player player profile page with more information
# Cashing

if __name__ == '__main__':
    app.run(debug=True)