# coding: utf-8

"""
    Gravscale Public Restful API

    API pública da Gravscale oferece aos usuários a capacidade de se autenticar, visualizar e contratar produtos disponíveis, enviar dados de contratação, escolher formas de pagamento e gerenciar nossos produtos. Além disso, os usuários podem cadastrar chaves SSH e realizar o deploy de um sistema operacional de forma eficiente e segura. Esta API foi projetado para simplificar e agilizar o gerenciamento de recursos proporcionando que a a Gravscale forneça uma experiência integrada e intuitiva para os usuários.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from gravscale.models.validation_error_loc_inner import ValidationErrorLocInner
from typing import Optional, Set
from typing_extensions import Self

class ValidationError(BaseModel):
    """
    ValidationError
    """ # noqa: E501
    loc: List[ValidationErrorLocInner]
    msg: StrictStr
    type: StrictStr
    __properties: ClassVar[List[str]] = ["loc", "msg", "type"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ValidationError from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in loc (list)
        _items = []
        if self.loc:
            for _item in self.loc:
                if _item:
                    _items.append(_item.to_dict())
            _dict['loc'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ValidationError from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "loc": [ValidationErrorLocInner.from_dict(_item) for _item in obj["loc"]] if obj.get("loc") is not None else None,
            "msg": obj.get("msg"),
            "type": obj.get("type")
        })
        return _obj

