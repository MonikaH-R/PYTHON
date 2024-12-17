<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple AI Chatbot</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css"></link>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Roboto', sans-serif;
        }
    </style>
</head>
<body class="bg-gray-100 flex items-center justify-center min-h-screen">
    <div class="bg-white shadow-lg rounded-lg w-full max-w-md">
        <div class="bg-blue-500 text-white text-center py-4 rounded-t-lg">
            <h1 class="text-2xl font-bold">AI Chatbot</h1>
        </div>
        <div class="p-4 h-96 overflow-y-auto" id="chat-window">
            <!-- Chat messages will appear here -->
        </div>
        <div class="p-4 border-t border-gray-200">
            <form id="chat-form" class="flex">
                <input type="text" id="user-input" class="flex-1 border border-gray-300 rounded-l-lg p-2 focus:outline-none" placeholder="Type your message...">
                <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded-r-lg hover:bg-blue-600 focus:outline-none">
                    <i class="fas fa-paper-plane"></i>
                </button>
            </form>
        </div>
    </div>

    <script>
        const chatWindow = document.getElementById('chat-window');
        const chatForm = document.getElementById('chat-form');
        const userInput = document.getElementById('user-input');

        chatForm.addEventListener('submit', function(event) {
            event.preventDefault();
            const userMessage = userInput.value.trim();
            if (userMessage) {
                addMessage('user', userMessage);
                userInput.value = '';
                getBotResponse(userMessage);
            }
        });

        function addMessage(sender, message) {
            const messageElement = document.createElement('div');
            messageElement.classList.add('my-2', 'p-2', 'rounded-lg', 'max-w-xs', 'w-fit');
            if (sender === 'user') {
                messageElement.classList.add('bg-blue-100', 'self-end');
                messageElement.innerHTML = `<p class="text-blue-900">${message}</p>`;
            } else {
                messageElement.classList.add('bg-gray-200', 'self-start');
                messageElement.innerHTML = `<p class="text-gray-900">${message}</p>`;
            }
            chatWindow.appendChild(messageElement);
            chatWindow.scrollTop = chatWindow.scrollHeight;
        }

        function getBotResponse(userMessage) {
            // Simulate an AI response (replace with actual AI logic)
            setTimeout(() => {
                const botMessage = `You said: ${userMessage}`;
                addMessage('bot', botMessage);
            }, 1000);
        }
    </script>
</body>
</html>