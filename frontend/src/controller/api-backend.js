async function sendingDataToBackend({ message, settings }) {
  let system_prompt_analytica = settings.prompts[0]
  let system_prompt_creativa = settings.prompts[1]
  let system_prompt_pragmatica = settings.prompts[2]
  let user_prompt = message
  try {
    let response = await fetch(
      `${import.meta.env.VITE_BACKEND_URL}/multiAgent`,
      {
        method: "POST",
        body: JSON.stringify({ system_prompt_analytica,system_prompt_creativa,system_prompt_pragmatica,user_prompt }),
        headers: {
          "Content-Type": "application/json",
        },
      }
    );
    let data = await response.json();
    
    return data.message;
  } catch {
    return JSON.stringify({ message: "Hmm something went wrong❗" });
  }
}

export default sendingDataToBackend;
