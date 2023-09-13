function startScroll() {
    // Disable the Start button to prevent multiple selections
    document.getElementById('start-button').disabled = true;

    // Function to generate and display a random number every 1000 milliseconds (1 second)
    function scrollNumber() {
        const randomNumber = Math.floor(Math.random() * 75) + 1;
        document.getElementById('number-container').textContent = randomNumber;
        document.getElementById('selected-number-input').value = randomNumber;

        // Check if a number is selected (not equal to 0) and submit the form
        if (randomNumber !== 0) {
            document.getElementById('bingo-form').submit();
        } else {
            // Continue scrolling numbers after a 1-second interval
            setTimeout(scrollNumber, 5000);
        }
    }

    // Start scrolling numbers for 5 seconds (5000 milliseconds)
    setTimeout(function () {
        // Stop scrolling after 5 seconds
        document.getElementById('start-button').disabled = false;
    }, 5000);

    // Start scrolling numbers
    scrollNumber();
}
