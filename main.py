from app.api import create_app
import dotenv
import os

dotenv.load_dotenv()

app = create_app()

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, port=port)
