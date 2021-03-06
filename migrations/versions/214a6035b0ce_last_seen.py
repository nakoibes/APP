"""last_seen

Revision ID: 214a6035b0ce
Revises: 6a4616f6f607
Create Date: 2021-07-11 12:24:55.985361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '214a6035b0ce'
down_revision = '6a4616f6f607'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
