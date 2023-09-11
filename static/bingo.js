// JavaScript code to handle random number scrolling
const numberContainer = document.getElementById('number-container');
const startButton = document.getElementById('start-button');
const bingoTable = document.getElementById('bingo-table');
let interval;

function getRandomNumber() {
    return Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
}

function startScrolling() {
    clearInterval(interval); // Clear any existing interval
    let startTime = Date.now();

    interval = setInterval(function () {
        const elapsedTime = Date.now() - startTime;
        if (elapsedTime >= 5000) {
            clearInterval(interval); // Stop scrolling after 5 seconds
            const randomNumber = getRandomNumber();
            numberContainer.textContent = randomNumber;

            // Display the selected number in the corresponding column
            let columnId = '';
            if (randomNumber >= 1 && randomNumber <= 15) {
                columnId = 'b-column';
            } else if (randomNumber >= 16 && randomNumber <= 30) {
                columnId = 'i-column';
            } else if (randomNumber >= 31 && randomNumber <= 45) {
                columnId = 'n-column';
            } else if (randomNumber >= 46 && randomNumber <= 60) {
                columnId = 'g-column';
            } else {
                columnId = 'o-column';
            }

            const column = document.getElementById(columnId);
            if (column.textContent === '') {
                column.textContent = randomNumber;
            }

            // Remove the selected number from the scroll
            numberContainer.textContent = '';
        } else {
            const randomNumber = getRandomNumber();
            numberContainer.textContent = randomNumber;
        }
    }, 100);
}

startButton.addEventListener('click', startScrolling);
