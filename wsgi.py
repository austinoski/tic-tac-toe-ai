import os
from api import app


if __name__ == "__main__":
    debug = os.environ.get("DEBUG") or False
    app.run(debug=debug)
