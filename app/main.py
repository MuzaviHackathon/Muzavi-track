
from fastapi import FastAPI, HTTPException
import requests

from app.track_recommendation import recommend_for_user
JAVA_BASE_URL: str = "http://localhost:8080"

app = FastAPI(title="Course Track Recommender")


@app.get("/users/{user_id}/recommendation")
def get_recommendation(user_id: int):
    """
    Java(또는 프론트엔드)가 호출하는 메인 엔드포인트
    """
    try:
        result = recommend_for_user(user_id)
        return result
    except requests.HTTPError as err:      # Java 호출 실패
        raise HTTPException(status_code=502, detail=str(err))
    except Exception as err:               # 예기치 못한 내부 오류
        raise HTTPException(status_code=500, detail=str(err))
