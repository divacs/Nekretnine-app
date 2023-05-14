"""Migriranje baze 1

Revision ID: f7e15c0f7374
Revises: 
Create Date: 2023-05-14 19:17:09.350492

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7e15c0f7374'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nekretnina',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tipNekretnine', sa.String(length=100), nullable=False),
    sa.Column('tipPonude', sa.String(length=100), nullable=False),
    sa.Column('grad', sa.String(length=100), nullable=False),
    sa.Column('opstina', sa.String(length=100), nullable=False),
    sa.Column('kvadratura', sa.Double(), nullable=False),
    sa.Column('godinaIzgradnje', sa.Date(), nullable=False),
    sa.Column('povrsinaZemljista', sa.Double(), nullable=True),
    sa.Column('spratnost', sa.Integer(), nullable=False),
    sa.Column('uknjizenost', sa.String(length=20), nullable=False),
    sa.Column('tipGrejanja', sa.String(length=50), nullable=False),
    sa.Column('ukupanBrojSoba', sa.Float(), nullable=False),
    sa.Column('ukupnoKupatila', sa.Integer(), nullable=False),
    sa.Column('parking', sa.String(length=20), nullable=True),
    sa.Column('dodatneKarakteristike', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nekretnina')
    # ### end Alembic commands ###
