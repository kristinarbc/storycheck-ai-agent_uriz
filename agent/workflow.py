from langgraph.graph import StateGraph, END
from typing import TypedDict
from agent.llm import get_llm
from agent.prompts import (
    ANALYSIS_PROMPT,
    ACCEPTANCE_CRITERIA_PROMPT,
    TEST_CASES_PROMPT,
    RISK_PROMPT,
    RECOMMENDATIONS_PROMPT
)

llm = get_llm()

class AgentState(TypedDict):
    story: str
    analysis: str
    acceptance_criteria: str
    test_cases: str
    risks: str
    recommendations: str


def analyze_story(state: AgentState) -> AgentState:
    prompt = ANALYSIS_PROMPT.format(story=state["story"])
    result = llm.invoke(prompt)
    state["analysis"] = result.content
    return state


def generate_acceptance_criteria(state: AgentState) -> AgentState:
    prompt = ACCEPTANCE_CRITERIA_PROMPT.format(story=state["story"])
    result = llm.invoke(prompt)
    state["acceptance_criteria"] = result.content
    return state


def generate_test_cases(state: AgentState) -> AgentState:
    prompt = TEST_CASES_PROMPT.format(story=state["story"])
    result = llm.invoke(prompt)
    state["test_cases"] = result.content
    return state


def assess_risks(state: AgentState) -> AgentState:
    prompt = RISK_PROMPT.format(story=state["story"])
    result = llm.invoke(prompt)
    state["risks"] = result.content
    return state


def generate_recommendations(state: AgentState) -> AgentState:
    prompt = RECOMMENDATIONS_PROMPT.format(story=state["story"])
    result = llm.invoke(prompt)
    state["recommendations"] = result.content
    return state


def build_workflow():
    graph = StateGraph(AgentState)

    graph.add_node("analyze", analyze_story)
    graph.add_node("acceptance_criteria", generate_acceptance_criteria)
    graph.add_node("test_cases", generate_test_cases)
    graph.add_node("risks", assess_risks)
    graph.add_node("recommendations", generate_recommendations)

    graph.set_entry_point("analyze")
    graph.add_edge("analyze", "acceptance_criteria")
    graph.add_edge("acceptance_criteria", "test_cases")
    graph.add_edge("test_cases", "risks")
    graph.add_edge("risks", "recommendations")
    graph.add_edge("recommendations", END)

    return graph.compile()