from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Aspect")


@attr.s(auto_attribs=True)
class Aspect:
    """The type that defines the fields for the name/value pairs for the aspects of the product. For example: BRAND/Apple

    Attributes:
        localized_name (Union[Unset, str]): The text representing the name of the aspect for the name/value pair, such
            as Brand.
        localized_values (Union[Unset, List[str]]): The text representing the value of the aspect for the name/value
            pair, such as Apple.
    """

    localized_name: Union[Unset, str] = UNSET
    localized_values: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localized_name = self.localized_name
        localized_values: Union[Unset, List[str]] = UNSET
        if not isinstance(self.localized_values, Unset):
            localized_values = self.localized_values

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if localized_values is not UNSET:
            field_dict["localizedValues"] = localized_values

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        localized_name = d.pop("localizedName", UNSET)

        localized_values = cast(List[str], d.pop("localizedValues", UNSET))

        aspect = cls(
            localized_name=localized_name,
            localized_values=localized_values,
        )

        aspect.additional_properties = d
        return aspect

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
