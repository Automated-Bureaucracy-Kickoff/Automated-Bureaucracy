

async function sendingDataToBackend({message, settings}) {
    try {
      let response = await fetch(`${import.meta.env.VITE_BACKEND_URL}/response`, {
        method: "POST",
        body: JSON.stringify({ message: message }),  // Wrap message in an object
        headers: {
          "Content-Type": "application/json"
        },
      });
  
      
      let data = await response.json();
        return data.message;
    } catch {
      return JSON.stringify({message: "Hmm something went wrong❗"});
    }
  }

export default sendingDataToBackend