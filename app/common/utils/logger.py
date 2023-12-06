import sys
import logging
import structlog

def disable_uvicorn_logs() -> None:
    uvicorn_access = logging.getLogger("uvicorn.access")
    uvicorn_access.disabled = True

def setup_logging() -> None:
    disable_uvicorn_logs()

    shared_processors = [
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(key="time", fmt="iso"),
    ]

    if sys.stderr.isatty():
        processors = shared_processors + [
            structlog.dev.ConsoleRenderer(),
        ]
    else:
        processors = shared_processors + [
            structlog.processors.dict_tracebacks,
            structlog.processors.EventRenamer("message"),
            structlog.processors.JSONRenderer(),
        ]

    structlog.configure(processors)
