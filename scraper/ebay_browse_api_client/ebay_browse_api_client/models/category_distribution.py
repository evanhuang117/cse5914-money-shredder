from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CategoryDistribution")


@attr.s(auto_attribs=True)
class CategoryDistribution:
    """The container that defines the fields for the category refinements. This container is returned when <b>
    fieldgroups</b> is set to <code>CATEGORY_REFINEMENTS</code> or <code>FULL</code> in the request.

        Attributes:
            category_id (Union[Unset, str]): The identifier of the category.
            category_name (Union[Unset, str]): The name of the category, such as Baby & Toddler Clothing.
            match_count (Union[Unset, int]): The number of items in this category.
            refinement_href (Union[Unset, str]): The HATEOAS reference of this category.
    """

    category_id: Union[Unset, str] = UNSET
    category_name: Union[Unset, str] = UNSET
    match_count: Union[Unset, int] = UNSET
    refinement_href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        category_id = self.category_id
        category_name = self.category_name
        match_count = self.match_count
        refinement_href = self.refinement_href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if category_id is not UNSET:
            field_dict["categoryId"] = category_id
        if category_name is not UNSET:
            field_dict["categoryName"] = category_name
        if match_count is not UNSET:
            field_dict["matchCount"] = match_count
        if refinement_href is not UNSET:
            field_dict["refinementHref"] = refinement_href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        category_id = d.pop("categoryId", UNSET)

        category_name = d.pop("categoryName", UNSET)

        match_count = d.pop("matchCount", UNSET)

        refinement_href = d.pop("refinementHref", UNSET)

        category_distribution = cls(
            category_id=category_id,
            category_name=category_name,
            match_count=match_count,
            refinement_href=refinement_href,
        )

        category_distribution.additional_properties = d
        return category_distribution

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
