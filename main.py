from database.schema import create_all_tables

from ui.login_page import open_login_page


# CREATE ALL DATABASE TABLES
create_all_tables()

print("Database Ready")


# START APPLICATION
open_login_page()