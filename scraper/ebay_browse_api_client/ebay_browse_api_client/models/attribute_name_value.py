from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AttributeNameValue")


@attr.s(auto_attribs=True)
class AttributeNameValue:
    """The type the defines attribute name/value pair fields that specify a product. The type of data depends on the
    context. For example, if you were using this to specify a specific vehicle, the attribute names would be Make,
    Model, Year, etc.

        Attributes:
            name (Union[Unset, str]): The name of the product attribute, such as Make, Model, Year, etc.
            value (Union[Unset, str]): The value for the <b> name</b> attribute, such as BMW, R1200GS, 2011, etc.
    """

    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        attribute_name_value = cls(
            name=name,
            value=value,
        )

        attribute_name_value.additional_properties = d
        return attribute_name_value

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
