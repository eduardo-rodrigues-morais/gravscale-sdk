import json
from abc import ABCMeta, abstractmethod
from time import sleep
from typing import List, Callable, Any, Tuple

import click
from tqdm import tqdm

import gravscale
from .exceptions import ReadInputValueException, PrintableTableException
from .utils import get_columns_size, get_max_size_columns


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
        try:
            size_items = await get_columns_size(headers, rows)
            column_widths = await get_max_size_columns(headers, size_items)
            return column_widths
        except Exception as exc:
            raise PrintableTableException(exc)

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
        formatted_json = json.dumps(data, indent=2)
        click.echo(formatted_json)


class AbstractPrintableTask(metaclass=ABCMeta):
    @classmethod
    async def _echo_task_info(cls, task):
        click.echo(f"Status: {task.status}") if task.status else None
        click.echo(f"Result: {str(task.result)}") if task.result else None


class AbstractReadInputValue(metaclass=ABCMeta):
    @classmethod
    async def _read_prompt_input(
        cls,
        text: str,
        variable,
        validators: List[Tuple[Callable[[Any], bool], str]] = None,
        **kwargs,
    ):
        error = None
        try:
            value = click.prompt(text, **kwargs) if not variable else variable
            if validators:
                for validator, msg_error in validators:
                    error = msg_error
                    validator(value)
            return value
        except ValueError as exc:
            error = error if error else exc.args[0]
            click.echo(error)
            return await cls._read_prompt_input(
                text, None, validators=validators, **kwargs
            )
        except click.exceptions.Abort:
            raise ReadInputValueException("Input aborted")


class AbstractTask(metaclass=ABCMeta):
    @classmethod
    async def await_task_complete(
        cls,
        api_client: gravscale.ApiClient,
        client_id: int,
        task: gravscale.TaskSchema,
    ):
        updated_task = None
        task_id = task.id
        task_status = task.status
        percentage_complete = task.percentage_complete
        taskman_api = gravscale.TaskManagerApi(api_client)
        if task_status not in ["completed", "failed"]:
            with tqdm(total=100) as pbar:
                while percentage_complete < 100:
                    updated_task = taskman_api.get_task(task_id, client_id)
                    if percentage_complete != updated_task.percentage_complete:
                        percentage_complete = updated_task.percentage_complete
                        pbar.update(percentage_complete)
                    sleep(1)
        task = updated_task if updated_task else task
        return task
