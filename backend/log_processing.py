from aiokafka import AIOKafkaConsumer
import dask.dataframe as dd
from anomaly_detection import detect_anomalies
import asyncio

async def process_logs():
    consumer = AIOKafkaConsumer("log_topic", bootstrap_servers="localhost:9092")
    await consumer.start()
    try:
        logs = []
        async for msg in consumer:
            logs.append(msg.value.decode("utf-8"))  # Collect logs
            if len(logs) >= 100:  # Process every 100 logs
                df = dd.from_pandas(pd.DataFrame(logs), npartitions=2)
                anomalies = detect_anomalies(df)
                print(f"Anomalies detected: {anomalies}")
                logs.clear()  # Clear buffer
    finally:
        await consumer.stop()
