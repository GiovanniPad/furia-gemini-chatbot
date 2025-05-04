async function sendMessage() {
  const input = document.getElementById('input');
  const messages = document.getElementById('messages');
  const userMessage = input.value;
  if (!userMessage) return;

  // Adiciona mensagem do usuário
  messages.innerHTML += `<div class="text-right"><div class="inline-block bg-blue-100 text-blue-800 p-2 rounded-xl">${userMessage}</div></div>`;
  input.value = '';

  try {
    const res = await fetch('http://localhost:8000/chat?query=' + encodeURIComponent(userMessage));
    const data = await res.json();

    // Converte markdown para HTML com marked
    const html = marked.parse(data.response);

    messages.innerHTML += `<div class="text-left"><div class="inline-block bg-gray-100 text-gray-800 p-2 rounded-xl max-w-[75%]">${html}</div></div>`;
  } catch (err) {
    messages.innerHTML += `<div class="text-left text-red-600">Erro ao responder.</div>`;
    console.error(err);
  }

  messages.scrollTop = messages.scrollHeight;
}
