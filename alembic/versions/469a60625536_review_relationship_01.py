"""Review Relationship -01

Revision ID: 469a60625536
Revises: dbea8c426d2c
Create Date: 2023-12-24 00:42:03.126330

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '469a60625536'
down_revision: Union[str, None] = 'dbea8c426d2c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('review', sa.Column('pokemon_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'review', 'pokemon', ['pokemon_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'review', type_='foreignkey')
    op.drop_column('review', 'pokemon_id')
    # ### end Alembic commands ###
