import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from dotenv import load_dotenv

# Load original environment variables
load_dotenv()

raw_url = os.getenv("DATABASE_URL")
if not raw_url:
    print("Warning: DATABASE_URL not found in .env. Initializing with sqlite default for now.")
    DATABASE_URL = "sqlite+aiosqlite:///./test.db"  # Fallback for compilation or local test
else:
    # Ensure the URL uses the asyncpg driver
    if "?" in raw_url:
        base_url = raw_url.split("?")[0]
    else:
        base_url = raw_url
        
    if base_url.startswith("postgresql://"):
        DATABASE_URL = base_url.replace("postgresql://", "postgresql+asyncpg://", 1)
    elif base_url.startswith("postgres://"):
        DATABASE_URL = base_url.replace("postgres://", "postgresql+asyncpg://", 1)
    else:
        DATABASE_URL = base_url

engine = create_async_engine(
    DATABASE_URL, 
    echo=False,
    connect_args={"ssl": "require"} if "neon.tech" in DATABASE_URL else {}
)

async_session_maker = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with async_session_maker() as session:
        yield session
