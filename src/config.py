import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    gemini_api_key: str
    sender_email: str
    sender_app_password: str
    recipient_email: str
    arxiv_categories: tuple[str, ...] = (
        "cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.RO", "cs.NE"
    )
    max_papers: int = 3
    summary_max_words: int = 120
    max_message_length: int = 10000
    gemini_model: str = "gemini-3.5-flash"
    request_timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 2.0

    @classmethod
    def from_env(cls) -> "Config":
        return cls(
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
            sender_email=os.getenv("SENDER_EMAIL"),
            sender_app_password=os.getenv("SENDER_APP_PASSWORD"),
            recipient_email=os.getenv("RECIPIENT_EMAIL"),
        )
