"""empty message

Revision ID: 3f27ebe3efbc
Revises: None
Create Date: 2014-07-30 14:08:01.250000

"""

# revision identifiers, used by Alembic.
revision = '3f27ebe3efbc'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('author_id', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'author_id')
    ### end Alembic commands ###
