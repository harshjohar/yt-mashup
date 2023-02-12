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
            <label for="output">Output file name:</label>
            <input type="text" name="output" required>
            <br>
            <input type="submit" value="Submit">
        </form>
    '''
@app.route('/', methods=['POST'])
def submit():
    singer = request.form['singer']
    num_videos = int(request.form['num_videos'])
    audio_duration = int(request.form['audio_duration'])
    output = request.form['output']
    output = mashup(singer, num_videos, audio_duration, f"{output}.mp3")
    return f'<p>{output}.mp3</p>'

if __name__ == '__main__':
    app.run()