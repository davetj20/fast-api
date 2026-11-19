"""add foreign key

Revision ID: 144f3d42f87a
Revises: c28cda4b2d1c
Create Date: 2026-11-17 11:34:16.089314

"""
from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '144f3d42f87a'
down_revision: str | Sequence[str] | None = 'c28cda4b2d1c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("user_id",sa.Integer(),nullable=False))
    op.create_foreign_key("posts_users_fk",
                          source_table="posts",
                          referent_table="users",
                          local_cols=["user_id"],
                          remote_cols=["id"],
                          ondelete="CASCADE")


def downgrade() -> None:
    op.drop_constraint("post_users_fk",table_name="posts")
    op.drop_column("posts","user_id")

