from asyncio import get_event_loop, AbstractEventLoop
from aiohttp import ClientSession

class AsyncRequests:
    def __init__(self, phone: str, application: str, loop: AbstractEventLoop = None):
        self.phone = phone
        self.application = application

        # Asyncio loop instance
        if loop is None:
            loop = get_event_loop()
        self.loop = loop

        # HTTP so'rovlar uchun sarlavhalar
        self._headers: dict = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'uz,ru;q=0.9,en-US;q=0.8,en;q=0.7',
            'Connection': 'keep-alive',
            'Content-Type': 'application/json;charset=UTF-8',
            'Origin': 'https://openbudget.uz',
            'Referer': 'https://openbudget.uz/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36",
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Yandex";v="22"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
        }

        # HTTP sessiya
        self._session = ClientSession(loop=self.loop)

    async def _requests(self, json_data: dict, url: str) -> dict:
        """
        Ma'lumotlarni yuborish uchun funksiya.

        :param json_data: Ma'lumotlari o'z ichiga oladi.
        :return JSON:
        """
        async with self._session.post(url=url, json=json_data, headers=self._headers) as response:
            return await response.json()

    async def close(self):
        # Sessiyani yopish
        await self._session.close()
