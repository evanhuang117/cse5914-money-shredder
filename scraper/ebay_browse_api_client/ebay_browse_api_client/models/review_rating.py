from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.rating_histogram import RatingHistogram
from ..types import UNSET, Unset

T = TypeVar("T", bound="ReviewRating")


@attr.s(auto_attribs=True)
class ReviewRating:
    """The type that defines the fields for the rating of a product review.

    Attributes:
        average_rating (Union[Unset, str]): The average rating given to a product based on customer reviews.
        rating_histograms (Union[Unset, List[RatingHistogram]]): An array of containers for the product rating
            histograms that shows the review counts and the product rating.
        review_count (Union[Unset, int]): The total number of reviews for the item.
    """

    average_rating: Union[Unset, str] = UNSET
    rating_histograms: Union[Unset, List[RatingHistogram]] = UNSET
    review_count: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        average_rating = self.average_rating
        rating_histograms: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rating_histograms, Unset):
            rating_histograms = []
            for rating_histograms_item_data in self.rating_histograms:
                rating_histograms_item = rating_histograms_item_data.to_dict()

                rating_histograms.append(rating_histograms_item)

        review_count = self.review_count

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if average_rating is not UNSET:
            field_dict["averageRating"] = average_rating
        if rating_histograms is not UNSET:
            field_dict["ratingHistograms"] = rating_histograms
        if review_count is not UNSET:
            field_dict["reviewCount"] = review_count

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        average_rating = d.pop("averageRating", UNSET)

        rating_histograms = []
        _rating_histograms = d.pop("ratingHistograms", UNSET)
        for rating_histograms_item_data in _rating_histograms or []:
            rating_histograms_item = RatingHistogram.from_dict(rating_histograms_item_data)

            rating_histograms.append(rating_histograms_item)

        review_count = d.pop("reviewCount", UNSET)

        review_rating = cls(
            average_rating=average_rating,
            rating_histograms=rating_histograms,
            review_count=review_count,
        )

        review_rating.additional_properties = d
        return review_rating

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
