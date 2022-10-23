from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.core_item import CoreItem
from ..models.error import Error
from ..types import UNSET, Unset

T = TypeVar("T", bound="Items")


@attr.s(auto_attribs=True)
class Items:
    """Container for a list of items.

    Attributes:
        items (Union[Unset, List[CoreItem]]): An arraylist of all the items.
        total (Union[Unset, int]): The total number of items retrieved.
        warnings (Union[Unset, List[Error]]): An array of warning messages. These types of errors do not prevent the
            method from executing but should be checked.
    """

    items: Union[Unset, List[CoreItem]] = UNSET
    total: Union[Unset, int] = UNSET
    warnings: Union[Unset, List[Error]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        items: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.items, Unset):
            items = []
            for items_item_data in self.items:
                items_item = items_item_data.to_dict()

                items.append(items_item)

        total = self.total
        warnings: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = []
            for warnings_item_data in self.warnings:
                warnings_item = warnings_item_data.to_dict()

                warnings.append(warnings_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if items is not UNSET:
            field_dict["items"] = items
        if total is not UNSET:
            field_dict["total"] = total
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        items = []
        _items = d.pop("items", UNSET)
        for items_item_data in _items or []:
            items_item = CoreItem.from_dict(items_item_data)

            items.append(items_item)

        total = d.pop("total", UNSET)

        warnings = []
        _warnings = d.pop("warnings", UNSET)
        for warnings_item_data in _warnings or []:
            warnings_item = Error.from_dict(warnings_item_data)

            warnings.append(warnings_item)

        items = cls(
            items=items,
            total=total,
            warnings=warnings,
        )

        items.additional_properties = d
        return items

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
