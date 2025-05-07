// Handle the user's input and send a request to the Flask app
document.getElementById('send-button').addEventListener('click', function() {
    // Get the user's command
    const command = document.getElementById('command-input').value;
    // Send a POST request to the Flask app with the user's command as JSON data
    fetch('/respond', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ 'command': command }),
    })
    .then(response => response.json())
    .then(data => {
        // Do something with the response from the Flask app
        console.log(data);
    })
    .catch((error) => {
        // Handle errors
        console.error('Error:', error);
    });
    // Clear the input field
    document.getElementById('command-input').value = '';
});