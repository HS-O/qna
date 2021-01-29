from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
	  return render_template('index.html')
  else:
    #if request.form.get('submit')
    userInput = request.form.get('userInput')
    finaldata = ''
    finaldata += userInput + '\n'
    with open('userinput.txt', 'a') as _file:
      _file.write(finaldata)
    _file.close
    return render_template("submission.html")

@app.route('/submission', methods=['GET', 'POST'])
def submission():
  if request.method == 'GET':
	  return render_template('submission.html')
  else:
    return render_template('index.html')

app.run(host='0.0.0.0', port=8080)