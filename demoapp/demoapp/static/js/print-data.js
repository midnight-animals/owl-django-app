document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/data/')  
        .then(response => response.json())
        .then(data => {
            let el = document.getElementById("data")
            el.textContent = `User: ${data.username} ${data.email}`;
            console.log(data);
        })
        .catch(error => console.error('Error:', error));
})