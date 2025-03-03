# AgriAdapt 🌱

## Overview
AgriAdapt is a **mobile and web platform** that helps African farmers adapt to climate change using **AI, IoT, and blockchain**. The platform provides real-time weather insights, AI-driven crop recommendations, IoT-based water optimization, and blockchain-based sustainability rewards.

---

## Features
✅ **Weather Forecasting:** Get real-time weather insights.  
✅ **Crop Recommendation:** AI-driven crop selection based on climate conditions.  
✅ **Water Optimization:** IoT-based precision irrigation using soil moisture data.  
✅ **Sustainability Rewards:** Blockchain-based incentives for sustainable farming practices.  
✅ **Community Hub:** Peer-to-peer knowledge sharing (future feature).  

---

## Tech Stack
- **Backend:** Flask (Python), PostgreSQL, AI (TensorFlow), IoT (MQTT)  
- **Frontend:** React (Web), React Native (Mobile)  
- **Cloud:** AWS (Hosting, Database, IoT Integration)  
- **Blockchain:** Ethereum/Solana for sustainability rewards  

---

## Installation

### Backend Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/AgriAdapt.git
   cd AgriAdapt/backend
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
3. Set up the database:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```
4. Run the Flask server:
   ```bash
   python run.py
   ```

### Frontend Setup (Web)
1. Navigate to the frontend folder:
   ```bash
   cd ../frontend/web
   ```
2. Install dependencies and start the React app:
   ```bash
   npm install
   npm start
   ```

---

## API Endpoints

### Weather
**GET** `/weather?location=city`  
Get real-time weather data for a specific location.

**Example:**
```bash
curl "http://127.0.0.1:5000/weather?location=Nairobi"
```
**Response:**
```json
{
  "location": "Nairobi",
  "temperature": 293.15,
  "weather": "clear sky"
}
```

### Crop Recommendation
**GET** `/recommend-crop?condition=climate_condition`  
Get AI-recommended crops based on climate conditions.

**Example:**
```bash
curl "http://127.0.0.1:5000/recommend-crop?condition=drought-resistant"
```
**Response:**
```json
{
  "recommended_crop": "Sorghum"
}
```

### IoT Integration
**POST** `/soil-moisture`  
Submit soil moisture data and get irrigation suggestions.

**Example:**
```bash
curl -X POST "http://127.0.0.1:5000/soil-moisture" \
     -H "Content-Type: application/json" \
     -d '{"farmer_id": 1, "moisture_level": 25}'
```
**Response:**
```json
{
  "suggestion": "Irrigate immediately"
}
```

### Blockchain Integration
**POST** `/reward-farmer`  
Reward a farmer with tokens for sustainable practices.

**Example:**
```bash
curl -X POST "http://127.0.0.1:5000/reward-farmer" \
     -H "Content-Type: application/json" \
     -d '{"farmer_address": "0x...", "reward_amount": 10}'
```
**Response:**
```json
{
  "tx_hash": "0x..."
}
```

---

## Roadmap

### Phase 1: MVP Development
✅ Weather API  
✅ Crop Recommendation API  
✅ IoT Integration  
✅ Blockchain Integration  

### Phase 2: Advanced Features
⏳ Mobile App (React Native)  
⏳ Farmer Community Hub  
⏳ Machine Learning for Predictive Analytics  

### Phase 3: Deployment
⏳ Deploy backend on AWS  
⏳ Deploy frontend on Netlify/Vercel  
⏳ Integrate IoT devices  

---

## Contributing
We welcome contributions! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeatureName`).
3. Commit your changes (`git commit -m 'Add some feature'`).
4. Push to the branch (`git push origin feature/YourFeatureName`).
5. Open a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For questions or feedback, reach out to:
📧 Email: misheckgogo45@gmail.com  
🌐 Website:   
🐦 Twitter: [@kingboris28](https://twitter.com/kingboris28)  

---

## Acknowledgments
- OpenWeatherMap for weather data.  
- Ethereum/Solana for blockchain integration.  
- Flask and React communities for amazing tools and libraries.  

---

### **How to Use This README**
1. Replace placeholders (e.g., `yourusername`, `your.email@example.com`) with your actual details.
2. Add a `LICENSE` file if you want to use the MIT License.
3. Update the roadmap and features as your project evolves.

This README provides a professional and comprehensive overview of your project. Let me know if you need further customization! 🚀
