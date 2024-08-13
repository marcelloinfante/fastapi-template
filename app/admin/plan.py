from sqladmin import ModelView

from app.models.plan import Plan


class PlanAdmin(ModelView, model=Plan):
    icon = "fa-solid fa-money-bill"

    column_list = [
        Plan.id,
        Plan.type,
        Plan.created_at,
        Plan.updated_at,
    ]

    column_sortable_list = [
        Plan.id,
        Plan.type,
        Plan.created_at,
        Plan.updated_at,
    ]

    column_searchable_list = [
        Plan.id,
        Plan.type,
        Plan.created_at,
        Plan.updated_at,
    ]

    form_columns = [Plan.user, Plan.type]

    column_formatters = {
        Plan.user: lambda m, a: m.user.email if m.user else None,
    }

    column_formatters_detail = {
        Plan.user: lambda m, a: m.user.email if m.user else None,
    }
