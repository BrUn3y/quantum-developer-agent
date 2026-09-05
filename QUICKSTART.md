# 🚀 Quick Start Guide - Quantum Developer Agent

## ⚡ Fast Setup (5 minutes)

### 1. Prerequisites
```bash
# Install uv (if not installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Verify installation
uv --version
```

### 2. Clone & Configure
```bash
# Navigate to the project
cd quantum-developer-agent

# Copy environment template
cp .env.example .env

# Edit .env with your credentials
nano .env  # or use your preferred editor
```

### 3. Required Environment Variables
```env
# Watsonx Credentials (REQUIRED)
WATSONX_API_KEY=your_api_key_here
WATSONX_PROJECT_ID=your_project_id_here

# Local Granite model
OLLAMA_API_BASE=http://127.0.0.1:11434
DEVELOPER_MODEL=ollama:granite4.2:8b
DEVELOPER_HOST=127.0.0.1
DEVELOPER_PORT=8001
```

### 4. Run the Agent

**Option A: Using start script (Recommended)**
```bash
chmod +x start.sh
./start.sh
```

**Option B: Using uv directly**
```bash
uv run server
```

**Option C: Using Python**
```bash
uv sync
python -m quantum_developer_agent.agent
```

### 5. Verify Agent is Running
```bash
# Check agent card
curl http://localhost:8001/.well-known/agent-card.json

# Test with a simple request
curl -X POST http://localhost:8001/jsonrpc/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "message/send",
    "params": {
      "message": {
        "kind": "message",
        "messageId": "51188d1f-1c19-46ed-aad7-e45735bcb0ab",
        "role": "user",
        "parts": [{"kind": "text", "text": "Create a Bell state circuit in QASM"}]
      }
    }
  }'
```

## 🐳 Docker Quick Start

```bash
# Build
docker build -t quantum-developer-agent .

# Run
docker run -p 8001:8001 --env-file .env quantum-developer-agent

# Run in background
docker run -d -p 8001:8001 --env-file .env --name quantum-dev quantum-developer-agent
```

## 📝 Usage Examples

### Generate Quantum Code
```bash
curl -X POST http://localhost:8001/jsonrpc/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "message/send",
    "params": {
      "message": {
        "kind": "message",
        "messageId": "d2741136-e3d7-4f5d-add1-64a46b44db87",
        "role": "user",
        "parts": [{"kind": "text", "text": "Create a superposition circuit with 3 qubits"}]
      }
    }
  }'
```

### Implement Grover's Algorithm
```bash
curl -X POST http://localhost:8001/jsonrpc/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "message/send",
    "params": {
      "message": {
        "kind": "message",
        "messageId": "5557b6a4-276a-4e26-b7b8-1fcdcf9db7e3",
        "role": "user",
        "parts": [{"kind": "text", "text": "Implement Grover'\''s algorithm for 3 qubits"}]
      }
    }
  }'
```

### Explain Quantum Concepts
```bash
curl -X POST http://localhost:8001/jsonrpc/ \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": "1",
    "method": "message/send",
    "params": {
      "message": {
        "kind": "message",
        "messageId": "84780764-e7fb-42a1-91d5-2696a1acbef9",
        "role": "user",
        "parts": [{"kind": "text", "text": "Explain quantum entanglement with an example"}]
      }
    }
  }'
```

## 🔧 Troubleshooting

### Port Already in Use
```bash
# Find process using port 8001
lsof -i :8001

# Kill the process
kill -9 <PID>
```

### Missing Dependencies
```bash
# Reinstall all dependencies
uv sync --reinstall
```

### Watsonx API Errors
- Verify your API key is correct
- Check project ID matches your Watsonx project
- For local inference, run `ollama pull granite4.2:8b`
- Check Watsonx service status

## 📚 What This Agent Does

✅ **Generates quantum code** in QASM 2.0/3.0 and Qiskit
✅ **Explains quantum concepts** with detailed examples
✅ **Implements quantum algorithms** (Grover, Shor, Deutsch-Jozsa, etc.)
✅ **Optimizes quantum circuits** to reduce gates and depth
✅ **Documents code** with helpful comments

## 🔗 Integration

This agent can work:
- **Standalone**: Direct HTTP requests
- **A2A Protocol**: Agent-to-Agent communication
- **Part of Quantum Lab System**: Orchestrated by main agent

## 📖 Full Documentation

See [README.md](README.md) for complete documentation.

---
