"""Insert data into products table

Revision ID: da558edc19c3
Revises: d0e2fc7f9ee9
Create Date: 2026-05-29 13:57:49.993346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da558edc19c3'
down_revision = 'd0e2fc7f9ee9'
branch_labels = None
depends_on = None


def upgrade():
    op.execute("INSERT INTO categories (name) VALUES ('Books')")
    op.execute("INSERT INTO categories (name) VALUES ('Clothing')")

    op.execute("""
        INSERT INTO products (name, price, category_id, active)
        SELECT 'Novel', 25.50, id, 1
        FROM categories
        WHERE name = 'Books'
    """)

    op.execute("""
        INSERT INTO products (name, price, category_id, active)
        SELECT 'T-Shirt', 19.99, id, 1
        FROM categories
        WHERE name = 'Clothing'
    """)

    op.execute("""
        INSERT INTO products (name, price, category_id, active)
        SELECT 'Smartphone LG', 800.00, id, 1
        FROM categories
        WHERE name = 'Laptops'
    """)


def downgrade():
    op.execute("""
        DELETE FROM products
        WHERE name IN ('Novel', 'T-Shirt', 'Smartphone LG')
    """)

    op.execute("""
        DELETE FROM categories
        WHERE name IN ('Books', 'Clothing')
    """)