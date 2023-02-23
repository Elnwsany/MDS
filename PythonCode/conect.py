from flask import Flask , render_template , request
rec_app = Flask(__name__)

@rec_app.route("/", methods=['GET','POST'])

def homepage():
    if request.method == 'POST':
        imagefile = request.files['imagefile']
        image_path = "./images/" + imagefile.filename
        imagefile.save(image_path)

        # model
        # use image_path to get photo

    return render_template("homepage.html")

if __name__ == "__main__":
    rec_app.run(debug=True, port=9000)