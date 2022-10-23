from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aspect_value_distribution import AspectValueDistribution
from ..types import UNSET, Unset

T = TypeVar("T", bound="AspectDistribution")


@attr.s(auto_attribs=True)
class AspectDistribution:
    """The type that define the fields for the aspect information. Aspects are the variations of an item, such as color,
    size, etc.

        Attributes:
            aspect_value_distributions (Union[Unset, List[AspectValueDistribution]]): An array of containers for the various
                values of the aspect and the match count and a HATEOAS reference (<b> refinementHref</b>) for this aspect.
            localized_aspect_name (Union[Unset, str]): The name of an aspect, such as Brand, Color, etc.
    """

    aspect_value_distributions: Union[Unset, List[AspectValueDistribution]] = UNSET
    localized_aspect_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aspect_value_distributions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aspect_value_distributions, Unset):
            aspect_value_distributions = []
            for aspect_value_distributions_item_data in self.aspect_value_distributions:
                aspect_value_distributions_item = aspect_value_distributions_item_data.to_dict()

                aspect_value_distributions.append(aspect_value_distributions_item)

        localized_aspect_name = self.localized_aspect_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_value_distributions is not UNSET:
            field_dict["aspectValueDistributions"] = aspect_value_distributions
        if localized_aspect_name is not UNSET:
            field_dict["localizedAspectName"] = localized_aspect_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aspect_value_distributions = []
        _aspect_value_distributions = d.pop("aspectValueDistributions", UNSET)
        for aspect_value_distributions_item_data in _aspect_value_distributions or []:
            aspect_value_distributions_item = AspectValueDistribution.from_dict(aspect_value_distributions_item_data)

            aspect_value_distributions.append(aspect_value_distributions_item)

        localized_aspect_name = d.pop("localizedAspectName", UNSET)

        aspect_distribution = cls(
            aspect_value_distributions=aspect_value_distributions,
            localized_aspect_name=localized_aspect_name,
        )

        aspect_distribution.additional_properties = d
        return aspect_distribution

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
