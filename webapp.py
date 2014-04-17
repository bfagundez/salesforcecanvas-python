from flask import Flask
from canvas_signed_request import SignedRequest
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

# add a new route
@app.route('/canvas', methods=['POST',])
def canvas():
  sr_param = request.form['signed_request']
  secret = os.environ.get('CANVAS_SECRET')
  srHelper = SignedRequest(secret,sr_param)
  canvasRequestJSON = srHelper.verifyAndDecode()

  #load request data json to extract parameters
  return str(canvasRequestJSON)

if __name__ == "__main__":
    app.run()
