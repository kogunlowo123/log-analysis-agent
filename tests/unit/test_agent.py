"""Log Analysis Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_search_logs():
    """Test Search logs with natural language queries translated to log query syntax."""
    tools = AgentTools()
    result = await tools.search_logs(query="test", time_range="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_detect_anomalies():
    """Test Detect anomalous patterns in log streams."""
    tools = AgentTools()
    result = await tools.detect_anomalies(log_source="test", baseline_period="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_correlate_events():
    """Test Correlate events across multiple services using trace IDs."""
    tools = AgentTools()
    result = await tools.correlate_events(trace_id="test", time_window="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_summarize_patterns():
    """Test Summarize recurring log patterns in natural language."""
    tools = AgentTools()
    result = await tools.summarize_patterns(log_source="test", time_range="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.log_analysis_agent_agent import LogAnalysisAgentAgent
    agent = LogAnalysisAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
