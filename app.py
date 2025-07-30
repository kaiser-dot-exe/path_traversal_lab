from flask import Flask, request, send_from_directory, render_template

app = Flask(__name__)


DOWNLOAD_DIRECTORY = "files"


import os
if not os.path.exists(DOWNLOAD_DIRECTORY):
    os.makedirs(DOWNLOAD_DIRECTORY)


with open(os.path.join(DOWNLOAD_DIRECTORY, "secret_notes.txt"), "w") as f:
    f.write("Bu, çok gizli bir nottur. Şifrelerim: user123, admin456")

with open(os.path.join(DOWNLOAD_DIRECTORY, "public_info.txt"), "w") as f:
    f.write("Bu dosya genel bilgiler içerir.")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    filename = request.args.get('filename')
    if filename:
        try:
            # Burası zafiyetin olduğu yer! Kullanıcıdan gelen dosya adı doğrudan kullanılıyor.
            return send_from_directory(DOWNLOAD_DIRECTORY, filename)
        except Exception as e:
            return f"Dosya bulunamadı veya bir hata oluştu: {e}", 404
    return "Lütfen bir dosya adı belirtin. Örn: /download?filename=public_info.txt"

if __name__ == '__main__':
    app.run(debug=True)