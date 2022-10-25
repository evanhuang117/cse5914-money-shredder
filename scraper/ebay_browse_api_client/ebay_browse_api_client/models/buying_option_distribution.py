from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BuyingOptionDistribution")


@attr.s(auto_attribs=True)
class BuyingOptionDistribution:
    """The container that defines the fields for the buying options refinements. This container is returned when <b>
    fieldgroups</b> is set to <code>BUYING_OPTION_REFINEMENTS</code> or <code>FULL</code> in the request.

        Attributes:
            buying_option (Union[Unset, str]): The container that returns the buying option type. This will be AUCTION,
                FIXED_PRICE, CLASSIFIED_AD, or a combination of these options. For details, see <a href="/api-
                docs/buy/browse/resources/item_summary/methods/search#response.itemSummaries.buyingOptions">buyingOptions</a>.
            match_count (Union[Unset, int]): The number of items having this buying option.
            refinement_href (Union[Unset, str]): The HATEOAS reference for this buying option.
    """

    buying_option: Union[Unset, str] = UNSET
    match_count: Union[Unset, int] = UNSET
    refinement_href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        buying_option = self.buying_option
        match_count = self.match_count
        refinement_href = self.refinement_href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if buying_option is not UNSET:
            field_dict["buyingOption"] = buying_option
        if match_count is not UNSET:
            field_dict["matchCount"] = match_count
        if refinement_href is not UNSET:
            field_dict["refinementHref"] = refinement_href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        buying_option = d.pop("buyingOption", UNSET)

        match_count = d.pop("matchCount", UNSET)

        refinement_href = d.pop("refinementHref", UNSET)

        buying_option_distribution = cls(
            buying_option=buying_option,
            match_count=match_count,
            refinement_href=refinement_href,
        )

        buying_option_distribution.additional_properties = d
        return buying_option_distribution

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
