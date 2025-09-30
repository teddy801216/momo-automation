### **步驟**：
0. 啟動虛擬環境
python 必須高於 python3.11, 本範例使用 python3.13

``bash
➜  momo-automation python3.13 -m venv momo_venv
➜  momo-automation source momo_venv/bin/activate
```

1. 安裝依賴：
   ```bash
   pip install -r requirements.txt
   ```

2. 輸入在 config.txt 輸入帳號密碼
    ```config.txt
    [MOMO_LOGIN_PAGE]
    momo_account = 
    momo_password =
    ```
--
# Candidate: 羅泰集
# Position: QA Engineer
# Supplement Note

1) Login UI 自動化 + OpenAI API
- 目標: 確認出現 2FA 阻擋
- 程式位置： momo-automation/test/UI/login_test.py
- 執行方式： pytest -vs test/UI/login_test.py
- 運行影片：output.mp4

2) API 測試
- 目標: 要展示 API 測試設計與掌握度
- 程式位置: momo-automation/test/API_test/query_goods_stock_test.py
- 執行方式: pytest -vs test/API_test/query_goods_stock_test.py
- RESTful API，使用假的 host, 詳細思路與驗證重點，將於面試時說明。

--- 
