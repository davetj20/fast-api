"""add new col content

Revision ID: 7a5e1f28d1f9
Revises: 8759436b2099
Create Date: 2026-11-09 19:59:12.379689

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '7a5e1f28d1f9'
down_revision: str | Sequence[str] | None = '8759436b2099'
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("content",sa.String(),nullable=False))


def downgrade() -> None:
    op.drop_column("posts","content")    

