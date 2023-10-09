from fastapi import BackgroundTasks, FastAPI, Request
from handlers.tg import telegram_handler

app = FastAPI()


@app.post("/tg_webhook")
async def send_notification(request: Request, background_tasks: BackgroundTasks):
    print("received telegram webhook...")

    incoming_data = await request.json()
    background_tasks.add_task(telegram_handler, event=incoming_data)

    return


@app.get("/")
async def root():
    return
