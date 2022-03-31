def index():
    return """
        <h1>Welcome to Rock Paper Scissors game</h1>
        <form method="post" action="/init-cookies">
            <p>Name of Player 1: <input type="text" name="player1" required></p>
            <p>Name of Player 2: <input type="text" name="player2" required></p>
            <p>
                Is Player 2 Computer? 
                <select name="is_p2_computer">
                    <option value="yes">Yes</option>
                    <option value="no">No</option>
                </select>
            </p>
            
            <input type="submit" value="Play">
        </form>
    """
