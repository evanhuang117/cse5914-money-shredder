from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="TypedNameValue")


@attr.s(auto_attribs=True)
class TypedNameValue:
    """The type that defines the fields for the name/value pairs for item aspects.

    Attributes:
        name (Union[Unset, str]): The text representing the name of the aspect for the name/value pair, such as Color.
        type (Union[Unset, str]): This indicates if the value being returned is a string or an array of values.
            <br><br><b> Valid Values: </b> <ul><li><b> STRING</b> - Indicates the value returned is a string.</li>  <li><b>
            STRING_ARRAY</b> - Indicates the value returned is an array of strings.</li></ul>  Code so that your app
            gracefully handles any future changes to this list. For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:ValueTypeEnum'>eBay API documentation</a>
        value (Union[Unset, str]): The value of the aspect for the name/value pair, such as Red.
    """

    name: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        type = self.type
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        type = d.pop("type", UNSET)

        value = d.pop("value", UNSET)

        typed_name_value = cls(
            name=name,
            type=type,
            value=value,
        )

        typed_name_value.additional_properties = d
        return typed_name_value

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
