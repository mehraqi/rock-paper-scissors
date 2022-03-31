from flask import request, make_response, redirect

from logic import result, computer


def init_cookies():
    response = make_response(redirect("/p1-turn"))
    response.set_cookie("p1_name", request.form.get("player1"))
    response.set_cookie("p2_name", request.form.get("player2"))
    response.set_cookie("is_p2_computer", request.form.get("is_p2_computer"))
    response.set_cookie("p1_score", "0")
    response.set_cookie("p2_score", "0")
    return response


def p1_turn():
    p1_name = request.cookies.get("p1_name")
    p2_name = request.cookies.get("p2_name")
    p1_score = request.cookies.get("p1_score")
    p2_score = request.cookies.get("p2_score")
    return f"""
        <h1>{p1_name} vs {p2_name}</h1>
        <p>Score: {p1_score} vs {p2_score}
        <br/>
        <h4>{p1_name}'s turn</h4>
        <form method="post" action="/set-p1-choice">
            <label for="cars">Choose:</label>
            <select name="choice">
                <option value="rock">Rock</option>
                <option value="paper">Paper</option>
                <option value="scissors">scissors</option>
            </select> 
            <input type="submit" value="Submit Choice">
        </form>
    """


def set_p1_choice():
    response = make_response(redirect("/p2-turn"))
    response.set_cookie("p1_choice", request.form.get("choice"))
    return response


def p2_turn():
    is_p2_computer = request.cookies.get("is_p2_computer")
    if is_p2_computer == "yes":
        response = make_response(redirect("/set-p2-choice"))
        return response
    else:
        p1_name = request.cookies.get("p1_name")
        p2_name = request.cookies.get("p2_name")
        p1_score = request.cookies.get("p1_score")
        p2_score = request.cookies.get("p2_score")
        return f"""
            <h1>{p1_name} vs {p2_name}</h1>
            <p>Score: {p1_score} vs {p2_score}
            <br/>
            <h4>{p2_name}'s turn</h4>
            <form method="post" action="/set-p2-choice">
                <label for="cars">Choose:</label>
                <select name="choice">
                    <option value="rock">Rock</option>
                    <option value="paper">Paper</option>
                    <option value="scissors">scissors</option>
                </select>
                <input type="submit" value="Submit Choice"> 
            </form>
        """


def set_p2_choice():
    is_p2_computer = request.cookies.get("is_p2_computer")
    response = make_response(redirect("/get-winner"))
    if is_p2_computer == "yes":
        response.set_cookie("p2_choice", computer.get_computer_choice())
    else:
        response.set_cookie("p2_choice", request.form.get("choice"))
    return response


def get_winner():
    p1_name = request.cookies.get("p1_name")
    p2_name = request.cookies.get("p2_name")
    p1_score = request.cookies.get("p1_score")
    p2_score = request.cookies.get("p2_score")
    p1_choice = request.cookies.get("p1_choice")
    p2_choice = request.cookies.get("p2_choice")
    winner = result.get_winner(p1_choice, p2_choice)
    response = make_response(redirect("/reveal-winner"))
    if winner:
        if winner == "Player 1":
            response.set_cookie("winner", p1_name)
            response.set_cookie("p1_score", f"{int(p1_score) + 1}")
        else:
            response.set_cookie("winner", p2_name)
            response.set_cookie("p2_score", f"{int(p2_score) + 1}")
    else:
        response.set_cookie("winner", "None")
    return response


def reveal_winner():
    p1_name = request.cookies.get("p1_name")
    p2_name = request.cookies.get("p2_name")
    p1_score = request.cookies.get("p1_score")
    p2_score = request.cookies.get("p2_score")
    p1_choice = request.cookies.get("p1_choice")
    p2_choice = request.cookies.get("p2_choice")
    winner = request.cookies.get("winner")
    if winner != "None":
        winner_msg = f"<h1>{winner} is the winner</h1>"
    else:
        winner_msg = "<h1>It's a Tie</h1>"
    return f"""
        {winner_msg}
        <p>{p1_name} chose {p1_choice} and {p2_name} chose {p2_choice}</p>
        <br/>
        <p>Score: {p1_score} vs {p2_score}</p>
        <br/>
        <p><a href="/p1-turn">Next Round</a></p>
        <p><a href="/">Exit</a></p>
    """
