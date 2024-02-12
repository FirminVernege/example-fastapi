"""create post table again

Revision ID: f521f3bfe027
Revises: cd0afb138cd2
Create Date: 2024-02-12 10:54:57.443401

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f521f3bfe027'
down_revision: Union[str, None] = 'cd0afb138cd2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table('posts')
    pass
