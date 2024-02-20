from flask import Flask, render_template
import database

app = Flask(__name__)

# JOBS = [
#   {
#     'id':1,
#     'title':"Backend Developer",
#     'name':"Arpan"
#   },
  
#   {
#     'id':2,
#     'title':"Fullstack Developer",
#     'name':"Ravish"
#   },

#   {
#     'id':3,
#     'title':"Algorithms Engineer",
#     'name':"Krish"
#   },
# ]

@app.route('/')
def hello_world():
  JOBS = database.load_jobs_from_db()
  return render_template('home.html', jobs=JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)