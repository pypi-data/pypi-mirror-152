from typing import Optional

from fastapi import Cookie, Depends

from fief.crypto.token import get_token_hash
from fief.dependencies.workspace_managers import get_session_token_manager
from fief.managers import SessionTokenManager
from fief.models import SessionToken
from fief.settings import settings


async def get_session_token(
    token: Optional[str] = Cookie(None, alias=settings.session_cookie_name),
    manager: SessionTokenManager = Depends(get_session_token_manager),
) -> Optional[SessionToken]:
    if token is not None:
        token_hash = get_token_hash(token)
        return await manager.get_by_token(token_hash)
    return None
