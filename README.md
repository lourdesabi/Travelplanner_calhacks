# Travelplanner CalHacks

A collection of agents that collaborate to generate travel itineraries with live weather context and flight search assistance.

## Prerequisites
- Python 3.10 or newer

## Project Setup
1. Create a virtual environment in the project root:
   ```bash
   python3 -m venv venv
   ```
2. Activate the environment:
   - macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - Windows (PowerShell):
     ```powershell
     venv\Scripts\Activate.ps1
     ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Environment Variables
1. Copy the example file and fill in your credentials:
   ```bash
   cp .env.example .env
   ```
2. Update `.env` with valid API keys:
   - `OPENAI_API_KEY`
   - `ANTHROPIC_API_KEY`
   - `OPENWEATHER_API_KEY`

All agents load variables via `python-dotenv`, so keep the `.env` file in the project root. The actual `.env` file is ignored by git to keep secrets out of version control.

## Running the Agents
- **Flight search assistant**:
  ```bash
  python agents/flightagent.py
  ```
- **Weather agent** (stand-alone check):
  ```bash
  python agents/weather_agent.py
  ```
- **Full orchestrator demo**:
  ```bash
  python agents/orchestrator.py
  ```

Make sure the virtual environment is activated before running any scripts so they can access the installed dependencies and the `.env` configuration.
