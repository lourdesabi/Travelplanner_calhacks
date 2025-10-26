from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import sys
import os
from datetime import datetime

sys.path.append('agents')

from orchestrator import OrchestratorAgent
from team_config import TeamConfig

app = Flask(__name__, static_folder='.')
CORS(app)  # Enable CORS for frontend-backend communication

@app.route('/')
def index():
    # Serve index.html with no-cache headers to prevent caching issues
    response = send_from_directory('.', 'index.html')
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/api/plan-trip', methods=['POST'])
def plan_trip():
    """
    API endpoint to generate a complete travel plan using AI agents
    """
    try:
        data = request.json
        
        # Extract trip details from request
        origin = data.get('origin')
        destination = data.get('destination')
        departure_date = data.get('departureDate')
        return_date = data.get('returnDate')
        passengers = int(data.get('passengers', 2))
        budget = int(data.get('budget', 3000))
        interests = data.get('interests', 'architecture, food, beaches, culture')
        
        # Calculate days
        start = datetime.strptime(departure_date, '%Y-%m-%d')
        end = datetime.strptime(return_date, '%Y-%m-%d')
        days = (end - start).days
        
        if days <= 0:
            return jsonify({'error': 'Return date must be after departure date'}), 400
        
        # Initialize orchestrator and generate plan
        orchestrator = OrchestratorAgent()
        
        # This will coordinate all agents: Flight, Weather, Travel, Links
        plan = orchestrator.plan_complete_trip(
            origin=origin,
            destination=destination,
            departure_date=departure_date,
            return_date=return_date,
            days=days,
            budget=budget,
            interests=interests,
            passengers=passengers
        )
        
        return jsonify({
            'success': True,
            'plan': plan,
            'summary': {
                'origin': origin,
                'destination': destination,
                'days': days,
                'passengers': passengers,
                'budget': budget,
                'totalBudget': budget * passengers
            }
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({'status': 'healthy', 'message': 'Travel Planner API is running'})

if __name__ == '__main__':
    print("🚀 Starting Travel Planner API Server...")
    print("📍 Frontend: http://localhost:5000")
    print("🔌 API: http://localhost:5000/api/plan-trip")
    
    # Get port from environment variable (for deployment) or use 5000 for local
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
