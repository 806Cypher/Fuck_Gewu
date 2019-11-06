from flask import Flask, render_template
app = Flask(__name__, static_url_path='/', static_folder="fuck_front/dist/",
            template_folder='fuck_front/dist/')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
