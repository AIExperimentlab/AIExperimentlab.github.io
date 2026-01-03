// script.js
const inputText = document.getElementById('input-text');
const submitButton = document.getElementById('submit-button');
const outputText = document.getElementById('output-text');

submitButton.addEventListener('click', async () => {
    const prompt = inputText.value.trim();
    if (prompt !== '') {
        try {
            const response = await fetch('https://api.groq.io/v1/queries', {
                method: 'POST',
                headers: {
                    'Authorization': 'Bearer YOUR_GROQ_KEY',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    query: `query MagnusOpus($prompt: String!) {
                        magnusOpus(prompt: $prompt) {
                            response
                        }
                    }`,
                    variables: {
                        prompt: prompt
                    }
                })
            });
            const data = await response.json();
            outputText.innerText = data.data.magnusOpus.response;
        } catch (error) {
            console.error(error);
            outputText.innerText = 'Error: ' + error.message;
        }
    } else {
        outputText.innerText = 'Please enter a prompt.';
    }
});
