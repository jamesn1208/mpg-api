from sqlalchemy.orm import Session


async def get_metrics(_: Session) -> dict:
    # Simulate fetching metrics from a database or external service
    return {
        "cpu_usage": 75.5,
        "memory_usage": 65.2,
        "disk_usage": 80.1,
        "network_in": 120.5,
        "network_out": 110.3
    }
