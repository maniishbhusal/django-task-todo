// Wait for the DOM content to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
    const checkboxes = document.querySelectorAll('.checkbox');

    checkboxes.forEach(function (checkbox) {
        const itemId = checkbox.getAttribute('data-id');
        const label = document.querySelector(`label[for="checkbox${itemId}"]`);
        const dataCompleted = checkbox.getAttribute('data-completed') === 'True';

        // Set the initial state of the checkbox based on the 'completed' attribute
        checkbox.checked = dataCompleted;
        if (checkbox.checked) label.classList.add('completed');

        // Store a reference to the label for later use
        checkbox.label = label;

        // Add a 'change' event listener to each checkbox
        checkbox.addEventListener('change', function () {
            const itemId = checkbox.getAttribute('data-id');
            const label = checkbox.label;

            // Check if the checkbox is checked
            if (checkbox.checked) {
                label.classList.add('completed');
                updateCompletedStatus(itemId, 1);
            } else {
                // Remove 'completed' class from the label if the checkbox is unchecked
                label.classList.remove('completed');
                updateCompletedStatus(itemId, 0);
            }
        });
    });

    // Function to send an asynchronous request
    function sendRequest(url, method, headers, body) {
        // Use the Fetch API to send a request with specified parameters
        fetch(url, {
            method,
            headers,
            body
        });
    }

    // Function to update the completed status of a todo item
    function updateCompletedStatus(itemId, status) {
        const url = `/update-completed/${itemId}/${status}/`;
        const method = 'POST';
        const headers = {
            'Content-Type': 'application/json',
            'X-CSRFToken': getCookie('csrftoken')
        };
        const body = JSON.stringify({});
        sendRequest(url, method, headers, body);
    }

    // Function to get the value of a specific cookie
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
});