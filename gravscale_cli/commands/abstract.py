import json
from abc import ABCMeta, abstractmethod
from typing import List, Callable, Any, Tuple

import click
from click import ParamType


class AbstractPrintableTable(metaclass=ABCMeta):
    @property
    @abstractmethod
    def _table_headers(self) -> List[str]:
        pass

    @abstractmethod
    def _gen_table_rows(self, data: List[dict]) -> List[tuple]:
        pass

    @classmethod
    async def _calculate_columns_width(cls, headers: List[str], rows: List[tuple]):
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

        column_widths = []
        for column, widths in dict_i.items():
            max_value = (
                max(widths)
                if max(widths) > len(headers[column])
                else len(headers[column])
            )
            column_widths.append({column: max_value})

        return column_widths

    @classmethod
    async def _generate_line(cls, *args):
        header = "|"
        for i in range(len(args)):
            header += " {:^{}} |".format(*args[i])
        return header

    @classmethod
    async def _echo_table(cls, width: List[dict], headers: [str], data: [tuple]):
        header = await cls._generate_line(
            *[(headers[i], width[i][i]) for i in range(len(headers))]
        )

        click.echo("-" * len(header))
        click.echo(header)
        click.echo("-" * len(header))
        for item in data:
            line = await cls._generate_line(
                *[(item[i], width[i][i]) for i in range(len(item))]
            )
            click.echo(line)
        click.echo("-" * len(header))


class AbstractPrintableJSON(metaclass=ABCMeta):
    @classmethod
    async def _echo_json(cls, data: dict):
        formatted_json = json.dumps(data, indent=3)
        click.echo(formatted_json)


class AbstractReadInputValue(metaclass=ABCMeta):
    @classmethod
    async def _read_prompt_input(
        cls,
        text: str,
        variable,
        type: ParamType,
        validators: List[Tuple[Callable[[Any], bool], str]] = None,
    ):
        value = click.prompt(text, type=type) if not variable else variable

        if validators:
            error = None
            try:
                for validator, msg_error in validators:
                    error = msg_error
                    validator(value)

            except ValueError as exc:
                error = error if error else exc.args[0]
                click.echo(error)
                return await cls._read_prompt_input(text, None, type, validators)

        return value
