from flask import Flask, request, jsonify
from webscraper import scrape_jobs

app = Flask(__name__)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    query = request.args.get('query')
    if not query:
        return jsonify({'error': 'Please provide a job title (query) parameter.'}), 400
    jobs = scrape_jobs(query)
    print(f"Jobs returned by scraper: {len(jobs)}")
    return jsonify(jobs)

def create_app():
    return app