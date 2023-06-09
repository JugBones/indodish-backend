"""empty message

Revision ID: df22ab21c25b
Revises: 8cd17e462d02
Create Date: 2023-05-21 21:21:15.825159

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df22ab21c25b'
down_revision = '8cd17e462d02'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('description', sa.TEXT(), nullable=True))
    op.add_column('restaurant', sa.Column('phone_number', sa.TEXT(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'phone_number')
    op.drop_column('restaurant', 'description')
    # ### end Alembic commands ###
