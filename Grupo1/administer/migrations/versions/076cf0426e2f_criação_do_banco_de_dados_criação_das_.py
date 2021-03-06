"""Criação do banco de dados, criação das tabelas

Revision ID: 076cf0426e2f
Revises: 
Create Date: 2019-07-06 14:54:28.944143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '076cf0426e2f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administradores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('data_nasc', sa.DateTime(), nullable=False),
    sa.Column('hhash', sa.String(), nullable=True),
    sa.Column('urole', sa.String(length=80), nullable=True),
    sa.Column('avatar', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('funcionarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=120), nullable=False),
    sa.Column('idade', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('setor', sa.String(length=120), nullable=False),
    sa.Column('admin_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['administradores.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionarios')
    op.drop_table('administradores')
    # ### end Alembic commands ###
