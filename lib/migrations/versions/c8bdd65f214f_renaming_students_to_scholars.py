"""Renaming students to scholars

Revision ID: c8bdd65f214f
Revises: 791279dd0760
Create Date: 2024-01-04 10:49:35.024045

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8bdd65f214f'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.rename_table('students', 'scholars')


def downgrade() -> None:
     op.rename_table('scholars', 'students')
