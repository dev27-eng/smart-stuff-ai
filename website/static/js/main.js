document.addEventListener('DOMContentLoaded', function() {
    const stateSelection = document.querySelector('#state-selection');
    const leaseUpload = document.querySelector('#lease-upload');
    const compareButton = document.querySelector('#compare-button');
    const comparisonResult = document.querySelector('#comparison-result');

    compareButton.addEventListener('click', function() {
        uploadLease();
    });

    function uploadLease() {
        let formData = new FormData();
        formData.append('state', stateSelection.value);
        formData.append('lease', leaseUpload.files[0]);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.message === 'uploadSuccess') {
                displayResult(data.comparisonResult);
            } else if (data.message === 'uploadFailure') {
                alert('Failed to upload lease. Please try again.');
            }
        })
        .catch(error => console.error('Error:', error));
    }

    function displayResult(result) {
        comparisonResult.innerHTML = '';
        if (result.length === 0) {
            comparisonResult.innerHTML = 'No violations found in the lease.';
        } else {
            result.forEach(violation => {
                let violationElement = document.createElement('p');
                violationElement.textContent = `Section ${violation.section}: ${violation.description}`;
                comparisonResult.appendChild(violationElement);
            });
        }
    }
});