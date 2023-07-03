```python
from flask import Flask, render_template, request, jsonify
from utils.lease_parser import parseLease
from utils.state_laws import getLaws
from utils.comparison_engine import compareLease

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    lease_file = request.files['lease-upload']
    state = request.form['state-selection']
    parsedLease = parseLease(lease_file)
    stateLaws = getLaws(state)
    comparisonResult = compareLease(parsedLease, stateLaws)
    return jsonify(comparisonResult)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
```