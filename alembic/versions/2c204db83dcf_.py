"""empty message

Revision ID: 2c204db83dcf
Revises: b96b61e31844
Create Date: 2023-05-29 06:48:36.878076

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2c204db83dcf'
down_revision = 'b96b61e31844'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('image',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('url', sa.TEXT(), nullable=False),
    sa.Column('alt', sa.TEXT(), nullable=False),
    sa.Column('width', sa.INTEGER(), nullable=False),
    sa.Column('height', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dish',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('name', sa.TEXT(), nullable=False),
    sa.Column('description', sa.TEXT(), nullable=True),
    sa.Column('restaurant_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('category', postgresql.ENUM('snack', 'appetizer', 'main_course', 'dessert', 'beverage', name='dish_category'), nullable=True),
    sa.Column('price', postgresql.MONEY(), nullable=False),
    sa.Column('rating_sum', sa.INTEGER(), nullable=False),
    sa.Column('number_of_voters', sa.INTEGER(), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('restaurant_image',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('restaurant_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('image_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.ForeignKeyConstraint(['restaurant_id'], ['restaurant.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('dish_image',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('dish_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('image_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['image_id'], ['image.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cart',
    sa.Column('id', postgresql.UUID(as_uuid=True), server_default=sa.text('uuid_generate_v4()'), nullable=False),
    sa.Column('quantity', sa.INTEGER(), nullable=False),
    sa.Column('dish_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('user_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('refresh_token_id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['dish_id'], ['dish.id'], ),
    sa.ForeignKeyConstraint(['refresh_token_id'], ['refresh_token.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_constraint('restaurant_user_id_key', 'restaurant', type_='unique')
    op.drop_constraint('restaurant_user_id_fkey', 'restaurant', type_='foreignkey')
    op.drop_column('restaurant', 'user_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('restaurant', sa.Column('user_id', postgresql.UUID(), autoincrement=False, nullable=False))
    op.create_foreign_key('restaurant_user_id_fkey', 'restaurant', 'user', ['user_id'], ['id'], ondelete='CASCADE')
    op.create_unique_constraint('restaurant_user_id_key', 'restaurant', ['user_id'])
    op.drop_table('cart')
    op.drop_table('dish_image')
    op.drop_table('restaurant_image')
    op.drop_table('dish')
    op.drop_table('image')
    # ### end Alembic commands ###
