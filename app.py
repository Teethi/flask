from flask import Flask, render_template
# referencing this file
app=Flask(__name__)

@app.route('/')
def index():
    # return 'This is the homepage'
    return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)
