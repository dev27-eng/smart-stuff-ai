```python
from .lease_parser import parsedLease
from .state_laws import stateLaws

def compareLease(parsedLease, stateLaws):
    comparisonResult = []
    for section, content in parsedLease.items():
        if section in stateLaws:
            if content != stateLaws[section]:
                comparisonResult.append({
                    'section': section,
                    'lease_content': content,
                    'state_law': stateLaws[section]
                })
    return comparisonResult
```