"""create post table

Revision ID: 8759436b2099
Revises: 
Create Date: 2026-11-09 18:41:47.491720

"""
from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8759436b2099'
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table("posts"
                    ,sa.Column("id",sa.Integer(),nullable=False,primary_key=True)
                    ,sa.Column("title",sa.String(),nullable=False)
                    )
    


def downgrade() -> None:
    op.drop_table("posts")
