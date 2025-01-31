import { useState } from "react";
import { useDispatch } from "react-redux";
import { setSetting } from "../redux/slices/settings";

export default function SettingsComponent() {
  const [numAgents, setNumAgents] = useState(1);
  const [prompts, setPrompts] = useState([""]);
  const [duration, setDuration] = useState("");
  const [model, setModel] = useState("Model 1");
  const [temperature, setTemperature] = useState(1.0);
  const [tools, setTools] = useState({ webSearch: false, notepad: false });
  const dispatch = useDispatch()  
  const handleNumAgentsChange = (e) => {
    const value = Math.max(1, Number(e.target.value));
    setNumAgents(value);
    setPrompts(new Array(value).fill(""));
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
    <>
      <h2 className="text-3xl font-semibold mt-3 p-6 text-[var(--color-primary-text)]">Settings</h2>
      <div className="space-y-3 p-6 -mt-9 mb-14 relative">
        <div>
          <label className="block font-medium text-[var(--color-primary-text)]">No of agents</label>
          <input 
            type="number" 
            value={numAgents} 
            onChange={handleNumAgentsChange} 
            className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]" 
            min="1" 
          />
        </div>
        {prompts.map((prompt, index) => (
          <div key={index}>
            <label className="block font-medium text-[var(--color-primary-text)]">System prompt for Agent {index + 1}</label>
            <textarea 
              value={prompt} 
              onChange={(e) => handlePromptChange(index, e.target.value)} 
              className="w-full bg-[var(--color-secondary-bg)] p-2 rounded border border-[var(--color-secondary-border)]"
            />
          </div>
        ))}
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
    </>
  );
  
}
