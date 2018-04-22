"""empty message

Revision ID: c068d03fe8b8
Revises: eca3d3c8561c
Create Date: 2018-04-21 23:09:27.557056

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'c068d03fe8b8'
down_revision = 'eca3d3c8561c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('students', sa.Column('student_id', sa.Integer(), nullable=False))
    op.drop_column('students', 'id')
    op.add_column('tutors', sa.Column('tutor_id', sa.Integer(), nullable=False))
    op.drop_column('tutors', 'id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tutors', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('tutors', 'tutor_id')
    op.add_column('students', sa.Column('id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_column('students', 'student_id')
    # ### end Alembic commands ###
