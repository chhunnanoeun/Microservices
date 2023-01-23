from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_user as us

app = Flask(__name__)

@app.route('/delete', methods=['DELETE'])
def delete():
    # Get the user's login information from the request
    user = request.form.get('username')

    _user = us.user_name()
    data = [x for x in _user if x["user"]==user]
    
    if (data):
        return jsonify({'message': 'delete Successfully'}), 200
    else:
        us.user_name(user)
        return jsonify({'message': 'cannot delete user'}), 401

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003, debug=True) #127.0.0.1