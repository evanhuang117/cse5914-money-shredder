from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CommonDescriptions")


@attr.s(auto_attribs=True)
class CommonDescriptions:
    """The type that defines the fields for the item ids that all use a common description.  Often the item variations
    within an item group all have the same description. Instead of repeating this description in the item details of
    each item, a description that is shared by at least one other item is returned in this container. If the description
    is unique, it is returned in the <b> items.description</b> field.

        Attributes:
            description (Union[Unset, str]): The item description that is used by more than one of the item variations.
            item_ids (Union[Unset, List[str]]): A list of item ids that have this description.
    """

    description: Union[Unset, str] = UNSET
    item_ids: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        item_ids: Union[Unset, List[str]] = UNSET
        if not isinstance(self.item_ids, Unset):
            item_ids = self.item_ids

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if item_ids is not UNSET:
            field_dict["itemIds"] = item_ids

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        item_ids = cast(List[str], d.pop("itemIds", UNSET))

        common_descriptions = cls(
            description=description,
            item_ids=item_ids,
        )

        common_descriptions.additional_properties = d
        return common_descriptions

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
