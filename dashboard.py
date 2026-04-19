import time
import requests

API = "http://localhost:8000"
STORE = "STORE_001"

def fetch():
    try:
        metrics = requests.get(f"{API}/stores/{STORE}/metrics").json()
        funnel = requests.get(f"{API}/stores/{STORE}/funnel").json()
        return metrics, funnel
    except:
        return {}, {}

while True:
    metrics, funnel = fetch()

    print("\n" + "="*50)
    print("📊 LIVE STORE DASHBOARD")
    print("="*50)

    # ✅ FIXED: match your API response keys
    print(f"Visitors: {metrics.get('unique_visitors', 0)}")
    print(f"Transactions: {metrics.get('transactions', 0)}")
    print(f"Conversion: {metrics.get('conversion_rate', 0):.2f}%")

    print("\nFunnel:")
    print(f"Entry: {funnel.get('entry', 0)}")
    print(f"Exit:  {funnel.get('exit', 0)}")

    print("\nUpdating every 5 seconds...")
    time.sleep(5)