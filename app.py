from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def gfg():
	if request.method == "POST":

	    # first_name = request.form.get("fname")
	    # last_name = request.form.get("lname")
	
	    return render_template("index.html")

if __name__=='__main__':
    app.run(debug=True)