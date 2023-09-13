// JavaScript code to handle random number scrolling
const numberContainer = document.getElementById('number-container');
const startButton = document.getElementById('start-button');
const selectedNumberContainer = document.getElementById('selected-number-container'); // Element to display selected number
let interval;
let selectedNumber;

function saveSelectedNumberToDB(selectedNumber) {
    // Create a new FormData object to send the selected number as part of the form
    const formData = new FormData();
    formData.append('csrfmiddlewaretoken', '{{ csrf_token }}');
    formData.append('selected_number', selectedNumber);

    // Create a new XMLHttpRequest to submit the form data
    const xhr = new XMLHttpRequest();
    xhr.open('POST', '{% url "save_selected_number" %}', true);
    xhr.onreadystatechange = function () {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                // Handle the success response from the server if needed
                console.log('Number saved to the database:', selectedNumber);
            } else {
                // Handle errors if any
                console.error('Error saving number:', xhr.statusText);
            }
        }
    };
    xhr.send(formData);
}

function startScrolling() {
    clearInterval(interval); // Clear any existing interval
    let startTime = Date.now();

    interval = setInterval(function () {
        const elapsedTime = Date.now() - startTime;
        if (elapsedTime >= 5000) {
            clearInterval(interval); // Stop scrolling after 5 seconds
            selectedNumber = Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
            numberContainer.textContent = selectedNumber;
            selectedNumberContainer.textContent = `Selected Number: ${selectedNumber}`; // Display the selected number

            // Send the selected number to your Django view to save in the database
            saveSelectedNumberToDB(selectedNumber);
        } else {
            const randomNumber = Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
            numberContainer.textContent = randomNumber;
        }

    }, 100);
}

startButton.addEventListener('click', startScrolling);
