"""empty message

Revision ID: 27cefdbfe3e1
Revises: 
Create Date: 2023-01-24 06:38:43.615605

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '27cefdbfe3e1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admins',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('username', sa.String(length=25), nullable=True),
    sa.Column('password', sa.String(length=300), nullable=True),
    sa.Column('access', sa.String(length=50), nullable=True),
    sa.Column('active', sa.String(length=1), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('contents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=500), nullable=True),
    sa.Column('types', sa.String(length=500), nullable=True),
    sa.Column('content', sa.String(length=300), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contents')
    op.drop_table('admins')
    # ### end Alembic commands ###
