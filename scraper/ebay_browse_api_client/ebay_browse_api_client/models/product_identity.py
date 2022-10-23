from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ProductIdentity")


@attr.s(auto_attribs=True)
class ProductIdentity:
    """The type that defines the fields for the product identifier type/value pairs of product associated with an item.

    Attributes:
        identifier_type (Union[Unset, str]): The type of product identifier, such as UPC and EAN.
        identifier_value (Union[Unset, str]): The product identifier value.
    """

    identifier_type: Union[Unset, str] = UNSET
    identifier_value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        identifier_type = self.identifier_type
        identifier_value = self.identifier_value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if identifier_type is not UNSET:
            field_dict["identifierType"] = identifier_type
        if identifier_value is not UNSET:
            field_dict["identifierValue"] = identifier_value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        identifier_type = d.pop("identifierType", UNSET)

        identifier_value = d.pop("identifierValue", UNSET)

        product_identity = cls(
            identifier_type=identifier_type,
            identifier_value=identifier_value,
        )

        product_identity.additional_properties = d
        return product_identity

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
