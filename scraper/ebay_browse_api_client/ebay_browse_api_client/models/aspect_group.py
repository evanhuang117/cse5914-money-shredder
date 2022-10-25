from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aspect import Aspect
from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectGroup")


@attr.s(auto_attribs=True)
class AspectGroup:
    """
    Attributes:
        aspects (Union[Unset, List[Aspect]]): An array of the name/value pairs for the aspects of the product. For
            example: BRAND/Apple
        localized_group_name (Union[Unset, str]): The name of a group of aspects. <br /><br />In the following example,
            <b> Product Identifiers</b> and <b> Process</b> are product aspect group names. Under the group name are the
            product aspect name/value pairs. <p><b> Product Identifiers</b> <br />&nbsp;&nbsp;&nbsp;Brand/Apple <br
            />&nbsp;&nbsp;&nbsp;Product Family/iMac</p> <p><b> Processor</b><br />&nbsp;&nbsp;&nbsp;Processor Type/Intel <br
            />&nbsp;&nbsp;&nbsp;Processor Speed/3.10</p>
    """

    aspects: Union[Unset, List[Aspect]] = UNSET
    localized_group_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aspects: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aspects, Unset):
            aspects = []
            for aspects_item_data in self.aspects:
                aspects_item = aspects_item_data.to_dict()

                aspects.append(aspects_item)

        localized_group_name = self.localized_group_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspects is not UNSET:
            field_dict["aspects"] = aspects
        if localized_group_name is not UNSET:
            field_dict["localizedGroupName"] = localized_group_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aspects = []
        _aspects = d.pop("aspects", UNSET)
        for aspects_item_data in _aspects or []:
            aspects_item = Aspect.from_dict(aspects_item_data)

            aspects.append(aspects_item)

        localized_group_name = d.pop("localizedGroupName", UNSET)

        aspect_group = cls(
            aspects=aspects,
            localized_group_name=localized_group_name,
        )

        aspect_group.additional_properties = d
        return aspect_group

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
