from pydantic import BaseModel, Field
from typing import Optional, List

class Movie(BaseModel):
    id: Optional[int]
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
     "json_schema_extra": {
            "examples": [
                {
                    "id": 1,
                    "title": "My Movie",
                    "overview": "This movies is about...",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Horror"
                }
            ]
        }
    }
