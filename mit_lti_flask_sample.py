import os
from flask import Flask
from flask import render_template
from flask.ext.wtf import Form
from wtforms import IntegerField, BooleanField
from random import randint

from pylti.flask import lti

VERSION = '0.0.1'
app = Flask(__name__)
app.config.from_object('config')


class AddForm(Form):
    """ Add data from Form

    :param Form:
    """

    p11 = IntegerField('p11')
    p12 = IntegerField('p12')
    p21 = IntegerField('p21')
    p22 = IntegerField('p22')
    p31 = IntegerField('p31')
    p32 = IntegerField('p32')
    p41 = IntegerField('p41')
    p42 = IntegerField('p42')
    p51 = IntegerField('p51')
    p52 = IntegerField('p52')
    result1 = IntegerField('result1')
    result2 = IntegerField('result2')
    result3 = IntegerField('result3')
    result4 = IntegerField('result4')
    result5 = IntegerField('result5')
    correct1 = BooleanField('correct1')
    correct2 = BooleanField('correct2')
    correct3 = BooleanField('correct3')
    correct4 = BooleanField('correct4')
    correct5 = BooleanField('correct5')


def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')


@app.route('/is_up', methods=['GET'])
def hello_world(lti=lti):
    """ Indicate the app is working. Provided for debugging purposes.

    :param lti: the `lti` object from `pylti`
    :return: simple page that indicates the request was processed by the lti
        provider
    """
    return render_template('up.html', lti=lti)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET'])
@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    return render_template('index.html', lti=lti)


@app.route('/index_staff', methods=['GET', 'POST'])
@lti(request='session', error=error, role='staff', app=app)
def index_staff(lti=lti):
    """ render the contents of the staff.html template

    :param lti: the `lti` object from `pylti`
    :return: the staff.html template rendered
    """
    return render_template('staff.html', lti=lti)


@app.route('/add', methods=['GET'])
@lti(request='session', error=error, app=app)
def add_form(lti=lti):
    """ initial access page for lti consumer

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    form = AddForm()
    form.p11.data = randint(1, 9)
    form.p12.data = randint(1, 9)
    form.p21.data = randint(1, 9)
    form.p22.data = randint(1, 9)
    form.p31.data = randint(1, 9)
    form.p32.data = randint(1, 9)
    form.p41.data = randint(1, 9)
    form.p42.data = randint(1, 9)
    form.p51.data = randint(1, 9)
    form.p52.data = randint(1, 9)
    return render_template('add.html', form=form)


@app.route('/grade', methods=['POST'])
@lti(request='session', error=error, app=app)
def grade(lti=lti):
    """ post grade

    :param lti: the `lti` object from `pylti`
    :return: grade rendered by grade.html template
    """
    form = AddForm()
    correct1 = ((form.p11.data + form.p12.data) == form.result1.data)
    correct2 = ((form.p21.data + form.p22.data) == form.result2.data)
    correct3 = ((form.p31.data + form.p32.data) == form.result3.data)
    correct4 = ((form.p41.data + form.p42.data) == form.result4.data)
    correct5 = ((form.p51.data + form.p52.data) == form.result5.data)
    form.correct1.data = correct1
    form.correct2.data = correct2
    form.correct3.data = correct3
    form.correct4.data = correct4
    form.correct5.data = correct5
    score = 0
    score += 2 if correct1 else 0
    score += 2 if correct2 else 0
    score += 2 if correct3 else 0
    score += 2 if correct4 else 0
    score += 2 if correct5 else 0
    lti.post_grade(score/10.)
    return render_template('grade.html', form=form, score=score)


def set_debugging():
    """ enable debug logging

    """
    import logging
    import sys

    root = logging.getLogger()
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(name)s - %(message)s')
    ch.setFormatter(formatter)
    root.addHandler(ch)

set_debugging()

if __name__ == '__main__':
    """
    For if you want to run the flask development server
    directly
    """
    port = int(os.environ.get("FLASK_LTI_PORT", 5000))
    host = os.environ.get("FLASK_LTI_HOST", "localhost")
    app.run(debug=True, host=host, port=port)
