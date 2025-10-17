from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_folder='website-main')

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    # Пытаемся найти файл по пути
    file_path = os.path.join(app.static_folder, path)
    
    # Если путь существует и это файл - отдаем его
    if os.path.exists(file_path) and os.path.isfile(file_path):
        return send_from_directory(app.static_folder, path)
    
    # Иначе отдаем index.html (для React Router)
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == '__main__':
    app.run(host='localhost', port=3000, debug=True)