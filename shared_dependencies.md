1. Exported Variables:
   - `stateLaws` (from `state_laws.py` to `comparison_engine.py`)
   - `parsedLease` (from `lease_parser.py` to `comparison_engine.py`)
   - `comparisonResult` (from `comparison_engine.py` to `app.py`)

2. Data Schemas:
   - `LeaseSchema` (used in `lease_parser.py` and `comparison_engine.py`)
   - `StateLawSchema` (used in `state_laws.py` and `comparison_engine.py`)

3. DOM Element IDs:
   - `#state-selection` (used in `index.html` and `main.js`)
   - `#lease-upload` (used in `index.html` and `main.js`)
   - `#compare-button` (used in `index.html` and `main.js`)
   - `#comparison-result` (used in `results.html` and `main.js`)

4. Message Names:
   - `uploadSuccess` (used in `main.js` and `app.py`)
   - `uploadFailure` (used in `main.js` and `app.py`)
   - `comparisonComplete` (used in `main.js` and `app.py`)

5. Function Names:
   - `parseLease()` (defined in `lease_parser.py` and used in `app.py`)
   - `getLaws()` (defined in `state_laws.py` and used in `app.py`)
   - `compareLease()` (defined in `comparison_engine.py` and used in `app.py`)
   - `uploadLease()` (defined in `main.js` and used in `index.html`)
   - `displayResult()` (defined in `main.js` and used in `results.html`)