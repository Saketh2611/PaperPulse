import os
from dataclasses import dataclass
from dotenv import load_dotenv

load_dotenv()

@dataclass(frozen=True)
class Config:
    groq_api_key: str
    sender_email: str
    sender_app_password: str
    recipient_email: str
    arxiv_categories: tuple[str, ...] = (
        "cs.AI", "cs.CL", "cs.LG", "cs.CV", "cs.RO", "cs.NE"
    )
    max_papers: int = 3
    summary_max_words: int = 120
    max_message_length: int = 10000
    groq_model: str = "llama-3.3-70b-versatile"
    request_timeout: int = 30
    max_retries: int = 3
    retry_delay: float = 2.0

    @classmethod
    def from_env(cls) -> "Config":
        # Extract variables
        groq_api_key = os.getenv("GROQ_API_KEY")
        sender_email = os.getenv("SENDER_EMAIL")
        sender_app_password = os.getenv("SENDER_APP_PASSWORD")
        recipient_email = os.getenv("RECIPIENT_EMAIL")

        # Validate that required keys are present
        if not all([groq_api_key, sender_email, sender_app_password, recipient_email]):
            raise ValueError(
                "Missing one or more required environment variables. "
                "Please ensure GROQ_API_KEY, SENDER_EMAIL, SENDER_APP_PASSWORD, "
                "and RECIPIENT_EMAIL are set in your .env file."
            )

        return cls(
            groq_api_key=groq_api_key,
            sender_email=sender_email,
            sender_app_password=sender_app_password,
            recipient_email=recipient_email,
        )