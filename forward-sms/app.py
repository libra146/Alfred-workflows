from bottle import request, run, route, abort
import bottle

msg = ''


@route('/msg', method=['POST', 'GET'])
def set_msg():
    global msg
    data = request.json
    print('data: ' + str(data))
    token = data['token']
    if token != 'token':
        abort(404)
    msg = data['content']
    return 'Success'


@route('/get_msg')
def get_msg():
    global msg
    if request.query.get('token') != 'token':
        abort(404)
    return msg

if __name__ == "__main__":
    bottle.run(host='0.0.0.0', debug=False, port=9888)
else:
    app = bottle.default_app()
