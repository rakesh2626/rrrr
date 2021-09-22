import threading
from flask import Flask
from get.views import get
from post.views import post
from put.views import put11
from delete.views import delete11
from threading import Thread
app = Flask(__name__)
app.register_blueprint(get)
app.register_blueprint(post)
app.register_blueprint(put11)
app.register_blueprint(delete11)
threading.Thread(target=get)

print(app.url_map)

app.run(debug=False)

