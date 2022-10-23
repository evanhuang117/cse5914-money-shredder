from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConditionDistribution")


@attr.s(auto_attribs=True)
class ConditionDistribution:
    """The container that defines the fields for the conditions refinements. This container is returned when <b>
    fieldgroups</b> is set to <code>CONDITION_REFINEMENTS</code> or <code>FULL</code> in the request.

        Attributes:
            condition (Union[Unset, str]): The text describing the condition of the item, such as New or Used. For a list of
                condition names, see <a href="https://developer.ebay.com/devzone/finding/callref/enums/conditionIdList.html "
                target="_blank">Item Condition IDs and Names</a>.  <br /><br />Code so that your app gracefully handles any
                future changes to this list.
            condition_id (Union[Unset, str]): The identifier of the condition. For example, 1000 is the identifier for NEW.
            match_count (Union[Unset, int]): The number of items having the condition.
            refinement_href (Union[Unset, str]): The HATEOAS reference of this condition.
    """

    condition: Union[Unset, str] = UNSET
    condition_id: Union[Unset, str] = UNSET
    match_count: Union[Unset, int] = UNSET
    refinement_href: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        condition = self.condition
        condition_id = self.condition_id
        match_count = self.match_count
        refinement_href = self.refinement_href

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if condition is not UNSET:
            field_dict["condition"] = condition
        if condition_id is not UNSET:
            field_dict["conditionId"] = condition_id
        if match_count is not UNSET:
            field_dict["matchCount"] = match_count
        if refinement_href is not UNSET:
            field_dict["refinementHref"] = refinement_href

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        condition = d.pop("condition", UNSET)

        condition_id = d.pop("conditionId", UNSET)

        match_count = d.pop("matchCount", UNSET)

        refinement_href = d.pop("refinementHref", UNSET)

        condition_distribution = cls(
            condition=condition,
            condition_id=condition_id,
            match_count=match_count,
            refinement_href=refinement_href,
        )

        condition_distribution.additional_properties = d
        return condition_distribution

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
