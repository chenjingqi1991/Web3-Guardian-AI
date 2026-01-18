import redis
import time
from langchain_community.llms import Ollama

# 1. 初始化：連接本地 AI 引擎和 Redis
print("🤖 AI Agent 正在啟動，請稍候...")
try:
    llm = Ollama(model="llama3.2:1b")
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    print("✅ AI 引擎與數據通道連接成功！")
except Exception as e:
    print(f"❌ 啟動失敗: {e}")
    exit()

def analyze_risk():
    # 2. 從 Redis 讀取監控狀態
    status = r.get("circuit_breaker:status")
    
    if status == "OPEN":
        reason = r.get("circuit_breaker:reason")
        print(f"\n🚨 [緊急警報] 檢測到 Web3 熔斷！")
        print(f"📝 觸發原因: {reason}")
        
        # 3. 請求 AI 提供專家建議
        prompt = f"""
        你是一位頂級 Web3 安全架構師。
        當前系統觸發了熔斷機制，原因是：{reason}。
        請用中文給出 3 條具體的應急操作建議，以保護協議資產安全。
        """
        
        print("🤔 AI 正在進行風險建模與分析...")
        response = llm.invoke(prompt)
        print("\n--- 🛡️ AI 專家應急建議 ---")
        print(response)
        print("--------------------------")
    else:
        print(f"🟢 {time.strftime('%H:%M:%S')} 監控中：系統運行平穩，無異常風險。")

if __name__ == "__main__":
    # 每 15 秒檢查一次
    while True:
        analyze_risk()
        time.sleep(15)
