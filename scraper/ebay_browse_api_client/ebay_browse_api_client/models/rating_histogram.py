from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="RatingHistogram")


@attr.s(auto_attribs=True)
class RatingHistogram:
    """The type that defines the fields for product ratings. Only products that are in the eBay product catalog can be
    reviewed and rated.

        Attributes:
            count (Union[Unset, int]): The total number of user ratings that the product has received.
            rating (Union[Unset, str]): This is the average rating for the product. As part of a product review, users rate
                the product. Products are rated from one star (terrible) to five stars (excellent), with each star having a
                corresponding point value - one star gets 1 point, two stars get 2 points, and so on. If a product had one four-
                star rating and one five-star rating, its average rating would be <code> 4.5</code>, and this is the value that
                would appear in this field.
    """

    count: Union[Unset, int] = UNSET
    rating: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count = self.count
        rating = self.rating

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count is not UNSET:
            field_dict["count"] = count
        if rating is not UNSET:
            field_dict["rating"] = rating

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count = d.pop("count", UNSET)

        rating = d.pop("rating", UNSET)

        rating_histogram = cls(
            count=count,
            rating=rating,
        )

        rating_histogram.additional_properties = d
        return rating_histogram

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
