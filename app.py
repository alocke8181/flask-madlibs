from flask import Flask, request, render_template
from stories import story
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)

@app.route('/')
def show_home():
    return render_template('form.html', prompts = story.prompts)

@app.route('/story')
def show_story():
    story_text = story.generate(request.args)
    return render_template('story.html', story_text = story_text)