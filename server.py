"""Greeting Flask app."""

from random import choice

from flask import Flask, request, url_for

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Home page."""

    return """<!doctype html><html>
    <h1>Hi! This is the home page.</h1>
    <a href=\"/hello\">Hello</a>
    <a href=\"/mean\">Diss</a>
    </html>"""


@app.route('/hello')
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit"> <br>
          <input type="radio" name="comp" value="Compliment 1"> Compliment 1 </>
          <input type="radio" name="comp" value="Compliment 2"> Compliment 2 </>
          <input type="radio" name="comp" value="Compliment 3"> Compliment 3 </>
          <input type="radio" name="comp" value="Compliment 4"> Compliment 4 </>
        </form>
      </body>
    </html>
    """

@app.route('/mean')
def mean():
    """Say hello and prompt for user's name and a diss."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit"> <br>
          <input type="radio" name="diss" value="Diss 1"> Diss 1 </>
          <input type="radio" name="diss" value="Diss 2"> Diss 2 </>
          <input type="radio" name="diss" value="Diss 3"> Diss 3 </>
          <input type="radio" name="diss" value="Diss 4"> Diss 4 </>
        </form>
      </body>
    </html>
    """


@app.route('/greet')
def greet_person():
    """Get user by name."""

    player = request.args.get("person")

    compliment = request.args.get("comp")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {compliment}!
      </body>
    </html>
    """

@app.route('/diss')
def diss_person():
    """Get user by name."""

    player = request.args.get("person")

    diss = request.args.get("diss")
    return f"""
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {player}! I think you're {diss}!
      </body>
    </html>
    """


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
