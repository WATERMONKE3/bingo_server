// JavaScript code to handle random number scrolling
const numberContainer = document.getElementById('number-container');
const startButton = document.getElementById('start-button');
const selectedNumberContainer = document.getElementById('selected-number-container'); // Element to display selected number
let interval;
let selectedNumber;

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

            // Send the selected number to your Django view using AJAX
            saveSelectedNumber(selectedNumber);
        } else {
            const randomNumber = Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
            numberContainer.textContent = randomNumber;
        }

    }, 100);
}

startButton.addEventListener('click', startScrolling);

