from fastapi import APIRouter

router = APIRouter(prefix="/dishes", tags=["dishes"])


@router.get("/popular-cuisine")
async def get_popular_cuisine():
    pass
