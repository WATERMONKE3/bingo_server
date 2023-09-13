function startScroll() {
    // Disable the Start button to prevent multiple selections
    document.getElementById('start-button').disabled = true;

    // Function to generate and display a random number every 100 milliseconds
    function scrollNumber() {
        const randomNumber = Math.floor(Math.random() * 75) + 1;
        document.getElementById('number-container').textContent = randomNumber;
        document.getElementById('selected-number-input').value = randomNumber;

        // Check if a number is selected (not equal to 0) and submit the form
        if (randomNumber !== 0) {
            document.getElementById('bingo-form').submit();
        } else {
            // Continue scrolling numbers
            setTimeout(scrollNumber, 100);
        }
    }

    // Start scrolling numbers for 3 seconds (3000 milliseconds)
    setTimeout(function () {
        // Stop scrolling after 3 seconds
        document.getElementById('start-button').disabled = false;
    }, 5000);

    // Start scrolling numbers
    scrollNumber();
}
