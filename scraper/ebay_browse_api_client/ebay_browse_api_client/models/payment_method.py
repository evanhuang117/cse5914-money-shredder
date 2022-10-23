from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.payment_method_brand import PaymentMethodBrand
from ..types import UNSET, Unset

T = TypeVar("T", bound="PaymentMethod")


@attr.s(auto_attribs=True)
class PaymentMethod:
    """
    Attributes:
        payment_method_type (Union[Unset, str]): The payment method type, such as credit card or cash. For
            implementation help, refer to <a href='https://developer.ebay.com/api-
            docs/buy/browse/types/gct:PaymentMethodTypeEnum'>eBay API documentation</a>
        payment_method_brands (Union[Unset, List[PaymentMethodBrand]]): The payment method brands, including the payment
            method brand type and logo image.
        payment_instructions (Union[Unset, List[str]]): The payment instructions for the buyer, such as <i>cash in
            person</i> or <i>contact seller</i>.
        seller_instructions (Union[Unset, List[str]]): The seller instructions to the buyer, such as <i>accepts credit
            cards</i> or <i>see description</i>.
    """

    payment_method_type: Union[Unset, str] = UNSET
    payment_method_brands: Union[Unset, List[PaymentMethodBrand]] = UNSET
    payment_instructions: Union[Unset, List[str]] = UNSET
    seller_instructions: Union[Unset, List[str]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        payment_method_type = self.payment_method_type
        payment_method_brands: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.payment_method_brands, Unset):
            payment_method_brands = []
            for payment_method_brands_item_data in self.payment_method_brands:
                payment_method_brands_item = payment_method_brands_item_data.to_dict()

                payment_method_brands.append(payment_method_brands_item)

        payment_instructions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.payment_instructions, Unset):
            payment_instructions = self.payment_instructions

        seller_instructions: Union[Unset, List[str]] = UNSET
        if not isinstance(self.seller_instructions, Unset):
            seller_instructions = self.seller_instructions

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if payment_method_type is not UNSET:
            field_dict["paymentMethodType"] = payment_method_type
        if payment_method_brands is not UNSET:
            field_dict["paymentMethodBrands"] = payment_method_brands
        if payment_instructions is not UNSET:
            field_dict["paymentInstructions"] = payment_instructions
        if seller_instructions is not UNSET:
            field_dict["sellerInstructions"] = seller_instructions

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        payment_method_type = d.pop("paymentMethodType", UNSET)

        payment_method_brands = []
        _payment_method_brands = d.pop("paymentMethodBrands", UNSET)
        for payment_method_brands_item_data in _payment_method_brands or []:
            payment_method_brands_item = PaymentMethodBrand.from_dict(payment_method_brands_item_data)

            payment_method_brands.append(payment_method_brands_item)

        payment_instructions = cast(List[str], d.pop("paymentInstructions", UNSET))

        seller_instructions = cast(List[str], d.pop("sellerInstructions", UNSET))

        payment_method = cls(
            payment_method_type=payment_method_type,
            payment_method_brands=payment_method_brands,
            payment_instructions=payment_instructions,
            seller_instructions=seller_instructions,
        )

        payment_method.additional_properties = d
        return payment_method

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
