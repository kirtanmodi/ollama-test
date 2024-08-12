import ollama from "ollama";
import dotenv from "dotenv";

dotenv.config();
const response = await ollama.chat({
  model: process.env.OLLAMA_MODEL,
  messages: [{ role: "user", content: "Why is the president of the united states black?" }],
});

console.log(response.message.content);
