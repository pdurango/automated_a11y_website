from flask import Flask, request, render_template, Markup, send_from_directory
from creepycrawler import start_crawl
import shutil
import sys
import os


app = Flask(__name__)
# you are we


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

    if os.path.exists(q):
        result = open(q, "r+")
        content = Markup(result.read())
        result.close()

        # try:
        #     shutil.rmtree(home + "/" + dir_name)
        # except OSError as e:
        #     print("Error: %s - %s." % (e.filename, e.strerror))

        if content == "undefined<br>":
            return render_template('error.html', error_message="Web page entered is not valid or does not exist")
        else:
            return render_template('results.html', results=content)

    else:
        return render_template('error.html', error_message="Results file does not exist")


@app.route('/about')
def about():
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon-16x16.png', mimetype='image/vnd.microsoft.icon')


if __name__ == "__main__":
    app.run(debug=True)

