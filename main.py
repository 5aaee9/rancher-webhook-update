from flask import Flask
import router
import config

app = Flask(__name__)

app.i_config = config

# Import all router in router dir
for mod in dir(router):
    # Don't import hide module
    if str(mod).startswith("__"):
        continue

    getattr(router, mod).attach(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0")