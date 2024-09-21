from flask import Flask

app = Flask(_name_)

@app.route("/hello")
def hello():
    returt 'elko world'

    if _name_--'_main_':
        app.run(debug=True)