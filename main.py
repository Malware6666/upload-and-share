from flask import Flask, request, render_template
import os
import uuid

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    if file:
        filename = str(uuid.uuid4()) + '-' + file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        file_url = f"/uploads/{filename}"
        return f'File uploaded successfully. Access it <a href="{file_url}">here</a>'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
