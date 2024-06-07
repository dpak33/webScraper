# Job Search App

** Please read the below carefully before proceeding, particularly the sections beginning 'Connecting to the Mern stack app' below. **

## Webscraper Setup

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/dpak33/webScraper.git
    cd webScraper
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv webscraper-env
    ```

3. **Activate the Virtual Environment**:
    - **For Windows**:
      ```sh
      webscraper-env\Scripts\activate
      ```
    - **For macOS and Linux**:
      ```sh
      source webscraper-env/bin/activate
      ```

4. **Install the Required Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add the following:
    ```env
    FLASK_APP=main.py
    FLASK_ENV=development
    PORT=5000
    ```

6. **Run the Webscraper**:
    ```sh
    flask run
    ```

### Connecting to the MERN Stack App

The primary purpose of this webscraper is to provide an endpoint that can be queried for job listings within the job search route of a MERN stack application. To set up and connect the MERN stack app, follow these steps:

1. **Clone the MERN Stack App Repository**:
    ```sh
    git clone https://github.com/dpak33/TDD.git
    cd TDD
    ```

2. **Follow the Setup Instructions in the MERN Stack App Repository**:
    Detailed setup instructions can be found within the `README.md` file of the MERN stack app repository. Ensure the Flask app is running before making queries from the MERN stack app.

### Further Documentation

For detailed information on the relationship between the webscraper and the MERN stack app, please refer to the documentation in the [TDD repository](https://github.com/dpak33/TDD.git).

### Future Enhancements

Tests for the webscraper will be added shortly to ensure robust functionality and reliability.

## Webscraper
The webscraper app can be found at the following GitHub directory: [webScraper Repository](https://github.com/dpak33/webScraper)