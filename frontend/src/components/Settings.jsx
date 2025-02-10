import { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { setSetting } from "../redux/slices/settings";

export default function SettingsComponent() {
  const [numAgents, setNumAgents] = useState(3);
  const [prompts, setPrompts] = useState(["you are intelligent and be concise in 100 words","you are creative  and be concise in 100 words","you are practical and and be concise in 100 words"]);
  const [duration, setDuration] = useState("");
  const [model, setModel] = useState("Model 1");
  const [temperature, setTemperature] = useState(1.0);
  const [tools, setTools] = useState({ webSearch: false, notepad: false });
  
  const dispatch = useDispatch()  
  const handleNumAgentsChange = (e) => {
    const value = Math.max(1, Number(e.target.value));
    // setNumAgents(3);
    // setPrompts(new Array(3).fill(""));
  };

  const handlePromptChange = (index, value) => {
    const newPrompts = [...prompts];
    newPrompts[index] = value;
    setPrompts(newPrompts);
  };

  const handleSave = () => {
    const settings = {
      numAgents,
      prompts,
      duration,
      model,
      temperature,
      tools
    };
    console.log("Saved settings:", settings);
    dispatch(setSetting(settings))
  };

  return (
    <div className="flex flex-col min-h-[100%]   min-w-[90%] text-[var(--color-primary-text)] dark:text-[var(--color-primary-text)] rounded-[12px] mr-9 p-2 overflow-y-scroll -mt-9   ">
     
      <h2 className="text-3xl font-semibold  p-6 pb-0 text-[var(--color-primary-text)]">Settings</h2>
      <div className="space-y-3 p-6  relative">
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">No of agents</label>
          <input 
            type="number" 
            value={numAgents} 
            onChange={handleNumAgentsChange} 
            className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]" 
            max="3"
            
          />
        </div>
        <div className="grid grid-cols-2">
        {prompts.map((prompt, index) => (
          <div key={index}>
            <label className="block font-medium text-[var(--color-primary-text)]">System prompt for Agent {index + 1}</label>
            <textarea 
              defaultValue={prompt} 
              onChange={(e) => handlePromptChange(index, e.target.value)} 
              className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]"
            />
          </div>
         
        ))}
         </div>
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">Durations / Cycle</label>
          <input 
            type="text" 
            value={duration} 
            onChange={(e) => setDuration(e.target.value)} 
            className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]" 
          />
        </div>
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">Model Dropdown</label>
          <select 
            value={model} 
            onChange={(e) => setModel(e.target.value)} 
            className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]"
          >
            <option>Model 1</option>
            <option>Model 2</option>
          </select>
        </div>
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">Temperature</label>
          <input 
            type="range" 
            min="0" 
            max="2" 
            step="0.1" 
            value={temperature} 
            onChange={(e) => setTemperature(Number(e.target.value))} 
            className="w-full" 
          />
        </div>
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">Tools Checkboxes</label>
          <div className="flex flex-col">
            <label className="inline-flex items-center text-[var(--color-primary-text)]">
              <input 
                type="checkbox" 
                checked={tools.webSearch} 
                onChange={(e) => setTools({ ...tools, webSearch: e.target.checked })} 
                className="mr-2" 
              /> Web Search
            </label>
            <label className="inline-flex items-center text-[var(--color-primary-text)]">
              <input 
                type="checkbox" 
                checked={tools.notepad} 
                onChange={(e) => setTools({ ...tools, notepad: e.target.checked })} 
                className="mr-2" 
              /> Internal Notepad
            </label>
          </div>
        </div>
        <button 
          onClick={handleSave} 
          className="mt-6 text-2xl absolute right-0 bottom-1 text-[var(--color-button-text)] font-bold py-2 px-4 rounded bg-[var(--color-button-bg)] hover:bg-[var(--color-button-hover-bg)] animate-pulse"
        >
          Save
        </button>
      </div>
    </div>
  );
  
}
