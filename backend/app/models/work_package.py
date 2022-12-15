# -*- coding: utf-8 -*-
from datetime import datetime
from typing import Optional
from uuid import UUID, uuid4

import sqlalchemy as sa
import sqlalchemy.dialects.postgresql as pg
from pydantic import BaseModel
from sqlmodel import Field, SQLModel


class WorkPackage(SQLModel, table=True):
    __tablename__ = "work_package"

    id: Optional[UUID] = Field(
        sa_column=sa.Column(
            pg.UUID(as_uuid=True), primary_key=True, default=uuid4, server_default=sa.text("gen_random_uuid()")
        ),
    )
    created_date: Optional[datetime] = Field(
        sa_column=sa.Column(sa.DateTime(), nullable=False, server_default=sa.func.current_timestamp()),
    )
    expiry_date: Optional[datetime] = Field(sa_column=sa.Column(sa.DateTime(), nullable=True))
    person_id: UUID = Field(nullable=False, foreign_key="person.id", index=True)
    payload_type: str = Field(nullable=False, max_length=200)
    payload: BaseModel = Field(sa_column=sa.Column(pg.JSONB, nullable=False))
    api_client_id: UUID = Field(nullable=False, foreign_key="api_client.id")
