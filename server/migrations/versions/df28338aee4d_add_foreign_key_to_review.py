"""add foreign key to Review

Revision ID: df28338aee4d
Revises: 411fc90ef082
Create Date: 2024-10-05 09:57:20.511298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df28338aee4d'
down_revision = '411fc90ef082'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(batch_op.f('fk_reviews_employee_id_employees'), 'employees', ['employee_id'], ['id'])


def downgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_reviews_employee_id_employees'), type_='foreignkey')
        batch_op.drop_column('employee_id')
