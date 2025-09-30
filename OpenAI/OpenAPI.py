import os
import base64
import pyautogui
from openai import OpenAI
from io import BytesIO
from datetime import datetime
from Actions.Common import Common

common = Common()


class OpenAIHelper:
    def __init__(self):
        GITHUB_TOKEN = common.load_openai_api_token()
        if not GITHUB_TOKEN:
            raise EnvironmentError("請先 export GITHUB_TOKEN")

        self.client = OpenAI(
            base_url="https://models.github.ai/inference",
            api_key=GITHUB_TOKEN,
        )

    def _take_and_save_screenshot(self, save_dir="./ai_debug_screenshots"):
        """擷取畫面並儲存為 PNG 檔案，回傳路徑與 base64 編碼內容"""
        os.makedirs(save_dir, exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        path = os.path.join(save_dir, filename)

        screenshot = pyautogui.screenshot()
        screenshot.save(path)

        buffered = BytesIO()
        screenshot.save(buffered, format="PNG")
        screenshot_b64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

        return path, screenshot_b64

    def _parse_openai_bool_response(self, result: str) -> bool | None:
        cleaned = result.strip().lower()
        if cleaned == "true":
            return True
        elif cleaned == "false":
            return False
        else:
            print(f"⚠️ 無法解析 OpenAI 回覆為布林值：{result}")
            return None

    def compare_screen_with_image(self,
                                  image_path: str,
                                  model="openai/gpt-4.1",
                                  prompt="Compare two images. the one is screenshot of doing login you can find 帳號 & 密碼 & 登入 text other picture is login 2FA you can find error ACT016, please check screenshot conain error ACT016, if yes reply True if not reply False If neither image contains the elements of the other, reply False."):
        screenshot_path, screenshot_b64 = self._take_and_save_screenshot()

        with open(image_path, "rb") as f:
            image_b64 = base64.b64encode(f.read()).decode("utf-8")

        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text",
                                "text": (prompt + "Keep answer short. If really hard to compare beyond True and False, you can say None.")
                            },
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{screenshot_b64}"}},
                            {"type": "image_url", "image_url": {"url": f"data:image/png;base64,{image_b64}"}},
                        ],
                    }
                ],
                timeout=20
            )
            return self._parse_openai_bool_response(result=response.choices[0].message.content.strip())
        except Exception as e:
            print(f"❌ OpenAI 比對失敗：{e}")
            return False
