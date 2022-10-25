from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="SellerCustomPolicy")


@attr.s(auto_attribs=True)
class SellerCustomPolicy:
    """The container for custom policies that apply to a listed item.

    Attributes:
        description (Union[Unset, str]): The seller-defined description of the policy.
        label (Union[Unset, str]): The seller-defined label for an individual custom policy.
        type (Union[Unset, str]): The type of custom policy, such as PRODUCT_COMPLIANCE or TAKE_BACK. For implementation
            help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:SellerCustomPolicyTypeEnum'>eBay API documentation</a>
    """

    description: Union[Unset, str] = UNSET
    label: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        description = self.description
        label = self.label
        type = self.type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if description is not UNSET:
            field_dict["description"] = description
        if label is not UNSET:
            field_dict["label"] = label
        if type is not UNSET:
            field_dict["type"] = type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        description = d.pop("description", UNSET)

        label = d.pop("label", UNSET)

        type = d.pop("type", UNSET)

        seller_custom_policy = cls(
            description=description,
            label=label,
            type=type,
        )

        seller_custom_policy.additional_properties = d
        return seller_custom_policy

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
