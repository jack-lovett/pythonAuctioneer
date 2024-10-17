"""Initial migration

Revision ID: ceb3fa115dad
Revises: 
Create Date: 2024-10-17 22:42:19.971506

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ceb3fa115dad'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auctions',
    sa.Column('auction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('auction_description', sa.Text(), nullable=True),
    sa.Column('auction_open_time', sa.DateTime(), nullable=False),
    sa.Column('auction_close_time', sa.DateTime(), nullable=False),
    sa.Column('auction_status', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('auction_id')
    )
    op.create_table('card_conditions',
    sa.Column('condition_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('condition_name', sa.String(), nullable=False),
    sa.Column('condition_discount_percentage', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('condition_id'),
    sa.UniqueConstraint('condition_name')
    )
    op.create_table('card_finishes',
    sa.Column('finish_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('finish_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('finish_id'),
    sa.UniqueConstraint('finish_name')
    )
    op.create_table('customers',
    sa.Column('customer_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_firstname', sa.String(), nullable=False),
    sa.Column('customer_lastname', sa.String(), nullable=False),
    sa.Column('customer_address', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('customer_id')
    )
    op.create_table('shipping_methods',
    sa.Column('shipping_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('shipping_type', sa.String(), nullable=False),
    sa.Column('shipping_cost', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('shipping_id')
    )
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_table('orders',
    sa.Column('order_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('order_customer_id', sa.Integer(), nullable=False),
    sa.Column('order_shipping_id', sa.Integer(), nullable=True),
    sa.Column('order_tracking_reference', sa.String(), nullable=True),
    sa.Column('order_status', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['order_customer_id'], ['customers.customer_id'], ),
    sa.ForeignKeyConstraint(['order_shipping_id'], ['shipping_methods.shipping_id'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    op.create_table('cards',
    sa.Column('card_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('card_scryfall_id', sa.String(), nullable=False),
    sa.Column('card_name', sa.String(), nullable=False),
    sa.Column('card_initial_price', sa.Float(), nullable=True),
    sa.Column('card_purchase_price', sa.Float(), nullable=True),
    sa.Column('card_lot_number', sa.Integer(), nullable=True),
    sa.Column('card_caption', sa.String(), nullable=True),
    sa.Column('card_finish_id', sa.Integer(), nullable=True),
    sa.Column('card_condition_id', sa.Integer(), nullable=True),
    sa.Column('card_auction_id', sa.Integer(), nullable=True),
    sa.Column('card_order_id', sa.Integer(), nullable=True),
    sa.Column('card_times_on_auction', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['card_auction_id'], ['auctions.auction_id'], ),
    sa.ForeignKeyConstraint(['card_condition_id'], ['card_conditions.condition_id'], ),
    sa.ForeignKeyConstraint(['card_finish_id'], ['card_finishes.finish_id'], ),
    sa.ForeignKeyConstraint(['card_order_id'], ['orders.order_id'], ),
    sa.PrimaryKeyConstraint('card_id')
    )
    op.create_table('invoices',
    sa.Column('invoice_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('invoice_date_issued', sa.DateTime(), nullable=True),
    sa.Column('invoice_paid_status', sa.String(), nullable=True),
    sa.Column('invoice_order_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['invoice_order_id'], ['orders.order_id'], ),
    sa.PrimaryKeyConstraint('invoice_id')
    )
    op.create_table('bank_transactions',
    sa.Column('transaction_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('transaction_reference', sa.String(), nullable=False),
    sa.Column('transaction_date', sa.DateTime(), nullable=False),
    sa.Column('transaction_amount', sa.Float(), nullable=False),
    sa.Column('transaction_invoice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transaction_invoice_id'], ['invoices.invoice_id'], ),
    sa.PrimaryKeyConstraint('transaction_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('bank_transactions')
    op.drop_table('invoices')
    op.drop_table('cards')
    op.drop_table('orders')
    op.drop_table('users')
    op.drop_table('shipping_methods')
    op.drop_table('customers')
    op.drop_table('card_finishes')
    op.drop_table('card_conditions')
    op.drop_table('auctions')
    # ### end Alembic commands ###
