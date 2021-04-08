from aws_embedded_metrics import metric_scope

import logging
import time

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


@metric_scope
def my_handler(metrics):
    metrics.set_property("AccountId", "123456789012")
    metrics.set_property("RequestId", "422b1569-16f6-4a03-b8f0-fe3fd9b100f8")
    metrics.set_property("DeviceId", "61270781-c6ac-46f1-baf7-22c808af8162")
    metrics.set_property(
        "Payload", {"sampleTime": 123456789, "temperature": 273.0, "pressure": 101.3}
    )
    metrics.put_dimensions({"ApplicationVersion": "1.0"})
    metrics.put_metric("ProcessingLatency", 100, "Milliseconds")
    metrics.put_metric("ProcessingLatency", 200, "Milliseconds")

    return {"message": "Hello!"}


time.sleep(30)
my_handler()

log.info("Example completed.")
