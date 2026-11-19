"""add user table

Revision ID: c28cda4b2d1c
Revises: 7a5e1f28d1f9
Create Date: 2026-11-16 16:57:54.842810

"""
from collections.abc import Sequence
from typing import Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'c28cda4b2d1c'
down_revision: Union[str, Sequence[str], None] = '7a5e1f28d1f9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("users",
                    sa.Column("id",sa.Integer(),nullable=False,primary_key=True),
                    sa.Column("email",sa.String(),nullable=False,unique=True),
                    sa.Column("password",sa.String(),nullable=False),
                    sa.Column("time",sa.TIMESTAMP(timezone=True),server_default=sa.text('now()'), nullable=False)
                    )


def downgrade() -> None:
    op.drop_table("users")
