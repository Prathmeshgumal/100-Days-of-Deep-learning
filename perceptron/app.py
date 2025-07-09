from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    if request.method == "POST":
        learning_rate = request.form.get("learning_rate",type=float)
        epochs = request.form.get("epochs",type=int)
        print(f"Learing Rate: {learning_rate} , Epochs: {epochs}")

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)