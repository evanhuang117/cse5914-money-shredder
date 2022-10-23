from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Category")


@attr.s(auto_attribs=True)
class Category:
    """This type is used by the <b>categories</b> container in the response of the <b>search</b>  method, and contains the
    name and ID of the item category.

        Attributes:
            category_id (Union[Unset, str]): The unique identifier of the category.
            category_name (Union[Unset, str]): The name of the category.
    """

    category_id: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id
        category_name = self.category_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_name = d.pop("categoryName", UNSET)

        category = cls(
            category_id=category_id,
            category_name=category_name,
        )

        category.additional_properties = d
        return category

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
