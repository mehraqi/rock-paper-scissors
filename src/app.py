from flask import Flask

from views import index
from views import play

app = Flask("rock-paper-scissors")

app.add_url_rule("/", view_func=index.index)
app.add_url_rule("/init-cookies", view_func=play.init_cookies, methods=["POST"])
app.add_url_rule("/p1-turn", view_func=play.p1_turn)
app.add_url_rule("/set-p1-choice", view_func=play.set_p1_choice, methods=["POST"])
app.add_url_rule("/p2-turn", view_func=play.p2_turn)
app.add_url_rule("/set-p2-choice", view_func=play.set_p2_choice, methods=["GET", "POST"])
app.add_url_rule("/get-winner", view_func=play.get_winner)
app.add_url_rule("/reveal-winner", view_func=play.reveal_winner)

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8080, debug=True)
