from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict, Any
from ..analytics.workflow_monitor import WorkflowMonitor
from ..analytics.compliance_report import ComplianceReport
from ..analytics.data_visualizer import DataVisualizer
from ..agents.multi_agent_manager import MultiAgentManager

# Initialize core components
app = FastAPI()
agent_manager = MultiAgentManager()
workflow_monitor = WorkflowMonitor()
compliance_reporter = ComplianceReport()
visualizer = DataVisualizer()


# Models for API request/response
class AgentRequest(BaseModel):
    name: str
    system_prompt: str
    openai_api_key: str
    tavily_api_key: str
    mlflow_uri: str


class TaskRequest(BaseModel):
    agent_name: str
    task_prompt: str


class WorkflowLogRequest(BaseModel):
    workflow_id: str
    agent_name: str
    activity: str
    status: str


class ComplianceRule(BaseModel):
    type: str
    value: Any


# API Endpoints

@app.post("/agents/")
def create_agent(request: AgentRequest):
    """
    Create a new agent with the specified parameters.
    """
    try:
        agent = agent_manager.create_agent(
            name=request.name,
            system_prompt=request.system_prompt,
            openai_api_key=request.openai_api_key,
            tavily_api_key=request.tavily_api_key,
            mlflow_uri=request.mlflow_uri,
        )
        return {"message": "Agent created successfully", "agent": agent.name}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/agents/")
def list_agents():
    """
    List all active agents.
    """
    return {"agents": list(agent_manager.list_agents().keys())}


@app.post("/tasks/")
def execute_task(request: TaskRequest):
    """
    Execute a task for a specific agent.
    """
    agent = agent_manager.get_agent(request.agent_name)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    result = agent.execute_task(request.task_prompt)
    return {"message": "Task executed successfully", "result": result}


@app.post("/workflows/log/")
def log_workflow(request: WorkflowLogRequest):
    """
    Log an activity for a specific workflow.
    """
    workflow_monitor.log_workflow_activity(
        workflow_id=request.workflow_id,
        agent_name=request.agent_name,
        activity=request.activity,
        status=request.status,
    )
    return {"message": f"Activity logged for workflow {request.workflow_id}"}


@app.get("/workflows/{workflow_id}/summary/")
def get_workflow_summary(workflow_id: str):
    """
    Retrieve a summary of a specific workflow.
    """
    summary = workflow_monitor.get_workflow_summary(workflow_id)
    if "error" in summary:
        raise HTTPException(status_code=404, detail=summary["error"])
    return summary


@app.get("/workflows/{workflow_id}/bottlenecks/")
def detect_workflow_bottlenecks(workflow_id: str, threshold_minutes: int = 10):
    """
    Detect bottlenecks in a workflow based on time thresholds.
    """
    bottlenecks = workflow_monitor.detect_bottlenecks(workflow_id, threshold_minutes)
    return {"bottlenecks": bottlenecks}


@app.post("/compliance/")
def generate_compliance_report(agent_logs: Dict[str, List[Dict[str, Any]]], rules: List[ComplianceRule]):
    """
    Generate a compliance report for agents.
    """
    try:
        report = compliance_reporter.generate_report(agent_logs, [rule.dict() for rule in rules])
        return {"message": "Compliance report generated", "report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/visualization/singleton/")
def visualize_singleton_simulation(data: List[Dict[str, Any]], metric: str):
    """
    Visualize results of a singleton simulation.
    """
    try:
        visualizer.visualize_singleton_simulation(data, metric)
        return {"message": "Visualization rendered"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/visualization/ensemble/")
def visualize_ensemble_simulation(data: List[Dict[str, Any]], metric: str):
    """
    Visualize results of an ensemble simulation.
    """
    try:
        visualizer.visualize_ensemble_simulation(data, metric)
        return {"message": "Visualization rendered"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
