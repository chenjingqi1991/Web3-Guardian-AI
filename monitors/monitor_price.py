import time
import redis
from web3 import Web3

# 1. 连接配置
RPC_URL = "https://eth-mainnet.g.alchemy.com/v2/tXwg8mA3Rs-P5jqJMFusJ" # 建议换成你自己的 API Key
w3 = Web3(Web3.HTTPProvider(RPC_URL))
r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# 2. 策略参数
SYMBOL = "ETH"
THRESHOLD = 0.05  # 5% 波动阈值
last_price = None

def get_chain_price():
    # 简化版：实际生产中会调用 Uniswap 或 Chainlink Oracle 合约
    # 这里我们用 block number 模拟一个价格获取动作
    return w3.eth.get_block('latest')['baseFeePerGas'] # 暂用 Gas 费模拟价格波动

def trigger_circuit_breaker(current_p, change):
    print(f"⚠️ [警报] 价格波动过大: {change*100:.2f}%! 触发熔断...")
    r.set("circuit_breaker:status", "OPEN") # 开启熔断
    r.set("circuit_breaker:reason", f"Price volatility {change:.2%}")
    r.expire("circuit_breaker:status", 300) # 5分钟后尝试自动恢复

print(f"🚀 {SYMBOL} 风险监控系统已启动...")
r.set("circuit_breaker:status", "CLOSED") # 初始化状态为关闭（正常）

while True:
    try:
        curr_price = get_chain_price()
        if last_price:
            change = abs(curr_price - last_price) / last_price
            if change > THRESHOLD:
                trigger_circuit_breaker(curr_price, change)
            else:
                print(f"✅ 价格正常: {curr_price} (波动: {change:.4%})")
        
        last_price = curr_price
        time.sleep(10) # 每10秒轮询一次
    except Exception as e:
        print(f"❌ 监控异常: {e}")
        time.sleep(5)
