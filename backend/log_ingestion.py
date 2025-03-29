from aiokafka import AIOKafkaProducer
import json
import asyncio

class KafkaProducer:
    def __init__(self):
        self.producer = AIOKafkaProducer(bootstrap_servers="localhost:9092")

    async def start(self):
        await self.producer.start()

    async def send_log(self, log):
        await self.producer.send_and_wait("log_topic", json.dumps(log).encode("utf-8"))

    async def stop(self):
        await self.producer.stop()

kafka_producer = KafkaProducer()
asyncio.run(kafka_producer.start())  # Start producer on app start

async def ingest_log(log):
    await kafka_producer.send_log(log)
