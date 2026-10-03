from fastapi import Depends, Header, HTTPException

VALID_ROLES = ["consumer", "business", "authority", "admin"]


# TEMPORARY: header se user padhta hai. Supabase aane par sirf ye file badlegi.
def get_current_user(
    x_mock_user: str | None = Header(default=None),
    x_mock_role: str | None = Header(default=None),
):
    if not x_mock_user or not x_mock_role:
        raise HTTPException(
            status_code=401,
            detail="Unauthorized: x-mock-user and x-mock-role headers required",
        )
    if x_mock_role not in VALID_ROLES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid role. Use one of: {', '.join(VALID_ROLES)}",
        )
    return {"id": x_mock_user, "role": x_mock_role}


def require_role(*roles: str):
    def checker(user: dict = Depends(get_current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Forbidden: insufficient role")
        return user

    return checker