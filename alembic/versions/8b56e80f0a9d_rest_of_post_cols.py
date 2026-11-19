"""rest of post cols

Revision ID: 8b56e80f0a9d
Revises: 144f3d42f87a
Create Date: 2026-11-17 12:41:09.416650

"""
from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = '8b56e80f0a9d'
down_revision: Union[str, Sequence[str], None] = '144f3d42f87a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column("posts",sa.Column("published",sa.Boolean(),nullable=False,server_default="True"))
    op.add_column("posts",sa.Column("time",sa.TIMESTAMP(timezone=True),nullable=False,server_default=sa.text("now()")))


def downgrade() -> None:
    op.drop_column("posts","published")
    op.drop_column("posts","time")
    
