"""add content column to posts table

Revision ID: ccfb6b4f7011
Revises: f521f3bfe027
Create Date: 2024-02-12 12:12:53.956652

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ccfb6b4f7011'
down_revision: Union[str, None] = 'f521f3bfe027'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
