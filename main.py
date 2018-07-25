from flask import Flask, request, render_template, Markup
from creepycrawler import start_crawl
import shutil
import sys, os

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

    home = os.path.expanduser('~')
    q = os.path.join(home, file_loc)

    result = open(q, "r+")
    content = Markup(result.read())
    result.close()

    try:
        shutil.rmtree(q)
    except OSError as e:
        print("Error: %s - %s." % (e.filename, e.strerror))

    return render_template('results.html', results=content)


if __name__ == "__main__":
    app.run(debug=True)
