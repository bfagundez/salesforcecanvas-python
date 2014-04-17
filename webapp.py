from flask import Flask, request
from canvas_signed_request import SignedRequest
app = Flask(__name__)
import os 

@app.route("/")
def hello():
    return "Hello World!"

# add a new route
@app.route('/canvas', methods=['POST'])
def canvas():
  secret = os.environ.get('SECRET')
  sr_param = request.form['signed_request']
  srHelper = SignedRequest(secret,sr_param)
  canvasRequestJSON = srHelper.verifyAndDecode()
  return canvasRequestJSON

if __name__ == "__main__":
    app.run()
