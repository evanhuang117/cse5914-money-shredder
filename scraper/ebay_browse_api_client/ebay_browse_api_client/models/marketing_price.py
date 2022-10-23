from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.converted_amount import ConvertedAmount
from ..types import UNSET, Unset

T = TypeVar("T", bound="MarketingPrice")


@attr.s(auto_attribs=True)
class MarketingPrice:
    """The type that defines the fields that describe a seller discount.

    Attributes:
        discount_amount (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        discount_percentage (Union[Unset, str]): This field expresses the percentage of the seller discount based on the
            value in the <b>  originalPrice</b> container.
        original_price (Union[Unset, ConvertedAmount]): This type defines the monetary value of an amount. It can
            provide the amount in both the currency used on the eBay site where an item is being offered and the conversion
            of that value into another currency, if applicable.
        price_treatment (Union[Unset, str]): Indicates the pricing treatment (discount) that was applied to the price of
            the item. <br /><br /><span class="tablenote"><b>Note: </b> The pricing treatment affects the way and where the
            discounted price can be displayed.</span> For implementation help, refer to <a
            href='https://developer.ebay.com/api-docs/buy/browse/types/gct:PriceTreatmentEnum'>eBay API documentation</a>
    """

    discount_amount: Union[Unset, ConvertedAmount] = UNSET
    discount_percentage: Union[Unset, str] = UNSET
    original_price: Union[Unset, ConvertedAmount] = UNSET
    price_treatment: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        discount_amount: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.discount_amount, Unset):
            discount_amount = self.discount_amount.to_dict()

        discount_percentage = self.discount_percentage
        original_price: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.original_price, Unset):
            original_price = self.original_price.to_dict()

        price_treatment = self.price_treatment

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if discount_amount is not UNSET:
            field_dict["discountAmount"] = discount_amount
        if discount_percentage is not UNSET:
            field_dict["discountPercentage"] = discount_percentage
        if original_price is not UNSET:
            field_dict["originalPrice"] = original_price
        if price_treatment is not UNSET:
            field_dict["priceTreatment"] = price_treatment

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _discount_amount = d.pop("discountAmount", UNSET)
        discount_amount: Union[Unset, ConvertedAmount]
        if isinstance(_discount_amount, Unset):
            discount_amount = UNSET
        else:
            discount_amount = ConvertedAmount.from_dict(_discount_amount)

        discount_percentage = d.pop("discountPercentage", UNSET)

        _original_price = d.pop("originalPrice", UNSET)
        original_price: Union[Unset, ConvertedAmount]
        if isinstance(_original_price, Unset):
            original_price = UNSET
        else:
            original_price = ConvertedAmount.from_dict(_original_price)

        price_treatment = d.pop("priceTreatment", UNSET)

        marketing_price = cls(
            discount_amount=discount_amount,
            discount_percentage=discount_percentage,
            original_price=original_price,
            price_treatment=price_treatment,
        )

        marketing_price.additional_properties = d
        return marketing_price

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
