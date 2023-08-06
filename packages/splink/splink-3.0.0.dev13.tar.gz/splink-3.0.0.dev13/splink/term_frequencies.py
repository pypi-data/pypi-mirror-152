# For more information on where formulas came from, see
# https://github.com/moj-analytical-services/splink/pull/107

import logging

from .misc import escape_column
from .input_column import InputColumn

logger = logging.getLogger(__name__)


def colname_to_tf_tablename(colname):
    colname = colname.replace(" ", "_")
    return f"__splink__df_tf_{colname}"


def term_frequencies_for_single_column_sql(
    column_name, table_name="__splink__df_concat"
):

    # TODO: Not escaped so if col name has a space, will fail in Spark

    col = InputColumn(column_name, tf_adjustments=True)

    col_name = escape_column(column_name)

    sql = f"""
    select
    {col_name}, cast(count(*) as double) / (select
        count({col_name}) as total from {table_name}) as {col.tf_name(escape=False)}
    from {table_name}
    where {col_name} is not null
    group by {col_name}
    """

    return sql


def _join_tf_to_input_df(settings_obj):

    tf_cols = settings_obj._term_frequency_columns

    select_cols = []

    for col in tf_cols:
        tbl = colname_to_tf_tablename(col)
        tf_col = escape_column(f"tf_{col}")
        select_cols.append(f"{tbl}.{tf_col}")

    select_cols.insert(0, "__splink__df_concat.*")
    select_cols = ", ".join(select_cols)

    templ = "left join {tbl} on __splink__df_concat.{col} = {tbl}.{col}"

    left_joins = [
        templ.format(tbl=colname_to_tf_tablename(col), col=escape_column(col))
        for col in tf_cols
    ]
    left_joins = " ".join(left_joins)

    sql = f"""
    select {select_cols}
    from __splink__df_concat
    {left_joins}
    """

    return sql


def compute_all_term_frequencies_sqls(linker):

    settings_obj = linker._settings_obj
    tf_cols = settings_obj._term_frequency_columns

    if not tf_cols:
        return [
            {
                "sql": "select * from __splink__df_concat",
                "output_table_name": "__splink__df_concat_with_tf",
            }
        ]

    sqls = []
    for tf_col in tf_cols:
        tf_table_name = colname_to_tf_tablename(tf_col)

        if not linker._table_exists_in_database(tf_table_name):
            sql = term_frequencies_for_single_column_sql(tf_col)
            sql = {
                "sql": sql,
                "output_table_name": colname_to_tf_tablename(tf_col),
            }
            sqls.append(sql)

    sql = _join_tf_to_input_df(settings_obj)
    sql = {
        "sql": sql,
        "output_table_name": "__splink__df_concat_with_tf",
    }
    sqls.append(sql)

    return sqls
