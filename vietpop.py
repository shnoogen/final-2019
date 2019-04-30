from flask import Flask, render_template, redirect, url_for, request
from modules import convert_to_dict

from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, SelectField
from wtforms.validators import Required

app = Flask(__name__)

application = app 

# Flask-WTF requires an encryption key - the string can be anything
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

# Flask-Bootstrap requires this line
Bootstrap(app)

# create a list of dicts
viet_list = convert_to_dict("ACS_Vietnam.csv")

# with Flask-WTF, each web form is represented by a class
# "SearchForm" can change; "(FlaskForm)" cannot
class SearchForm(FlaskForm):
    # the choices are (option, string)
    viet_choice = SelectField('Select from this list')
    submit = SubmitField('Search')

# first route

@app.route('/', methods=['GET', 'POST'] )
def index():
    code_list = []
    state_list = []
    pairs_list = []
    # fill one list with the number of each presidency and
    # fill the other with the name of each president
    for viet in viet_list:
        code_list.append(viet['Id2'])
        state_list.append(viet['State'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(code_list, state_list)

    # this is from the class above; form will go to the template
    form = SearchForm()
    # this is how we auto-populate a select menu in a form
    form.viet_choice.choices = [ (p[0], p[1]) for p in pairs_list ]

    # if page opened by form submission, redirect to detail page
    if request.method == "POST":
        # get the input from the form
        viet_choice = request.form.get("viet_choice")
        return redirect( url_for('detail', num=viet_choice ) )

    # no else - just do this by default
    return render_template('search2.html', form=form)

    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    # return render_template('index.html', pairs=pairs_list, the_title="Vietnamese American Diaspora")

# second route

@app.route('/state/<num>')
def detail(num):
    for viet in viet_list:
        if viet['Id2'] == num:
            viet_dict = viet
            break
    return render_template('state.html', viet=viet_dict, the_title=viet_dict['State'])

# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
