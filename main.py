from flask import Flask, request, render_template, Markup
from creepycrawler import start_crawl
import sys

app = Flask(__name__)


@app.route('/')
def my_form():
    return render_template('my-form.html')


@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    dir_name = str(hash(text) % ((sys.maxsize + 1) * 2))
    start_crawl.main_execute(dir_name, text, True)

    file_loc = dir_name + "/audits/results-pally.html"
    result = open(file_loc, "r+")
    content = Markup(result.read())
    result.close()
    return render_template('results.html', results=content)


if __name__ == "__main__":
    app.run(debug=True)
