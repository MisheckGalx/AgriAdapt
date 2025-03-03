import os

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///agriadapt.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # OpenWeatherMap API key
    OPENWEATHERMAP_API_KEY = os.getenv('OPENWEATHERMAP_API_KEY', 'your_api_key_here')
    
    # Blockchain configuration
    ETHEREUM_NETWORK_URL = os.getenv('ETHEREUM_NETWORK_URL', 'https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID')
