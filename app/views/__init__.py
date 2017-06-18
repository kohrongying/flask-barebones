from app import app
from flask import jsonify, render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

"""

Error Handling

"""

@app.errorhandler(500)
def internal_server_error(error):
    responseObject = {
        'status': 'fail',
        'message': 'Try again. 500 Internal Server Error'
    }
    app.logger.error('Server Error: %s',(error))
    return jsonify(responseObject), 200
