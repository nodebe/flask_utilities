import secrets 
import random
from functools import wraps
# You have to import 'session', 'redirect', 'url_for' in your main .py file where you are calling the function

# Check if user session is set
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

#Function to check if email already exists in database
# where 'db' is set to the database set and 'users' is the name of the database table
def check_for_same_email(email):
    #create cursor
    cs = db.cursor()
    try:
        checkquery = 'SELECT * FROM users WHERE email = %s'
        new_email = (email)
        cs.execute(checkquery, new_email)
        result = cs.fetchone()
        if result:
            return 'Email already exists, choose another email or login!'
    except Exception as e:
        return 'Something went wrong! ' + str(e)

#function for creating unique id
#the length of the id is passed in as an argument to the function
def unique_id(x):
    token = secrets.token_hex(16)[:x]
    new_token = ' '.join(token).split(' ')
    main_id = ''.join(random.sample(new_token, len(new_token)-1))
    return (main_id)
