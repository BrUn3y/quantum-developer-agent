#!/bin/bash

echo "=========================================="
echo "🚀 Starting Quantum Developer Agent"
echo "=========================================="
echo ""
echo "📋 Agent Information:"
echo "  🔹 Name: Quantum Developer Agent"
echo "  🔹 Port: 8001"
echo "  🔹 Model: Granite 4.2 8B (Ollama)"
echo "  🔹 Role: Quantum Code Generation & Explanations"
echo ""
echo "=========================================="
echo ""

# Function to check if a port is in use
check_port() {
    if lsof -Pi :$1 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        echo "⚠️  Warning: Port $1 is already in use"
        return 1
    fi
    return 0
}

# Check port before starting
echo "🔍 Checking port 8001..."
check_port 8001
echo ""

# Start Developer Agent
echo "🚀 Starting Quantum Developer Agent on port 8001..."
echo "📦 Using uv to run the agent..."
echo ""
uv run server

echo ""
echo "=========================================="
echo "✅ Quantum Developer Agent started!"
echo "=========================================="
echo ""
echo "📊 Agent Details:"
echo "  🔹 URL: http://127.0.0.1:8001"
echo "  🔹 Model: Granite 4.2 8B (Ollama)"
echo "  🔹 Specialty: Quantum Code Generation"
echo ""
echo "=========================================="
echo ""
echo "💡 Tips:"
echo "  - This agent generates QASM and Qiskit code"
echo "  - Explains quantum computing concepts"
echo "  - Implements quantum algorithms (Grover, Shor, etc.)"
echo "  - Press Ctrl+C to stop the agent"
echo ""
echo "=========================================="
