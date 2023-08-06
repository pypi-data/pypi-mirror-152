import aioredis
from .rmq import Rmq
from .reply import Reply
from typing import Callable


class Message:
    def __init__(
        self,
        callback: Callable,
        queue: str,
        redis_reply: aioredis.Redis,
        shared_rmq: Rmq,
    ) -> None:
        self.callback = callback
        self.queue = queue
        self.redis_reply = redis_reply
        self.shared_rmq = shared_rmq

    async def process(self, message: dict):
        # print(msg_body)
        result = await self.callback(
            queue=self.queue,
            data=message["data"],
        )

        if result is None:
            return

        reply_to = message["reply_to"]
        reply_async = message["reply_async"]
        reply_method = message["reply_method"]
        async_payload = (
            message["async_payload"]
            if message.get("async_payload")
            else message["data"].get("async_payload")
        )

        reply = Reply(redis_reply=self.redis_reply, shared_rmq=self.shared_rmq)
        try:
            if reply_async:
                if result:
                    if async_payload:
                        result["async_payload"] = async_payload
                        await reply.send(
                            msg=result, queue=f"{self.queue}-async"
                        )
            else:
                if reply_method == "rmq":
                    await reply.send(msg=result, queue=reply_to)
                if reply_method == "redis":
                    await reply.send_redis(msg=result, queue=reply_to)
        except Exception:
            pass
        return
