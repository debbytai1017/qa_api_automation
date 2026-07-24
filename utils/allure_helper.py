import json
import allure

# 定義附加API請求內容(Request Body)的函式
def attach_request(request_body):
    allure.attach(
        json.dumps(
            request_body,
            indent=4,
            ensure_ascii=False
        ), # 將字典轉成縮排4格且支援中文的JSON字串
        name="Request Body", # 報告中顯示的副標題名稱
        attachment_type=allure.attachment_type.JSON # 指定附件類型為JSON
    )
# 定義附加API回應內容(Response)的函式
def attach_response(response):
    try:
        body = json.dumps(
            response.json(),
            indent=4,
            ensure_ascii=False
        )
        attachment_type = allure.attachment_type.JSON
    except Exception:
        # 如果回應內容不是JSON格式
        body = response.text # 取得原始文字內容
        attachment_type = allure.attachment_type.TEXT # 將附件型態設為純文字

    allure.attach(
        body, # 附加在報告上的回應內容(JSON字串或純文字))
        name="Response",
        attachment_type=attachment_type # 帶入上面判斷好的附件類型(JSON/TEXT)
    )
# 定義附加SQL查詢語法的函式
def attach_sql(sql):
    allure.attach(
        sql, # 附加在報告上的SQL指令字串
        name="SQL",
        attachment_type=allure.attachment_type.TEXT # 指定附件類型為純文字
    )