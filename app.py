from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')  # Render the HTML form from templates/index.html

@app.route('/login', methods=['POST'])
def login():
    user = request.form.get('nm')
    if user:
        return redirect(url_for('success', name=user))
    else:
        return "Please enter a name!"

@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}!"

if __name__ == '__main__':
    app.run(debug=True)
