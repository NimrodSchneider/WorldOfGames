from flask import Flask
from Score import get_score
import Utils
app = Flask(__name__)


# Score server function
# Tries to get score from the score file
# If gets - shows the score
# if fails - shows an error
@app.route('/')
def score_server():
    current_score = get_score()
    if current_score == Utils.BAD_RETURN_CODE:
        return '''
        <html>
            <head>
                <title>Scores Game</title>
            </head>
            <body>
                <h1><div id="score" style="color:red">'could not open the scores file'</div></h1>
            </body>
        </html>'''
    else:
        return f'''
        <html>
            <head>
                <title> Scores Game </title>
            </head>
            <body>
                <h1> The score is <div id = "score"> {current_score} </div> 
                </h1>
            </body>
        </html>'''


if __name__ == '__main__':
    app.run()
