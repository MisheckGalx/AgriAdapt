from flask import Blueprint, request, jsonify
from web3 import Web3
from app import Config

bp = Blueprint('blockchain', __name__)

# Connect to Ethereum blockchain
web3 = Web3(Web3.HTTPProvider(Config.ETHEREUM_NETWORK_URL))

@bp.route('/reward-farmer', methods=['POST'])
def reward_farmer():
    data = request.json
    farmer_address = data.get('farmer_address')
    reward_amount = data.get('reward_amount', 10)  # Default reward: 10 tokens
    
    # Logic to send tokens to farmer's wallet
    tx_hash = web3.eth.send_transaction({
        'to': farmer_address,
        'from': web3.eth.accounts[0],
        'value': web3.toWei(reward_amount, 'ether')
    })
    
    return jsonify({"tx_hash": tx_hash.hex()})
