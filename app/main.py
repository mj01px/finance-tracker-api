# app/main.py
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import Base, engine
from app.routes import expense, income, tag
from app.routes import balance as balance_router

# Import models to ensure metadata registration
from app.models import expense as expense_model  # noqa: F401
from app.models import tag as tag_model          # noqa: F401

try:
    from app.models import income as income_model  # noqa: F401
except Exception:
    pass


# --- 🕷️ Signature Function ---
def print_signature(url: str):
    """
    Prints an ASCII signature when the server starts.
    """
    spidey = r"""
⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠤⠤⢤⠤⢤⣀⠀⠀⠀⠀⠀⠰⠻⠙
⠀⠀⠈⠒⢌⠢⠀⠀⠀⡐⢀⠄⢠⣶⣿⣡⠤⡶⠣⣄⣀⠜⠛⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠎⢰⣿⣿⡇⢀⣸⡁⠀⡴⠉⢢⣦⡱⣳⡀⠀⠀⠀⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⢀⡿⣿⣿⡏⢁⡇⢈⠟⢦⣠⣴⠟⣿⣸⣇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⢿⣿⣹⣉⠟⣲⠾⠋⠀⠀⢸⣗⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠈⢿⣿⣾⠟⠁⠀⠀⠀⠀⢸⣿⡟⠀⡆⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⢠⣿⣿⡿⡄⠀⠀⠀⠀⠀⣼⣿⠃⢰⢸⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣶⣿⣿⠷⡿⡟⣦⣀⠀⣠⣼⣿⠏⠀⠀⠁⠀⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⡿⠟⡟⢻⣈⡽⢟⣛⣿⠏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⠟⣷⠊⢻⣄⣴⣿⡏⠀⠀⠀⠀⠀⠀⠀
⣀⡤⡤⠤⣄⡀⠀⢀⣀⣀⣀⣀⣼⣿⣝⣓⣾⣮⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠄⡀
⠖⠚⠛⣫⣿⠿⠟⣟⣻⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⢿⣿⠀⠀⠀⠀⠀⠀⠻⡪
⠒⢲⠉⢀⡠⠷⠮⣁⠬⠛⣿⣽⢿⡁⠸⡿⠚⢲⣿⣏⣎⢿⡄⠀⠀⠀⠀⠀⠀⠈
⠀⣿⣖⡁⠀⣠⠞⠉⠑⢢⣷⣽⣳⣿⡾⠤⠤⢈⣟⠂⠱⡀⣿⢦⡀⠀⠀⠀⠀⠀
⢀⡇⠀⣹⠾⢥⣀⣀⣰⠋⢷⣝⠻⣯⣳⣄⣀⡀⢹⠉⠉⠻⡚⢲⡷⣦⣤⣤⣄⡀⠀
    """

    print(spidey)
    print(f"Server running at {url}")


# --- Lifecycle context (runs on startup/shutdown) ---
@asynccontextmanager
async def lifespan(app: FastAPI):
    Base.metadata.create_all(bind=engine)  # create tables on startup
    print_signature("http://localhost:8000")  # <-- your signature prints here
    yield


# --- FastAPI app instance ---
app = FastAPI(
    title="Finance Tracker API",
    version="0.1.0",
    lifespan=lifespan,
)


# --- CORS configuration ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://localhost:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# --- Routers registration ---
app.include_router(expense.router)

try:
    app.include_router(income.router)
except Exception:
    pass

app.include_router(tag.router)
app.include_router(balance_router.router)