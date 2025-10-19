"""
Tag routes

Responsibilities:
- Manages CRUD operations for tag entities
- Prevents duplicate tag creation (unique constraint)
- Returns all tags or handles deletion by ID

Example:
    POST /tags
    {
        "name": "Food"
    }
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app import models, schemas


# Router configuration
router = APIRouter(prefix="/tags", tags=["Tags"])


@router.post("/", response_model=schemas.tag.TagOut)
def create_tag(data: schemas.tag.TagCreate, db: Session = Depends(get_db)):
    """
    Creates a new tag if it doesn't already exist.

    Raises:
        HTTPException: If a tag with the same name already exists.
    """
    existing = db.query(models.tag.Tag).filter(models.tag.Tag.name == data.name).first()
    if existing:
        raise HTTPException(status_code=400, detail="Tag already exists")

    tag = models.tag.Tag(name=data.name)
    db.add(tag)
    db.commit()
    db.refresh(tag)
    return tag


@router.get("/", response_model=list[schemas.tag.TagOut])
def list_tags(db: Session = Depends(get_db)):
    """
    Returns all registered tags.
    """
    return db.query(models.tag.Tag).all()


@router.delete("/{tag_id}")
def delete_tag(tag_id: int, db: Session = Depends(get_db)):
    """
    Deletes a tag by ID.

    Raises:
        HTTPException: If the tag does not exist.
    """
    tag = db.query(models.tag.Tag).get(tag_id)
    if not tag:
        raise HTTPException(status_code=404, detail="Tag not found")

    db.delete(tag)
    db.commit()
    return {"message": "Tag deleted successfully"}