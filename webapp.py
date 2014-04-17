from flask import Flask
from canvas_signed_request import SignedRequest
app = Flask(__name__)
import os 


@app.route("/")
def hello():
    return "Hello World!"

# add a new route
@app.route('/canvas', methods=['POST','GET'])
def canvas():
  print 'received signed request'
  secret = os.environ.get('SECRET')
  print ' secret '+secret
  sr_param = request.form['signed_request']
  print ' sr param '+sr_param
  srHelper = SignedRequest(secret,sr_param)
  canvasRequestJSON = srHelper.verifyAndDecode()

  #load request data json to extract parameters
  return str(canvasRequestJSON)

if __name__ == "__main__":
    app.run()
