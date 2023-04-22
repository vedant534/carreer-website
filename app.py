from flask import Flask,render_template

app= Flask(__name__)
JOBS=[
  {
    'id':1,
    'title': 'data analyst',
    'location': 'remote',
    'salary' : '10 lakhs'
  },
  {
    'id':2,
    'title': 'backend eng',
    'location': 'gurgaon',
    'salary' : '9 lakhs'
  },
  {
    'id':3,
    'title': 'frontend eng',
    'location': 'bengaluru',
    'salary' : '6 lakhs'
  }
]
@app.route("/")
def hello_naukri():
  return render_template('home.html',jobs=JOBS,company_name="good4u")
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)

