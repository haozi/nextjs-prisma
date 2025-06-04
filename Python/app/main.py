# import pdb; pdb.set_trace()

import os

from app.api.hello import router as hello_router
from app.api.items import router as items_router
from fastapi import FastAPI

# from app.api.fastapi_users import auth_router, users_router

disable_docs = os.getenv("DISABLE_DOCS", "false").lower() == "true"
app = FastAPI(
    docs_url=None if disable_docs else "/api/docs",
    openapi_url=None if disable_docs else "/api/docs/openapi.json",
)

# app.include_router(auth_router, prefix="/api/auth/jwt", tags=["auth"])
# app.include_router(users_router, prefix="/api/users", tags=["users"])
app.include_router(hello_router)
app.include_router(items_router)
