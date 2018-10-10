from flask import Flask, request
from generate import gen
app = Flask(__name__, static_url_path='/static')
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')

def homepage():
    return """
    <html>
    <head>
        <title>
            Handwriting Generation
        </title>
        <link rel = "stylesheet" href = "/static/style.css"/>
    </head>
    <body>
        <form action = "result" method = "post">
            <ul>
                <li>
                    <p>Enter the text to generate:</p>
                </li>
                <li>
                    <input type = "text" name = "gen_text" id = "gen_text" placeholder = "text"/>
                </li>
                <li>
                    <p> Select a style (optional): </p>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style1" value = "0">
                    <img src = "/static/imgs/style0.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style2" value = "1"/>
                    <img src = "/static/imgs/style1.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style3"  value = "2"/>
                    <img src = "/static/imgs/style2.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style4"  value = "3"/>
                    <img src = "/static/imgs/style3.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style5"  value = "4"/>
                    <img src = "/static/imgs/style4.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style6"  value = "5"/>
                    <img src = "/static/imgs/style5.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style7"  value = "6"/>
                    <img src = "/static/imgs/style6.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "style8"  value = "7"/>
                    <img src = "/static/imgs/style7.png" /></input>
                </li>
                <li>
                    <input type = "radio" name = "style" id = "none" value = "404"/>
                    None
                </li>
                <li>
                    Select the bias (min. 0, max. 1.0):
                </li>
                <li>
                    <input name = "bias" min = "0" max = "1" value = "0.15" step = "0.05" type = "range" />
                </li>
                <li>
                    <button type = "submit" id = "generate">Submit</button>
                </li>
            </ul>     
        </form>
    </body>
</html>
    """

@app.route('/result', methods = ['POST'])
def result():
    text = request.form["gen_text"]
    style = request.form.get('style', 404)
    bias = request.form.get('bias', 1.0)
    print("The text from user is: " + text)
    print("Generating..")
    gen(text, style, bias)
    return """
    <html>
    <head>
        <title>
            Handwriting Generation
        </title>
        <link rel = "stylesheet" href = "/static/style.css"/>
    </head>
        <body>
            <img src = /static/results/sample.png?34049493 />
        </body>
    </html>
    """

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug = True, use_reloader = True)