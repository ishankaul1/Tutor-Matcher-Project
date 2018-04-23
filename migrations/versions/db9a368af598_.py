"""empty message

Revision ID: db9a368af598
Revises: 0fe3c05d1111
Create Date: 2018-04-22 22:30:36.098328

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'db9a368af598'
down_revision = '0fe3c05d1111'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('username', sa.String(length=60), nullable=True),
    sa.Column('first_name', sa.String(length=60), nullable=True),
    sa.Column('last_name', sa.String(length=60), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('role', sa.String(length=128), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_Users_email'), 'Users', ['email'], unique=True)
    op.create_index(op.f('ix_Users_first_name'), 'Users', ['first_name'], unique=False)
    op.create_index(op.f('ix_Users_last_name'), 'Users', ['last_name'], unique=False)
    op.create_index(op.f('ix_Users_username'), 'Users', ['username'], unique=True)
    op.drop_table('students')
    op.drop_table('tutors')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tutors',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.create_table('students',
    sa.Column('id', mysql.INTEGER(display_width=11), nullable=False),
    sa.Column('email', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('username', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('first_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('last_name', mysql.VARCHAR(length=60), nullable=True),
    sa.Column('password_hash', mysql.VARCHAR(length=128), nullable=True),
    sa.Column('is_admin', mysql.TINYINT(display_width=1), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_default_charset=u'latin1',
    mysql_engine=u'InnoDB'
    )
    op.drop_index(op.f('ix_Users_username'), table_name='Users')
    op.drop_index(op.f('ix_Users_last_name'), table_name='Users')
    op.drop_index(op.f('ix_Users_first_name'), table_name='Users')
    op.drop_index(op.f('ix_Users_email'), table_name='Users')
    op.drop_table('Users')
    # ### end Alembic commands ###