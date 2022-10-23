from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectValueDistribution")


@attr.s(auto_attribs=True)
class AspectValueDistribution:
    """The container that defines the fields for the conditions refinements. This container is returned when <b>
    fieldgroups</b> is set to <code>ASPECT_REFINEMENTS</code> or <code>FULL</code> in the request.

        Attributes:
            localized_aspect_value (Union[Unset, str]): The value of an aspect. For example, Red is a value for the aspect
                Color.
            match_count (Union[Unset, int]): The number of items with this aspect.
            refinement_href (Union[Unset, str]): A HATEOAS reference for this aspect.
    """

    localized_aspect_value: Union[Unset, str] = UNSET
    match_count: Union[Unset, int] = UNSET
    refinement_href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        localized_aspect_value = self.localized_aspect_value
        match_count = self.match_count
        refinement_href = self.refinement_href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if localized_aspect_value is not UNSET:
            field_dict["localizedAspectValue"] = localized_aspect_value
        if match_count is not UNSET:
            field_dict["matchCount"] = match_count
        if refinement_href is not UNSET:
            field_dict["refinementHref"] = refinement_href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        localized_aspect_value = d.pop("localizedAspectValue", UNSET)

        match_count = d.pop("matchCount", UNSET)

        refinement_href = d.pop("refinementHref", UNSET)

        aspect_value_distribution = cls(
            localized_aspect_value=localized_aspect_value,
            match_count=match_count,
            refinement_href=refinement_href,
        )

        aspect_value_distribution.additional_properties = d
        return aspect_value_distribution

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
