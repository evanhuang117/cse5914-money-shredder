from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConvertedAmount")


@attr.s(auto_attribs=True)
class ConvertedAmount:
    """This type defines the monetary value of an amount. It can provide the amount in both the currency used on the eBay
    site where an item is being offered and the conversion of that value into another currency, if applicable.

        Attributes:
            converted_from_currency (Union[Unset, str]): The three-letter <a href="https://www.iso.org/iso-4217-currency-
                codes.html " target="_blank">ISO 4217</a> code representing the currency of the amount in the <b>
                convertedFromValue</b> field. This value is required or returned only if currency conversion/localization is
                required, and represents the pre-conversion currency. For implementation help, refer to <a
                href='https://developer.ebay.com/api-docs/buy/browse/types/ba:CurrencyCodeEnum'>eBay API documentation</a>
            converted_from_value (Union[Unset, str]): The monetary amount before any conversion is performed, in the
                currency specified by the <b> convertedFromCurrency</b> field. This value is required or returned only if
                currency conversion/localization is required. The <b> value</b> field contains the converted amount of this
                value, in the currency specified by the <b> currency</b> field.
            currency (Union[Unset, str]): The three-letter <a href="https://www.iso.org/iso-4217-currency-codes.html "
                target="_blank">ISO 4217</a> code representing the currency of the amount in the <b> value</b> field. If
                currency conversion/localization is required, this is the post-conversion currency of the amount in the <b>
                value</b> field.   <br /><br /><b> Default:</b> The currency of the authenticated user's country. For
                implementation help, refer to <a href='https://developer.ebay.com/api-
                docs/buy/browse/types/ba:CurrencyCodeEnum'>eBay API documentation</a>
            value (Union[Unset, str]): The monetary amount, in the currency specified by the <b> currency</b> field. If
                currency conversion/localization is required, this value is the converted amount, and the <b>
                convertedFromValue</b> field contains the amount in the original currency.
    """

    converted_from_currency: Union[Unset, str] = UNSET
    converted_from_value: Union[Unset, str] = UNSET
    currency: Union[Unset, str] = UNSET
    value: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        converted_from_currency = self.converted_from_currency
        converted_from_value = self.converted_from_value
        currency = self.currency
        value = self.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if converted_from_currency is not UNSET:
            field_dict["convertedFromCurrency"] = converted_from_currency
        if converted_from_value is not UNSET:
            field_dict["convertedFromValue"] = converted_from_value
        if currency is not UNSET:
            field_dict["currency"] = currency
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        converted_from_currency = d.pop("convertedFromCurrency", UNSET)

        converted_from_value = d.pop("convertedFromValue", UNSET)

        currency = d.pop("currency", UNSET)

        value = d.pop("value", UNSET)

        converted_amount = cls(
            converted_from_currency=converted_from_currency,
            converted_from_value=converted_from_value,
            currency=currency,
            value=value,
        )

        converted_amount.additional_properties = d
        return converted_amount

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
