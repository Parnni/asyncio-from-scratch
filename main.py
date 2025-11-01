"""Tricks
When creating APIs
        - Static APIs should be written first
        - Dynamic APIs should be written after static APIs
        - APIs should be ordered in increasing length of API path
        Example:
                - /blogs
                - /blogs/{pk}
                - /blogs/{pk}/comments
                - /blogs/{pk}/comments/likes
"""

from typing import Any, Optional

from fastapi import FastAPI, HTTPException

app = FastAPI()


# Static end points.
@app.get('/')
def index() -> dict[str, dict[str, str]]:
    """Home page."""
    return {
        'data': {
            'name': 'Param',
        }
    }


# ------------------- Blog end points -------------------
# Static end points.
@app.get('/blogs')
def get_blogs(
    limit: Optional[int] = 10, published: Optional[bool] = True
) -> dict[str, str]:
    """Gets all blogs."""
    if published:
        return {'data': f'Displaying only published blogs with limit: {limit}'}
    return {'data': f'Displaying only unpublished blogs with limit: {limit}'}


@app.get('/blogs/unpublished')
def get_unpublished_blogs() -> dict[str, str]:
    """Gets unpublished blogs."""
    return {
        'data': 'unpublished blogs',
    }


# Dynamic end points.
@app.get('/blogs/{pk}')
def get_blog(pk: int) -> dict[str, int]:
    """Gets blog for the id."""
    return {
        'data': pk,
    }


@app.get('/blogs/{pk}/comments')
def get_blog_comments(pk: int) -> dict[str, list[int]]:
    """Gets comments for the blog."""
    return {
        'data': [1, 2, 3],
    }


BANDS = [
    {
        "id": 1,
        "name": "Param",
    },
    {
        "id": 2,
        "name": "Dharam",
    },
]


@app.get('/bands')
async def get_bands() -> list[dict[str, Any]]:
    """Gets bands."""
    return BANDS


@app.get('/bands/{band_id}')
async def get_band(band_id: int) -> dict[str, Any]:
    """Gets a band."""
    band = list(filter(lambda band: band['id'] == band_id, BANDS))
    if not band:
        raise HTTPException(
            status_code=404, detail=f'Band with ID: {band_id} not found.'
        )
    return band[0]
