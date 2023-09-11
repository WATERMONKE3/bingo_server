        // JavaScript code to handle random number scrolling
        const numberContainer = document.getElementById('number-container');
        const startButton = document.getElementById('start-button');
        const stopButton = document.getElementById('stop-button');
        let interval;
    
        function startScrolling() {
            clearInterval(interval); // Clear any existing interval
            let startTime = Date.now();
            
            interval = setInterval(function () {
                const elapsedTime = Date.now() - startTime;
                if (elapsedTime >= 5000) {
                    clearInterval(interval); // Stop scrolling after 5 seconds
                    const randomNumber = Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
                    numberContainer.textContent = randomNumber;
                } else {
                    const randomNumber = Math.floor(Math.random() * 75) + 1; // Random numbers between 1 and 75
                    numberContainer.textContent = randomNumber;
                }
                
            }, 100);
        }
    
        startButton.addEventListener('click', startScrolling);

