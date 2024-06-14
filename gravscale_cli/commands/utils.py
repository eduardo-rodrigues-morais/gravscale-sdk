async def get_columns_size(headers: list[str], rows: list[tuple]) -> dict:
    dict_i = {}
    for item in rows:
        if len(item) > len(headers):
            raise ValueError("Headers and rows must be same size.")
        for i in range(len(item)):
            if i in dict_i.keys():
                dict_i[i].append(len(str(item[i])))
            else:
                dict_i[i] = []
                dict_i[i].append(len(str(item[i])))
    return dict_i


async def get_max_size_columns(headers: list[str], sizes: dict[int, int]):
    list_w = []
    for column, widths in sizes.items():
        max_value = (
            max(widths) if max(widths) > len(headers[column]) else len(headers[column])
        )
        list_w.append({column: max_value})
    return list_w
