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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from gravscale.models.app_modules_network_schema_vpc_schema import (
    AppModulesNetworkSchemaVpcSchema,
)
from gravscale.models.ip_schema import IpSchema
from typing import Optional, Set
from typing_extensions import Self


class PublicIpSchema(BaseModel):
    """
    PublicIpSchema
    """  # noqa: E501

    address: StrictStr
    vpc: AppModulesNetworkSchemaVpcSchema
    public_ip: List[IpSchema] = Field(alias="publicIp")
    __properties: ClassVar[List[str]] = ["address", "vpc", "publicIp"]

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
        """Create an instance of PublicIpSchema from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of vpc
        if self.vpc:
            _dict["vpc"] = self.vpc.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in public_ip (list)
        _items = []
        if self.public_ip:
            for _item in self.public_ip:
                if _item:
                    _items.append(_item.to_dict())
            _dict["publicIp"] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PublicIpSchema from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate(
            {
                "address": obj.get("address"),
                "vpc": AppModulesNetworkSchemaVpcSchema.from_dict(obj["vpc"])
                if obj.get("vpc") is not None
                else None,
                "publicIp": [IpSchema.from_dict(_item) for _item in obj["publicIp"]]
                if obj.get("publicIp") is not None
                else None,
            }
        )
        return _obj
