import { GoogleGenerativeAI } from "@google/generative-ai";

async function AI(data) {
  const genAI = new GoogleGenerativeAI(import.meta.env.VITE_GOOGLE_API_KEY);
  
  const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash",generationConfig: { responseMimeType: "application/json" } });

  const prompt = `It should follow this schema { message: String } and it should be a roast and try to make it fun  ${data}`;

  const result = await model.generateContent([prompt]);
  const response = result.response;
   console.log(response, "sd",typeof response)
  const text = response.text();
  return text; // text is a json object so this function should always return json
}

export default AI;
