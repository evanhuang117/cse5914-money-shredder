from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompatibilityProperty")


@attr.s(auto_attribs=True)
class CompatibilityProperty:
    """This container returns the product attribute name/value pairs that are compatible with the keyword. These attributes
    are submitted in the  <b>compatibility_filter</b> request field.

        Attributes:
            localized_name (Union[Unset, str]): The name of the product attribute that as been translated to the language of
                the site.
            name (Union[Unset, str]): The name of the product attribute, such as Make, Model, Year, etc.
            value (Union[Unset, str]): The value for the <b> name</b> attribute, such as BMW, R1200GS, 2011, etc.
    """

    localized_name: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localized_name = self.localized_name
        name = self.name
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localized_name is not UNSET:
            field_dict["localizedName"] = localized_name
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        localized_name = d.pop("localizedName", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        compatibility_property = cls(
            localized_name=localized_name,
            name=name,
            value=value,
        )

        compatibility_property.additional_properties = d
        return compatibility_property

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
