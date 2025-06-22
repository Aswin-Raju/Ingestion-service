from confluent_kafka import Producer, KafkaError
from fastapi import FastAPI, Header, HTTPException, status
from schemas import SecurityEvent
from config import API_KEY, KAFKA_TOPIC, KAFKA_BOOTSTRAP_SERVERS
from kafka_producer import produce_event

app = FastAPI()


@app.post("/api/v1/events", status_code=202)
async def ingest_event(
    event: SecurityEvent,
    x_api_key: str = Header(..., alias="X-API-KEY")
):
    if x_api_key != API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid API Key")

    produce_event(event.dict(), KAFKA_TOPIC)
    return {"message": "Event accepted"}


@app.get("/health", status_code=200)
async def health():
    try:
        producer = Producer({'bootstrap.servers': KAFKA_BOOTSTRAP_SERVERS})
        producer.poll(0)
        return {"status": "ok", "kafka": "healthy"}

    except KafkaError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Kafka unhealthy: {str(e)}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Kafka unreachable: {str(e)}"
        )
