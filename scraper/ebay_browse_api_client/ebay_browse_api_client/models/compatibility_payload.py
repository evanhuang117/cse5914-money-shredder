from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.attribute_name_value import AttributeNameValue
from ..types import UNSET, Unset

T = TypeVar("T", bound="CompatibilityPayload")


@attr.s(auto_attribs=True)
class CompatibilityPayload:
    """An array of attribute name/value pairs used to define a specific product. For example: If you wanted to specify a
    specific car, one of the name/value pairs would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p>
    For a list of the attributes required for cars and trucks and motorcycles see <a href="/api-docs/buy/static/api-
    browse.html#Check">Check compatibility</a> in the Buy Integration Guide.</p>

        Attributes:
            compatibility_properties (Union[Unset, List[AttributeNameValue]]): An array of attribute name/value pairs used
                to define a specific product. For example: If you wanted to specify a specific car, one of the name/value pairs
                would be <br /><code>"name" : "Year", <br />"value" : "2019"</code>  <p> For a list of the attributes required
                for cars and trucks and motorcycles see <a href="/api-docs/buy/static/api-browse.html#Check">Check
                compatibility</a> in the Buy Integration Guide.</p>
    """

    compatibility_properties: Union[Unset, List[AttributeNameValue]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        compatibility_properties: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.compatibility_properties, Unset):
            compatibility_properties = []
            for compatibility_properties_item_data in self.compatibility_properties:
                compatibility_properties_item = compatibility_properties_item_data.to_dict()

                compatibility_properties.append(compatibility_properties_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if compatibility_properties is not UNSET:
            field_dict["compatibilityProperties"] = compatibility_properties

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        compatibility_properties = []
        _compatibility_properties = d.pop("compatibilityProperties", UNSET)
        for compatibility_properties_item_data in _compatibility_properties or []:
            compatibility_properties_item = AttributeNameValue.from_dict(compatibility_properties_item_data)

            compatibility_properties.append(compatibility_properties_item)

        compatibility_payload = cls(
            compatibility_properties=compatibility_properties,
        )

        compatibility_payload.additional_properties = d
        return compatibility_payload

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
