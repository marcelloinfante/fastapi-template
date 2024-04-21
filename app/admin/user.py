from sqladmin import ModelView

from app.models.user import User


class UserAdmin(ModelView, model=User):
    icon = "fa-solid fa-user"

    column_list = [
        User.id,
        User.email,
        User.is_admin,
        User.first_name,
        User.last_name,
    ]

    column_sortable_list = [
        User.id,
        User.email,
        User.is_admin,
        User.first_name,
        User.last_name,
    ]

    column_searchable_list = [
        User.id,
        User.email,
        User.is_admin,
        User.first_name,
        User.last_name,
    ]

    column_details_list = [
        User.id,
        User.email,
        User.is_admin,
        User.first_name,
        User.last_name,
    ]

    form_columns = [
        User.email,
        User.first_name,
        User.last_name,
        User.is_admin,
    ]

    column_formatters = {}

    column_formatters_detail = {}
