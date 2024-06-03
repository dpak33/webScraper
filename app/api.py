from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from webscraper import scrape_jobs


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    query = request.args.get('query')
    location = request.args.get('location')
    if not query:
        response = make_response(jsonify({'error': 'Please provide a job title (query) parameter.'}), 400)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    jobs = scrape_jobs(query, location)
    print(f"Jobs returned by scraper: {len(jobs)}")
    response = make_response(jsonify(jobs))
    response.headers['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)