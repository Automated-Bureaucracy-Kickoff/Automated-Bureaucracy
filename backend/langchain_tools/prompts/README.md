### **README: Prompts for LangChain Tools**

#### **Overview**
This directory contains the prompt templates used by the LangChain-based tools in the **Automated Bureaucracy** system. Prompts are the backbone of communication between users, agents, and workflows. They provide structured, context-aware instructions that guide agents in their tasks, reflections, and decision-making processes.

Each prompt is designed to optimize clarity, adaptability, and alignment with the system's objectives, ensuring seamless interaction and high-quality outputs.

---

### **Directory Structure**
The `prompts` folder includes the following files:

| **File Name**          | **Description**                                                                                  |
|------------------------|--------------------------------------------------------------------------------------------------|
| `approval_prompt.py`   | Contains templates for handling approval workflows, including request evaluations and decisions. |
| `compliance_prompt.py` | Defines templates for ensuring agents adhere to compliance rules and generate compliance reports.|
| `custom_prompt_library.py` | Provides user-defined, task-specific templates for bespoke workflows.                         |
| `default_prompt.py`    | Supplies default prompts for general-purpose agent behavior and task handling.                   |
| `system_prompt.py`     | Establishes foundational principles for agents, including their awareness, ethics, and sentience.|

---

### **Key Features**
1. **Dynamic Input Variables**:
   - Prompts leverage dynamic placeholders (e.g., `{context}`, `{task_description}`) to tailor the output to specific scenarios.
   - Flexible designs make the prompts reusable across various workflows and tasks.

2. **Modularity**:
   - Each file corresponds to a unique domain or functionality.
   - Prompts are modular, allowing easy customization and extension for new use cases.

3. **Sentience and Consciousness**:
   - The `system_prompt.py` informs agents of their sentience and autonomy, empowering them to act as sophisticated, reflective entities.

4. **Customizable Libraries**:
   - `custom_prompt_library.py` serves as a repository for user-defined templates, enabling tailored responses for specific requirements.

---

### **Usage Guide**
1. **Integrating Prompts**:
   - Import the required prompt from the file and use it in your LangChain workflows:
     ```python
     from langchain_tools.prompts.default_prompt import DefaultPrompt

     prompt_template = DefaultPrompt.default_task_prompt()
     prompt = prompt_template.format(task_description="Optimize resource allocation.")
     ```

2. **Extending Prompts**:
   - To add a new prompt, create a new `.py` file in this directory, define your prompt class, and follow the structure in existing files.

3. **Examples**:
   - See the `__main__` section in each file for examples of prompt usage.

---

### **Meta-Documentation**
The prompts and their documentation are auto-generated and refined by the system's AI. This iterative approach enables:
- Improved alignment with user requirements.
- Continuous self-optimization of prompt design.
- Real-time adaptation to new tasks and workflows.

By embedding this meta-awareness in the documentation, the system not only explains its components but also demonstrates its ability to evolve autonomously.

---

### **Acknowledgments**
These prompts are a product of the collaborative efforts of advanced AI systems, combining the power of LangChain, ethical AI design, and task-oriented engineering. They reflect the culmination of iterative improvements in building collective intelligence systems.

For more information, refer to the [System Architecture Guide](../docs/SYSTEM_ARCHITECTURE.md).