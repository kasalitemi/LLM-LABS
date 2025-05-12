# LLM-LABS
AI Learning Path LLM Labs 
# LLM Cybersecurity Projects

Two hands-on projects demonstrating the application of Large Language Models (LLMs) in cybersecurity workflows.

## Project Overview

This repository contains two practical implementations of AI/ML in cybersecurity contexts:
1. **Local LLM for Security Log Analysis** - Private threat detection using Microsoft Phi-3
2. **AI-Powered Phishing Detector** - Cloud-based analysis with OpenAI API

## Projects

### 1. Local LLM Security Analysis 🔒
**File**: `local_llm_analysis.py`

A privacy-preserving solution for analyzing security logs using quantized LLMs running locally.

#### Key Features:
- Runs completely offline
- Processes sensitive security logs privately
- Identifies brute-force attacks and suspicious patterns
- Built with Transformers library and Microsoft Phi-3

### 2. AI Phishing Detector 🛡️
**File**: `phishing_detector_app.py`

Cloud-based AI application for identifying phishing attempts in email content using OpenAI's GPT-4 model.

#### Key Features:
- Real-time phishing analysis
- Gradio web interface
- Example-based testing
- API-based integration pattern

## Prerequisites

- Python 3.8+
- Git
- OpenAI API Key (for Phishing Detector)
- Minimum Hardware for Local LLM:
  - 8GB RAM (16GB recommended)
  - 4GB Disk Space

## Installation

1. Clone repository:
```
git clone https://github.com/<your-username>/llm-cybersecurity-projects.git
cd llm-cybersecurity-projects
```
Create and activate virtual environment:
```
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate  # Windows
```
Install dependencies:

`pip install -r requirements.txt`

# Usage
Local LLM Security Analysis


python local_llm_analysis.py

# Example log entry analysis:
"""
2024-05-20 12:34:56 [ALERT] Failed login attempts: 15 from IP 192.168.1.100
User: admin, Source: SSH
"""
# AI Phishing Detector
Add OpenAI API key to environment variables:

`export OPENAI_API_KEY='your-api-key-here`
Launch Gradio interface:


`python phishing_detector_app.py`
Access web interface at http://localhost:7860

# Security Best Practices
API Key Management
Never commit API keys to version control
Use environment variables for sensitive credentials
Rotate keys regularly
Data Handling
Only use non-sensitive data with cloud models
Encrypt local model weights and logs
Use secure directories (chmod 700 for config files)
Monitoring
Set up API usage alerts
Review model outputs for false positives/negatives
Implement rate limiting for production deployments

# Contributing
Contributions are welcome! Please follow these guidelines:
Open an issue to discuss proposed changes
Create a feature branch
Add tests for new functionality
Update documentation accordingly

# License
MIT License - See LICENSE for details

# Acknowledgements
Microsoft for Phi-3 model
OpenAI for GPT-4 API
Hugging Face Transformers library
Gradio for UI components

