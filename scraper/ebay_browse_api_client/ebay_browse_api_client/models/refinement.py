from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.aspect_distribution import AspectDistribution
from ..models.buying_option_distribution import BuyingOptionDistribution
from ..models.category_distribution import CategoryDistribution
from ..models.condition_distribution import ConditionDistribution
from ..types import UNSET, Unset

T = TypeVar("T", bound="Refinement")


@attr.s(auto_attribs=True)
class Refinement:
    """This type defines the fields for the various refinements of an item. You can use the information in this container
    to create histograms, which help shoppers choose exactly what they want.

        Attributes:
            aspect_distributions (Union[Unset, List[AspectDistribution]]): An array of containers for the all the aspect
                refinements.
            buying_option_distributions (Union[Unset, List[BuyingOptionDistribution]]): An array of containers for the all
                the buying option refinements.
            category_distributions (Union[Unset, List[CategoryDistribution]]): An array of containers for the all the
                category refinements.
            condition_distributions (Union[Unset, List[ConditionDistribution]]): An array of containers for the all the
                condition refinements.
            dominant_category_id (Union[Unset, str]): The identifier of the category that most of the items are part of.
    """

    aspect_distributions: Union[Unset, List[AspectDistribution]] = UNSET
    buying_option_distributions: Union[Unset, List[BuyingOptionDistribution]] = UNSET
    category_distributions: Union[Unset, List[CategoryDistribution]] = UNSET
    condition_distributions: Union[Unset, List[ConditionDistribution]] = UNSET
    dominant_category_id: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        aspect_distributions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.aspect_distributions, Unset):
            aspect_distributions = []
            for aspect_distributions_item_data in self.aspect_distributions:
                aspect_distributions_item = aspect_distributions_item_data.to_dict()

                aspect_distributions.append(aspect_distributions_item)

        buying_option_distributions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.buying_option_distributions, Unset):
            buying_option_distributions = []
            for buying_option_distributions_item_data in self.buying_option_distributions:
                buying_option_distributions_item = buying_option_distributions_item_data.to_dict()

                buying_option_distributions.append(buying_option_distributions_item)

        category_distributions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.category_distributions, Unset):
            category_distributions = []
            for category_distributions_item_data in self.category_distributions:
                category_distributions_item = category_distributions_item_data.to_dict()

                category_distributions.append(category_distributions_item)

        condition_distributions: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.condition_distributions, Unset):
            condition_distributions = []
            for condition_distributions_item_data in self.condition_distributions:
                condition_distributions_item = condition_distributions_item_data.to_dict()

                condition_distributions.append(condition_distributions_item)

        dominant_category_id = self.dominant_category_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if aspect_distributions is not UNSET:
            field_dict["aspectDistributions"] = aspect_distributions
        if buying_option_distributions is not UNSET:
            field_dict["buyingOptionDistributions"] = buying_option_distributions
        if category_distributions is not UNSET:
            field_dict["categoryDistributions"] = category_distributions
        if condition_distributions is not UNSET:
            field_dict["conditionDistributions"] = condition_distributions
        if dominant_category_id is not UNSET:
            field_dict["dominantCategoryId"] = dominant_category_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        aspect_distributions = []
        _aspect_distributions = d.pop("aspectDistributions", UNSET)
        for aspect_distributions_item_data in _aspect_distributions or []:
            aspect_distributions_item = AspectDistribution.from_dict(aspect_distributions_item_data)

            aspect_distributions.append(aspect_distributions_item)

        buying_option_distributions = []
        _buying_option_distributions = d.pop("buyingOptionDistributions", UNSET)
        for buying_option_distributions_item_data in _buying_option_distributions or []:
            buying_option_distributions_item = BuyingOptionDistribution.from_dict(buying_option_distributions_item_data)

            buying_option_distributions.append(buying_option_distributions_item)

        category_distributions = []
        _category_distributions = d.pop("categoryDistributions", UNSET)
        for category_distributions_item_data in _category_distributions or []:
            category_distributions_item = CategoryDistribution.from_dict(category_distributions_item_data)

            category_distributions.append(category_distributions_item)

        condition_distributions = []
        _condition_distributions = d.pop("conditionDistributions", UNSET)
        for condition_distributions_item_data in _condition_distributions or []:
            condition_distributions_item = ConditionDistribution.from_dict(condition_distributions_item_data)

            condition_distributions.append(condition_distributions_item)

        dominant_category_id = d.pop("dominantCategoryId", UNSET)

        refinement = cls(
            aspect_distributions=aspect_distributions,
            buying_option_distributions=buying_option_distributions,
            category_distributions=category_distributions,
            condition_distributions=condition_distributions,
            dominant_category_id=dominant_category_id,
        )

        refinement.additional_properties = d
        return refinement

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
