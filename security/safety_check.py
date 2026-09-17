def is_safe(sql):
    sql = sql.strip().upper()

    return sql.startswith("SELECT")