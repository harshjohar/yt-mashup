from flask import Flask, request
from mashup import mashup

app = Flask(__name__)

@app.route('/', methods=['GET'])
def form():
    return '''
        <form method="post">
            <label for="singer">Singer Name:</label>
            <input type="text" name="singer" required>
            <br>
            <label for="num_videos">Number of Videos:</label>
            <input type="number" name="num_videos" required>
            <br>
            <label for="audio_duration">Duration of Audio:</label>
            <input type="number" name="audio_duration" required>
            <br>
            <label for="email">Email:</label>
            <input type="email" name="email" required>
            <br>
            <input type="submit" value="Submit">
        </form>
    '''
@app.route('/', methods=['POST'])
def submit():
    singer = request.form['singer']
    num_videos = int(request.form['num_videos'])
    audio_duration = int(request.form['audio_duration'])
    email = request.form['email']
    output = mashup(singer, num_videos, audio_duration, email)
    return f'<p>{output}</p>'

if __name__ == '__main__':
    app.run()