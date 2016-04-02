from flask import *

from app import app, mongo
from app.form import CreateImageForm


@app.route('/add', methods=['GET', 'POST'])
def create_image():
    form = CreateImageForm(request.form)
    if form.validate_on_submit():
        image = {
            'name': form.name.data,
            'source': form.source.data,
        }
        mongo.db.images.insert_one(image)
        return redirect('/')
    return render_template('add_image.html', form=form)


# @app.route('/\d*')
# def retrieve_image():
#     return 'Hello World!'


@app.route('/')
def list_image():
    collection = list(mongo.db.images.find())
    return render_template('list_image.html', collection=collection)


@app.route('/static/<path>')
def static_proxy(path):
    return app.send_static_file(path)


if __name__ == '__main__':
    app.run(debug=True)
