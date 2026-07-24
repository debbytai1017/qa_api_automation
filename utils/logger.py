import json
import logging
import os

LOG_FOLDER = "logs"
os.makedirs(LOG_FOLDER, exist_ok=True)
# 建立logs資料夾, exist_ok=True 代表若資料夾已存在就不會重複建立而報錯
logging.basicConfig(
    filename=f"{LOG_FOLDER}/api.log", # 指定日誌要寫入的檔案路徑
    level=logging.INFO, # 日誌紀錄層級為INFO (紀錄INFO, WARNING, ERROR)
    format="%(asctime)s %(message)s", # 日誌的格式: 先輸出時間(asctime), 後接訊息內容(message)
    encoding="utf-8"
)

logger = logging.getLogger(__name__)
# 取得目前的logger物件, __name__ 代表當前模組名稱

# 定義一個專門記錄API呼叫細節的函式
def log_api(
        method,
        url,
        headers,
        request_body,
        response
):
    logger.info("=" * 60)
    logger.info(f"Method : {method}") # 記錄HTTP請求方法
    logger.info(f"URL    : {url}") # 記錄請求的目標URL地址
    logger.info("\nHeaders")
    logger.info(
        json.dumps(
            headers,
            indent=4,
            ensure_ascii=False
        )
    ) # 將Request Body轉成縮排4格且支援中文的JSON字串後記錄
    logger.info("\nRequest Body")
    logger.info(
        json.dumps(
            request_body,
            indent=4,
            ensure_ascii=False
        )
    )
    logger.info(f"\nStatus Code : {response.status_code}")
    logger.info("\nResponse")

    try:
        # 將回應內容轉換為JSON格式並做縮排美化輸出
        logger.info(
            json.dumps(
               response.json(),
               indent=4,
               ensure_ascii=False 
            )
        )
    except Exception:
        # 如果回應內容不是JSON格式(例如:純文字或HTML錯誤頁面), 則直接寫入原始文字
        logger.info(response.text)

    logger.info("=" * 60)