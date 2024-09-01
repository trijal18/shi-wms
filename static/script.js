function processText() {
    const text = document.getElementById("userText").value;

    if (text.trim() === "") {
        alert("Please enter some text!");
        return;
    }

    // Sending the text to the Python function
    fetch('/process_text', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: text })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            document.getElementById("videoDownload").style.display = "block";
            document.getElementById("downloadLink").href = data.videoUrl;
        } else {
            alert("Error processing text.");
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
