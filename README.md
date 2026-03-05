# 👨‍💻 Quantum Developer Agent

Expert agent in quantum code generation and quantum computing concept explanations.

## 🎯 Overview

The Quantum Developer Agent is a specialized AI agent that generates quantum code (QASM and Qiskit), explains quantum computing concepts, and implements classical quantum algorithms like Grover, Shor, Deutsch-Jozsa, and more.

### Key Features

- 🔬 **Quantum Code Generation**: Creates clean and efficient QASM 2.0/3.0 and Qiskit code
- 📚 **Concept Explanations**: Provides detailed explanations of quantum computing concepts
- 🧮 **Algorithm Implementation**: Implements classical quantum algorithms (Grover, Shor, Deutsch-Jozsa, QFT, etc.)
- ⚡ **Code Optimization**: Suggests optimizations to reduce gates and circuit depth
- 📖 **Documentation**: Generates well-documented code with helpful comments

## 🏗️ Architecture

- **Model**: Mistral Large 2 (Watsonx)
- **Port**: 8001
- **Type**: AgentStack Server with A2A protocol
- **Tools**: None (Pure LLM for code generation)
- **Framework**: BeeAI + Watsonx + A2A

## 📋 Prerequisites

- Python 3.11+
- IBM Watsonx account with API key

## 📦 Project Dependencies

### Main Dependencies (pyproject.toml)

```toml
[project]
requires-python = ">=3.11,<4.0"
dependencies = [
    "agentstack-sdk==0.4.0rc1",      # Framework for creating agents
    "beeai_framework>=0.1.76",        # BeeAI Framework for agents
    "python-dotenv>=1.0.0",           # Environment variable management
]
```

### System Dependencies

1. **Python 3.11+**
   ```bash
   python --version  # Must be 3.11 or higher
   ```

2. **uv** (Package Manager - Recommended)
   ```bash
   # Install uv
   curl -LsSf https://astral.sh/uv/install.sh | sh
   
   # Verify installation
   uv --version
   ```

3. **IBM Watsonx** (Credentials required)
   - Watsonx API Key
   - Watsonx Project ID
   - Get them at: https://cloud.ibm.com/

## 🎯 Specific Purpose

This agent is the **quantum code generation specialist** of the multi-agent system:

**Responsibilities:**
- ✅ Generate clean and efficient QASM 2.0/3.0 code
- ✅ Create documented Qiskit code
- ✅ Explain quantum computing concepts
- ✅ Implement classical quantum algorithms
- ✅ Optimize quantum circuits
- ✅ Provide educational examples

**Does NOT:**
- ❌ Does not execute circuits (use Computing Agent for that)
- ❌ Does not query backend status (use Status Agent)
- ❌ Does not retrieve job results (use Status Agent)

**Communication:**
- Receives requests via A2A from Operations Agent (port 8000)
- Responds with QASM/Qiskit code and explanations
- Can be invoked directly on port 8001

- `uv` package manager (recommended) or `pip`

## 🚀 Quick Start

### 1. Clone and Setup

```bash
cd quantum-developer-agent

# Install dependencies
uv sync
# or
pip install -e .
```

### 2. Configure Environment

Create `.env` file from template:

```bash
cp .env.example .env
```

Edit `.env` with your credentials:

```env
# Watsonx
WATSONX_API_KEY=your_watsonx_api_key_here
WATSONX_PROJECT_ID=your_project_id_here
WATSONX_API_URL=https://us-south.ml.cloud.ibm.com/ml/v1/text/chat?version=2023-05-29

# Developer Agent Configuration
WATSONX_DEVELOPER_MODEL=mistralai/mistral-large-2
DEVELOPER_HOST=127.0.0.1
DEVELOPER_PORT=8001
```

### 3. Start the Agent

```bash
# Using the start script (recommended)
./start.sh

# Or directly with uv
uv run server

# Or with Python
python -m quantum_developer_agent.agent
```

### 4. Verify Agent is Running

```bash
curl http://localhost:8001/.well-known/agent-card.json
```

## 💬 Usage Examples

### Example 1: Generate a Bell State Circuit

```bash
curl -X POST http://localhost:8001 \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{
      "role": "user",
      "content": "Create a Bell state circuit in QASM"
    }]
  }'
```

**Response includes:**
- Complete QASM 2.0 code
- Detailed explanation of the circuit
- Expected measurement results
- Practical applications

### Example 2: Implement Grover's Algorithm

```bash
curl -X POST http://localhost:8001 \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{
      "role": "user",
      "content": "Implement Grover'\''s algorithm for 3 qubits"
    }]
  }'
```

**Response includes:**
- Complete Grover's algorithm implementation
- Oracle and diffuser components
- Step-by-step explanation
- Quantum advantage analysis

### Example 3: Explain Quantum Concepts

```bash
curl -X POST http://localhost:8001 \
  -H "Content-Type: application/json" \
  -d '{
    "messages": [{
      "role": "user",
      "content": "Explain what quantum entanglement is"
    }]
  }'
```

**Response includes:**
- Detailed 3-4 paragraph explanation
- QASM code example demonstrating entanglement
- How the code works
- Practical applications

## 🧮 Supported Algorithms

The agent has deep knowledge of these quantum algorithms:

### Search & Optimization
- **Grover's Algorithm**: Quantum search with O(√N) complexity
- **Amplitude Amplification**: Generalization of Grover

### Function Analysis
- **Deutsch-Jozsa Algorithm**: Determine if function is constant or balanced
- **Bernstein-Vazirani Algorithm**: Find hidden binary string
- **Simon's Algorithm**: Find period of function with hidden symmetry

### Transforms & Factorization
- **Quantum Fourier Transform (QFT)**: Quantum analog of DFT
- **Shor's Algorithm**: Integer factorization in polynomial time

### Basic Circuits
- Bell States, GHZ States, W States
- Quantum Teleportation
- Superdense Coding
- Swap Test

## 🔧 Development

### Project Structure

```
quantum-developer-agent/
├── src/
│   └── quantum_developer_agent/
│       ├── __init__.py
│       └── agent.py          # Main agent implementation
├── .env.example              # Environment template
├── .gitignore               # Git ignore rules
├── Dockerfile               # Docker configuration
├── pyproject.toml           # Project dependencies
├── start.sh                 # Start script
└── README.md                # This file
```

### Dependencies

```toml
dependencies = [
    "agentstack-sdk==0.4.0rc1",
    "beeai_framework>=0.1.76",
    "python-dotenv>=1.0.0",
]
```

### Running with Docker

```bash
# Build image
docker build -t quantum-developer-agent .

# Run container
docker run -p 8001:8001 --env-file .env quantum-developer-agent

# Run in background
docker run -d -p 8001:8001 --env-file .env --name quantum-dev quantum-developer-agent

# View logs
docker logs -f quantum-dev

# Stop container
docker stop quantum-dev
```

### Running with uv

The project is configured to use `uv` for dependency management and execution:

```bash
# Install dependencies
uv sync

# Run the server
uv run server

# Run with custom port
DEVELOPER_PORT=9001 uv run server
```

## 🔗 Integration with Other Agents

This agent is designed to work as part of the Quantum Lab Agent System:

- **Invoked by**: Quantum Lab Agent (Port 8000)
- **Communication**: A2A protocol (Agent-to-Agent)
- **Purpose**: Generate quantum code when requested by the orchestrator

### Standalone Usage

While designed for A2A communication, the agent can also be used standalone:

```python
import requests

response = requests.post(
    "http://localhost:8001",
    json={
        "messages": [{
            "role": "user",
            "content": "Create a superposition circuit"
        }]
    }
)

print(response.json())
```

## 🐛 Troubleshooting

### Agent Won't Start

**Problem:** Port already in use

```bash
# Find process using port 8001
lsof -i :8001

# Kill process
kill -9 <PID>
```

**Problem:** Missing dependencies

```bash
# Reinstall dependencies
uv sync --reinstall
```

### Agent Not Responding

**Problem:** Watsonx API errors

- Check your API key in `.env`
- Verify project ID is correct
- Check Watsonx service status
- Ensure you have access to Mistral Large model

### Code Generation Issues

**Problem:** Agent generates wrong algorithm

- Be specific in your request
- Use exact algorithm names (e.g., "Grover's algorithm" not "search algorithm")
- The agent is trained to distinguish between different algorithms

## 🔗 Related Repositories

This agent is part of the Quantum Computing Multi-Agent System. Here are the related repositories:

- **[Quantum Computing Agent](https://github.ibm.com/Edgar-Castaneda/quantum-computing-agent)** - Circuit execution specialist
- **[Quantum Status Agent](https://github.ibm.com/Edgar-Castaneda/quantum-status-agent)** - Status monitoring and job tracking
- **[Quantum Developer Agent](https://github.ibm.com/Edgar-Castaneda/quantum-developer-agent)** - Code generation and algorithm implementation (this repository)
- **[Quantum Operations Agent](https://github.ibm.com/Edgar-Castaneda/quantum-lab-agent)** - Main orchestrator coordinating all agents

## 📚 Additional Resources

- [BeeAI Framework Documentation](https://github.com/i-am-bee/beeai-framework)
- [Qiskit Documentation](https://qiskit.org/documentation/)
- [OpenQASM Specification](https://github.com/openqasm/openqasm)
- [Watsonx Documentation](https://www.ibm.com/products/watsonx-ai)

## 🤝 Contributing

This agent is part of the Quantum Lab Agent System. For contributions, please refer to the main system repository.

## 📄 License

Apache 2.0 License

## 🙏 Acknowledgments

- Built with [BeeAI Framework](https://github.com/i-am-bee/beeai-framework)
- Powered by [IBM Watsonx](https://www.ibm.com/products/watsonx-ai)
- LLM: Mistral Large 2

---
