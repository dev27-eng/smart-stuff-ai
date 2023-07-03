```python
from .lease_parser import parsedLease
from .state_laws import stateLaws

def compareLease():
    comparisonResult = []
    for section in parsedLease:
        for law in stateLaws:
            if law['law'] in section['content']:
                comparisonResult.append({
                    'section': section['title'],
                    'content': section['content'],
                    'law': law['law'],
                    'description': law['description']
                })
    return comparisonResult
```