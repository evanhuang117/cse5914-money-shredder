from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.common_descriptions import CommonDescriptions
from ..models.error import Error
from ..models.item import Item
from ..types import UNSET, Unset

T = TypeVar("T", bound="ItemGroup")


@attr.s(auto_attribs=True)
class ItemGroup:
    """The type that defines the fields for the item details.

    Attributes:
        common_descriptions (Union[Unset, List[CommonDescriptions]]): An array of containers for a description and the
            item IDs of all the items that have this exact description. Often the item variations within an item group all
            have the same description. Instead of repeating this description in the item details of each item, a description
            that is shared by at least one other item is returned in this container. If the description is unique, it is
            returned in the <b> items.description</b> field.
        items (Union[Unset, List[Item]]): An array of containers for all the item variation details, excluding the
            description.
        warnings (Union[Unset, List[Error]]): An array of warning messages. These types of errors do not prevent the
            method from executing but should be checked.
    """

    common_descriptions: Union[Unset, List[CommonDescriptions]] = UNSET
    items: Union[Unset, List[Item]] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        common_descriptions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.common_descriptions, Unset):
            common_descriptions = []
            for common_descriptions_item_data in self.common_descriptions:
                common_descriptions_item = common_descriptions_item_data.to_dict()

                common_descriptions.append(common_descriptions_item)

        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if common_descriptions is not UNSET:
            field_dict["commonDescriptions"] = common_descriptions
        if items is not UNSET:
            field_dict["items"] = items
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        common_descriptions = []
        _common_descriptions = d.pop("commonDescriptions", UNSET)
        for common_descriptions_item_data in _common_descriptions or []:
            common_descriptions_item = CommonDescriptions.from_dict(common_descriptions_item_data)

            common_descriptions.append(common_descriptions_item)

        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = Item.from_dict(items_item_data)

            items.append(items_item)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        item_group = cls(
            common_descriptions=common_descriptions,
            items=items,
            warnings=warnings,
        )

        item_group.additional_properties = d
        return item_group

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
