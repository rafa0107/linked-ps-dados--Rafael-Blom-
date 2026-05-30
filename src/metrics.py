def receita_bruta(df):
    return df["total_value"].sum()

def receita_bruta(df):
    return df["total_value"].sum()

def ticket_medio(df):
    return (
        df["total_value"].sum()
        /
        df["order_id"].nunique()
    )

