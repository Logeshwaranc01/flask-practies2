from flask import Flask
app=Flask(__name__)
@app.route ('/')
def hello_world():
    return "<div style='backgroung : blue'><h1>Logesh</h1><br><p>Hi, I'm Logeshwaran. I am currently pursuing a bachelor's degree in mechanical engineering. </p></div>"
if __name__=='__main__':
    app.run(debug=True)