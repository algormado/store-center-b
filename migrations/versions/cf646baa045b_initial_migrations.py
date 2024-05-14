"""initial migrations

Revision ID: cf646baa045b
Revises: 
Create Date: 2024-05-14 09:38:50.194991

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cf646baa045b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage_slot',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size', sa.String(length=10), nullable=False),
    sa.Column('availability', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('_password_hash', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('storage_slot_id', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.Column('end_date', sa.Date(), nullable=False),
    sa.Column('is_picked_up', sa.Boolean(), nullable=True),
    sa.Column('is_delivered', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['storage_slot_id'], ['storage_slot.id'], name=op.f('fk_order_storage_slot_id_storage_slot')),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_order_user_id_user')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('delivery',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=False),
    sa.Column('delivery_date', sa.Date(), nullable=False),
    sa.Column('delivery_address', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], name=op.f('fk_delivery_order_id_order')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('delivery')
    op.drop_table('order')
    op.drop_table('user')
    op.drop_table('storage_slot')
    # ### end Alembic commands ###