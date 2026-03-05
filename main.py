import time
from loguru import logger

for i in range(20):
    logger.success(f"Hello {i} World !!!\n")
    time.sleep(0.3)

print("Selesai")