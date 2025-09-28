import hashlib
import time

def pow(prefix, difficulty):
    """
    prefix: 昵称
    difficulty: 前导0的数量
    """
    target = "0" * difficulty
    nonce = 0
    start_time = time.time()

    while True:
        text = f"{prefix}{nonce}"
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        if hash_value.startswith(target):
            elapsed = time.time() - start_time
            return nonce, text, hash_value, elapsed
        nonce += 1

if __name__ == "__main__":
    nickname = "drake"

    # 先找到 4 个 0 开头的哈希
    nonce4, text4, hash4, time4 = pow(nickname, 4)
    print(f"难度 4 -> 花费时间: {time4:.4f}s, 内容: {text4}, 哈希: {hash4}")

    # 再找到 5 个 0 开头的哈希
    nonce5, text5, hash5, time5 = pow(nickname, 5)
    print(f"难度 5 -> 花费时间: {time5:.4f}s, 内容: {text5}, 哈希: {hash5}")