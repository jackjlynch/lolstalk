from flask import Flask
from flask import render_template
from riotwatcher.riotwatcher import RiotWatcher

app = Flask(__name__)

riot_api = None

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/userinfo/<username>')
def user_info(username):
    game = riot_api.get_current_game(riot_api.get_summoner(name=username)['id'])
    return render_template('gameinfo.html', participants=game['participants'])
    # return str(game['participants'][0])


if __name__ == '__main__':
    app.debug = True
    app.config.from_pyfile('dev.cfg')
    riot_api = RiotWatcher(app.config['API_KEY'])
    app.run()