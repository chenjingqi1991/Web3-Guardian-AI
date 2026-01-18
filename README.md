

---

# 🛡️ Web3-Guardian-AI: Intelligent Circuit Breaker System

This project is a production-grade Web3 security infrastructure that integrates **Real-time Blockchain Monitoring** with **Local LLM-based Intelligence**. It serves as an automated "Guardian" for DeFi protocols or trading bots.

## 🌟 Core Features

* **Real-time Volatility Monitor**: Directly connects to Ethereum Mainnet via Alchemy/Infura to track asset price and gas fee fluctuations.
* **High-Performance State Management**: Uses **Redis** as a low-latency message bus for inter-process communication between the monitor and the AI agent.
* **Edge AI Reasoning**: Powered by **Ollama (Llama 3.2)**, the system analyzes on-chain anomalies and generates human-readable emergency protocols without data leaving the server.
* **Circuit Breaker Pattern**: Implements an automated "kill-switch" status that can be integrated with smart contract `pause()` functions.

## 🏗️ Architecture

1. **Monitoring Layer (`monitor_price.py`)**: Polls on-chain data and detects deviations against a 5% threshold.
2. **Data Layer (Redis)**: Stores the `circuit_breaker:status` and triggers events.
3. **Intelligence Layer (`ai_agent.py`)**: LangChain-orchestrated agent that consumes Redis alerts and performs risk modeling using local LLMs.

---

## 🚀 Deployment on AWS (Ubuntu 24.04)

### Prerequisites

* **AWS Instance**: `m7i-flex.large` (8GB RAM recommended for LLM inference)
* **Engine**: Ollama, Redis-server, Miniconda

### Setup Environment

```bash
conda create -n web3_ai python=3.12 -y
conda activate web3_ai
pip install web3 redis langchain langchain-community

```

### Usage

1. **Start the Monitor**:
```bash
python monitors/monitor_price.py

```
<img width="1967" height="973" alt="image" src="https://github.com/user-attachments/assets/b1123ee1-c51e-458f-98c0-b80161f8e0f0" />


2. **Start the AI Agent**:
```bash
python scripts/ai_agent.py

```
<img width="1978" height="889" alt="2fe65e0a-2b75-4472-9617-c3fea3867fc4" src="https://github.com/user-attachments/assets/5295abe9-a661-4189-be93-69f855ade865" />



## 🛡️ Future Roadmap

* [ ] Implement multi-node RPC load balancing (Nginx).
* [ ] Integrate with Uniswap V3 SDK for automated liquidity removal.
* [ ] Add Telegram/Discord Bot notification hooks.

---
