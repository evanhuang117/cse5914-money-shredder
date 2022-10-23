from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.amount import Amount
from ..models.coupon_constraint import CouponConstraint
from ..types import UNSET, Unset

T = TypeVar("T", bound="AvailableCoupon")


@attr.s(auto_attribs=True)
class AvailableCoupon:
    """
    Attributes:
        constraint (Union[Unset, CouponConstraint]): This type is used to provide the expiration date of a coded coupon.
        discount_amount (Union[Unset, Amount]):
        discount_type (Union[Unset, str]): The type of discount that the coupon applies. For implementation help, refer
            to <a href='https://developer.ebay.com/api-docs/buy/browse/types/gct:CouponDiscountType'>eBay API
            documentation</a>
        message (Union[Unset, str]): A description of the coupon.<br /><br /><span class="tablenote"><b> Note: </b> The
            value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying coupons. The
            value in the <b>availableCoupons.message</b> field must also be included, if returned in the API
            response.</span>
        redemption_code (Union[Unset, str]): The coupon code.
        terms_web_url (Union[Unset, str]): The URL to the coupon terms of use.<br /><br /><span class="tablenote"><b>
            Note: </b> The value returned in the <b>termsWebUrl</b> field should appear for all experiences when displaying
            coupons. The value in the <b>availableCoupons.message</b> field must also be included, if returned in the API
            response.</span>
    """

    constraint: Union[Unset, CouponConstraint] = UNSET
    discount_amount: Union[Unset, Amount] = UNSET
    discount_type: Union[Unset, str] = UNSET
    message: Union[Unset, str] = UNSET
    redemption_code: Union[Unset, str] = UNSET
    terms_web_url: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        constraint: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.constraint, Unset):
            constraint = self.constraint.to_dict()

        discount_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount_amount, Unset):
            discount_amount = self.discount_amount.to_dict()

        discount_type = self.discount_type
        message = self.message
        redemption_code = self.redemption_code
        terms_web_url = self.terms_web_url

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if constraint is not UNSET:
            field_dict["constraint"] = constraint
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if discount_type is not UNSET:
            field_dict["discountType"] = discount_type
        if message is not UNSET:
            field_dict["message"] = message
        if redemption_code is not UNSET:
            field_dict["redemptionCode"] = redemption_code
        if terms_web_url is not UNSET:
            field_dict["termsWebUrl"] = terms_web_url

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _constraint = d.pop("constraint", UNSET)
        constraint: Union[Unset, CouponConstraint]
        if isinstance(_constraint, Unset):
            constraint = UNSET
        else:
            constraint = CouponConstraint.from_dict(_constraint)

        _discount_amount = d.pop("discountAmount", UNSET)
        discount_amount: Union[Unset, Amount]
        if isinstance(_discount_amount, Unset):
            discount_amount = UNSET
        else:
            discount_amount = Amount.from_dict(_discount_amount)

        discount_type = d.pop("discountType", UNSET)

        message = d.pop("message", UNSET)

        redemption_code = d.pop("redemptionCode", UNSET)

        terms_web_url = d.pop("termsWebUrl", UNSET)

        available_coupon = cls(
            constraint=constraint,
            discount_amount=discount_amount,
            discount_type=discount_type,
            message=message,
            redemption_code=redemption_code,
            terms_web_url=terms_web_url,
        )

        available_coupon.additional_properties = d
        return available_coupon

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
